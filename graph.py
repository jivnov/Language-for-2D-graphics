import uuid
from enum import Enum
from typing import Any, Dict, List, Set, Tuple


class UndeclaredShapeError(NameError):
    pass


class UndefinedShapeError(ValueError):
    pass


class RedundantRelationError(NameError):
    pass


class UndefinedRelationError(ValueError):
    pass


class RedefiningExplicitRelationError(ValueError):
    pass


class CyclicRelationsError(ValueError):
    pass


class Shape(Enum):
    SQUARE = 1
    CIRCLE = 2
    RECT = 3
    TRIANGLE = 4
    SHAPE = 5

    @staticmethod
    def from_string(shape_name: str):
        if shape_name.lower() == "rect":
            return Shape.RECT
        elif shape_name.lower() == "square":
            return Shape.SQUARE
        elif shape_name.lower() == "circle":
            return Shape.CIRCLE
        elif shape_name.lower() == "triangle":
            return Shape.TRIANGLE
        elif shape_name.lower() == "shape":
            return Shape.SHAPE
        else:
            raise UndefinedShapeError


class Relation(Enum):
    # TODO: [Note for the future] For a relation to be true between a graph G and a vertex V it should be true between V and each vertex of graph G
    UNRELATED = 0
    LEFT = 1
    RIGHT = -1
    TOP = 2
    BOT = -2
    IN = 3
    CONTAINED = -3  # Opposite of IN
    ON = 4
    UNDER = -4

    def __neg__(self):
        return Relation(-self.value)

    @staticmethod
    def from_string(relation_name: str):
        if relation_name.upper() == "LEFT":
            return Relation.LEFT
        elif relation_name.upper() == "RIGHT":
            return Relation.RIGHT
        elif relation_name.upper() == "TOP":
            return Relation.TOP
        elif relation_name.upper() == "BOT":
            return Relation.BOT
        elif relation_name.upper() == "IN":
            return Relation.IN
        elif relation_name.upper() == "CONTAINED":
            return Relation.CONTAINED
        elif relation_name.upper() == "ON":
            return Relation.ON
        elif relation_name.upper() == "UNDER":
            return Relation.UNDER
        else:
            raise UndefinedRelationError


class Vertex:
    def __init__(self, parent_graph, var_name: str, shape, args: Any = None, content=None):
        # TODO: Every vertex begins as its own graph which then merges with other graphs through relations
        """

        :param parent_graph: Graph that contains this Vertex
        :param var_name: Name of the variable referencing this shape in code
        :param shape: Type of this variable
        :param args: Arguments passed to the variable initialization in code
        :param content: Type should be Graph or None; allows for comparison between graphs and shapes
        """
        # DONE: Vertex should have a reference to its Graph to track some more "global" properties (e.x. the total
        # width and height of the drawing it is a part of)
        self.name = var_name
        if isinstance(shape, Shape):
            self.shape = shape
        else:
            self.shape = Shape.from_string(shape)
        self.bb_w = 0.0

        self.updated = False
        self.drawn = False

        self.content = None  # Should only be not-None if this Vertex is actually a Graph (this allows defining Vertex to Graph relations)

        self.LEFT: Set[Vertex] = set()
        self.RIGHT: Set[Vertex] = set()
        self.TOP: Set[Vertex] = set()
        self.BOT: Set[Vertex] = set()
        self.IN: Vertex = None
        self.CONTAINED: Set[Vertex] = set()
        self.ON: Set[Vertex] = set()
        self.UNDER: Set[Vertex] = set()

        self.graph = parent_graph  # Graph that this shape is a part of
        self.uid = uuid.uuid1()  # This will allow editting svg files after calling draw() on parts of the graph; the
        # program can reference any shape by its unique ID or at least try to make a unique variable for each unique ID
        # TODO: Opening SVG files for editing (e.x. after calling draw() you want to add some more shapes to the picture)

        # Determine Bounding Box fractional size through passed arguments
        if isinstance(args, list) and len(args) > 0:
            self.bb_w = int(args.pop(0).replace('%', '')) / 100
            if len(args) > 0:
                self.bb_h = int(args.pop(0).replace('%', '')) / 100
            else:
                self.bb_h = self.bb_w
        else:
            self.bb_w = 0.5
            self.bb_h = 0.5

        # Adjust Bounding Box fractional size based on shape
        self.adjust_size_based_on_shape()

        self.width = self.bb_w * 1000
        self.height = self.bb_h * 1000

        self.x = (1 - self.bb_w) * 500
        self.y = (1 - self.bb_h) * 500

        self.unreachable = False

    def adjust_size_based_on_shape(self):
        # Adjust Bounding Box fractional size based on shape
        if self.shape == Shape.SQUARE or self.shape == Shape.CIRCLE:
            self.bb_h = self.bb_w = min(self.bb_h, self.bb_w)

    # HORIZONTAL RELATIONS
    def is_left(self, other) -> bool:
        return self.x <= other.x - self.width

    def is_right(self, other) -> bool:
        return self.x >= other.x + other.width

    def center_horizontally_if_legal(self):
        if len(self.LEFT) == 0 and len(self.RIGHT) == 0:
            self.x = self.graph.x + self.graph.width / 2

    def center_vertically_if_legal(self):
        if len(self.TOP) == 0 and len(self.BOT) == 0:
            self.y = self.graph.y + self.graph.height / 2

    def center_if_legal(self):
        self.center_horizontally_if_legal()
        self.center_vertically_if_legal()

    def to_left_of(self, other):
        """
        Move this vertex to the left side of other vertex
        :param other:
        :return:
        """
        self.x = other.x - self.width

    def to_right_of(self, other):
        """
        Move this vertex to the right side of other vertex
        :param other:
        :return:
        """
        self.x = other.x + other.width

    # VERTICAL RELATIONS
    def is_top(self, other) -> bool:
        return self.y <= other.y - self.height

    def is_bot(self, other) -> bool:
        return self.y >= other.y + other.height

    def to_top_of(self, other):
        """
        Move this vertex to the left side of other vertex
        :param other:
        :return:
        """
        self.y = other.y - self.height

    def to_bot_of(self, other):
        """
        Move this vertex to the right side of other vertex
        :param other:
        :return:
        """
        self.y = other.y + other.height

    def add_neighbour(self, v, relation: Relation):
        # TODO: [Note for the future] This method might not be necessary as querying graph.relation_matrix_XYZ[v1][v2] is quite intuitive BUT every vertex has to be a part of some graph at all times
        """
        Adds a new vertex with given relation to this one's neighbours and this one to the new vertex's with an opposite relation
        :param v: New vertex neighbour of self
        :param relation: Relation of self to neighbour vertex; read: "self RELATION v", e.x. for relation=Relation.LEFT: "self LEFT v", so "v RIGHT self"
        :return:
        """
        if relation == Relation.LEFT:
            v.LEFT.add(self)
            self.RIGHT.add(v)
        elif relation == Relation.RIGHT:
            v.RIGHT.add(self)
            self.LEFT.add(v)
        elif relation == Relation.TOP:
            v.TOP.add(self)
            self.BOT.add(v)
        elif relation == Relation.BOT:
            v.BOT.add(self)
            self.TOP.add(v)
        elif relation == Relation.IN:
            v.IN = self
            self.CONTAINED.add(v)
        elif relation == Relation.CONTAINED:
            v.CONTAINED.add(self)
            self.IN = v
        elif relation == Relation.ON:
            v.ON.add(self)
            self.UNDER.add(v)
        elif relation == Relation.UNDER:
            v.UNDER.add(self)
            self.ON.add(v)
        else:
            print("rel: ", self.name, v.name, relation)
            raise UndefinedRelationError()

    def remove_neighbour(self, neighbour):
        if neighbour in self.LEFT:
            self.LEFT.remove(neighbour)
            neighbour.RIGHT.remove(self)
        elif neighbour in self.RIGHT:
            self.RIGHT.remove(neighbour)
            neighbour.LEFT.remove(self)
        elif neighbour in self.TOP:
            self.TOP.remove(neighbour)
            neighbour.BOT.remove(self)
        elif neighbour in self.BOT:
            self.BOT.remove(neighbour)
            neighbour.TOP.remove(self)
        elif neighbour == self.IN:
            self.IN = None
            neighbour.CONTAINED.remove(self)
        elif neighbour in self.CONTAINED:
            self.CONTAINED.remove(neighbour)
            neighbour.IN = None
        elif neighbour in self.ON:
            self.ON.add(neighbour)
            neighbour.UNDER.remove(self)
        elif neighbour in self.UNDER:
            self.UNDER.remove(neighbour)
            neighbour.ON.remove(self)


class Graph:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.vertices: Set[Vertex] = set()  # all unique vertices in a graph

        # Position of the top-left corner of this graph's bounding box
        self.x = x
        self.y = y

        # Width and height of this graph's bounding box (width in the widest point and height in the highest point)
        self.width = width
        self.height = height

        self.relation_matrix_horizontal: Dict[
            Vertex, Dict[Vertex, Relation]] = dict()  # all horizontal relations in the shape graph

        self.relation_matrix_vertical: Dict[
            Vertex, Dict[Vertex, Relation]] = dict()  # all vertical relations in the shape graph

    def add_vertex(self, v: Vertex):
        if v not in self.vertices:
            # Add relations between this new vertex and other old vertices
            self.relation_matrix_horizontal[v] = {other_v: Relation.UNRELATED for other_v in self.vertices}
            self.relation_matrix_vertical[v] = {other_v: Relation.UNRELATED for other_v in self.vertices}

            # Add relations between other old vertices and this new vertex
            for key in self.relation_matrix_horizontal.keys():
                if key is not v:
                    self.relation_matrix_horizontal[key][v] = Relation.UNRELATED

            for key in self.relation_matrix_vertical.keys():
                if key is not v:
                    self.relation_matrix_vertical[key][v] = Relation.UNRELATED

            # Add new vertex to vertices set
            self.vertices.add(v)

            # Give the vertex a reference to this Graph
            v.graph = self

            self.update_position_and_size()

    def add_relation(self, v_from: Vertex, v_to: Vertex, r: Relation):
        """
        :param v_from:
        :param v_to:
        :param r:

        :raises UndeclaredShapeError
        :raises RedundantRelationError
        :raises CyclicRelationsError

        :return:
        """
        # Both shapes should have already been added to this graph before defining relations between them
        if v_from is None or v_to is None or v_from not in self.vertices or v_to not in self.vertices:
            print(f"{v_from=} {v_to=}")
            raise UndeclaredShapeError

        if v_from is v_to:
            raise RedundantRelationError

        # Modify relation in respective matrix; note that you need to modify it for both vertices
        if r in (Relation.LEFT, Relation.RIGHT):
            self.relation_matrix_horizontal[v_from][v_to] = r
            self.relation_matrix_horizontal[v_to][v_from] = -r

            if self._invalid_horizontal_relations():
                raise CyclicRelationsError(f"Relation {r=} between {v_from.name=} and {v_to.name=} causes a cycle in horizontal relations")

            # Adjust shape positions in X axis
            self.sort_horizontal()
        elif r in (Relation.TOP, Relation.BOT):
            self.relation_matrix_vertical[v_from][v_to] = r
            self.relation_matrix_vertical[v_to][v_from] = -r

            if self._invalid_vertical_relations():
                raise CyclicRelationsError(f"Relation {r=} between {v_from.name=} and {v_to.name=} causes a cycle in vertical relations")

            # Adjust shape positions in X axis
            self.sort_vertical()
            # TODO: Implement incidence matrices for other relations
        else:
            return

        # TODO: [Note for the future] This method might not be necessary as querying graph.relation_matrix_XYZ[v1][v2] is quite intuitive BUT every vertex has to be a part of some graph
        # Give vertex info about new neighbour
        v_from.add_neighbour(v_to, r)

    def _is_cyclic_horizontal_util(self, v: Vertex, visited: Dict[Vertex, bool], rec_stack: Dict[Vertex, bool]) -> bool:
        """
        Visit vertex "v" and check if any neighbour was visited previously
        :param v: Vertex to check
        :param visited: Dictionary of vertices, keys are vertices, values are True if visited
        :param rec_stack: Keys are vertices, values are True if scheduled for visit
        :return:
        """
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        rec_stack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # rec_stack then graph is cyclic
        # NOTE: Only check LEFT relation
        for neighbour in (neigh for neigh, relation in self.relation_matrix_horizontal[v].items() if relation == Relation.LEFT):
            if not visited[neighbour]:
                if self._is_cyclic_horizontal_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        # The node needs to be popped from
        # recursion stack before function ends
        rec_stack[v] = False
        return False

    def _invalid_horizontal_relations(self) -> bool:
        """
        Check if there is a cycle in the horizontal relations graph
        :return: True if horizontal relations graph is cyclic
        """
        visited = {v: False for v in self.vertices}
        rec_stack = {v: False for v in self.vertices}
        for node in self.vertices:
            if not visited[node]:
                if self._is_cyclic_horizontal_util(node, visited, rec_stack):
                    return True
        return False

    def _is_cyclic_vertical_util(self, v: Vertex, visited: Dict[Vertex, bool], rec_stack: Dict[Vertex, bool]) -> bool:
        """
        Visit vertex "v" and check if any neighbour was visited previously
        :param v: Vertex to check
        :param visited: Dictionary of vertices, keys are vertices, values are True if visited
        :param rec_stack: Keys are vertices, values are True if scheduled for visit
        :return:
        """
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        rec_stack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # rec_stack then graph is cyclic
        # NOTE: Only check TOP relation
        for neighbour in (neigh for neigh, relation in self.relation_matrix_vertical[v].items() if relation == Relation.TOP):
            if not visited[neighbour]:
                if self._is_cyclic_vertical_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        # The node needs to be popped from
        # recursion stack before function ends
        rec_stack[v] = False
        return False

    def _invalid_vertical_relations(self) -> bool:
        """
        Check if there is a cycle in the vertical relations graph
        :return: True if vertical relations graph is cyclic
        """
        visited = {v: False for v in self.vertices}
        rec_stack = {v: False for v in self.vertices}
        for node in self.vertices:
            if not visited[node]:
                if self._is_cyclic_vertical_util(node, visited, rec_stack):
                    return True
        return False

    def print_relations(self, v: Vertex) -> None:
        # TODO generate SVG for provided parameters
        if v not in self.vertices:
            print("not in graph")
        else:
            print(f"Found vertex {v.name}")
            for v2, relation in self.relation_matrix_horizontal[v].items():
                vertex_name = v2.name
                vertex_relation = relation
                print(f"{v2.shape}:{vertex_name}")

    def merge_with(self, other, r: Relation = Relation.UNRELATED):
        # TODO: Parameter "r" taken into account (as stated in docstring)
        """
        Merge vertices and relations of the other graph into this one
        :param r: [optional] Make all self.vertices satisfy relation "r" with all other.vertices
        :param other: Other Graph
        :return:
        """
        # Add all new vertices
        for vertex in other.vertices:
            self.add_vertex(vertex)

        # Add all new relations
        for v1, relation_dict in other.relation_matrix_horizontal.items():
            for v2, relation in relation_dict.items():
                self.add_relation(v1, v2, relation)

        # Clear vertex data from other Graph (they are now a part of this one)
        other.vertices.clear()
        other.relation_matrix_horizontal.clear()

    def find_vertex(self, vertex_name: str) -> Vertex:
        for vertex in self.vertices:
            if str(vertex.name) == str(vertex_name):
                return vertex
        raise UndeclaredShapeError(vertex_name)

    def sort_horizontal(self):
        """
        Make sure all horizontal relations are valid
        :return:
        """
        for v1, relation_map in self.relation_matrix_horizontal.items():
            for v2, relation in relation_map.items():
                v2_was_leftmost = self.x == v2.x
                v2_was_rightmost = self.x + self.width == v2.x + v2.width

                # ALWAYS MOVE THE OTHER VERTEX
                if relation is Relation.LEFT and not v1.is_left(v2):
                    v2.to_right_of(v1)
                elif relation is Relation.RIGHT and not v1.is_right(v2):
                    v2.to_left_of(v1)

                # UPDATE GRAPH BOUNDING BOX VALUES
                self._update_horizontal()

    def sort_vertical(self):
        """
        Make sure all vertical relations are valid
        :return:
        """
        for v1, relation_map in self.relation_matrix_vertical.items():
            for v2, relation in relation_map.items():
                v2_was_topmost = self.y == v2.y
                v2_was_botmost = self.y + self.height == v2.y + v2.height

                # ALWAYS MOVE THE OTHER VERTEX
                if relation is Relation.TOP and not v1.is_top(v2):
                    v2.to_bot_of(v1)
                elif relation is Relation.BOT and not v1.is_bot(v2):
                    v2.to_top_of(v1)

                # UPDATE GRAPH BOUNDING BOX VALUES
                self._update_vertical()

    def _update_x(self):
        self.x = min(v.x for v in self.vertices)

    def _update_y(self):
        self.y = min(v.y for v in self.vertices)

    def _update_horizontal(self):
        self._update_x()
        self.width = max(v.x + v.width for v in self.vertices) - self.x

    def _update_vertical(self):
        self._update_y()
        self.height = max(v.y + v.height for v in self.vertices) - self.y

    def update_position_and_size(self):
        """
        Recalculate graph's X, Y, width and height based on its vertices
        :return:
        """
        self._update_horizontal()
        self._update_vertical()

    def move_horizontal(self, dist: int):
        """
        Shift all shapes by the given distance in the X axis.

        :param dist: Positive integer to move right, negative to move left
        :return:
        """
        for v in self.vertices:
            v.x += dist
        self.x += dist

    def move_vertical(self, dist: int):
        """
        Shift all shapes by the given distance in the Y axis.

        :param dist: Positive integer to move down, negative to move up
        :return:
        """
        for v in self.vertices:
            v.y += dist
        self.y += dist

    def center(self, pw, ph, px: int = 0, py: int = 0):
        """
        Center this graph in given parent dimensions
        :param pw: Parent width
        :param ph: Parent height
        :param px: Parent X; 0 for viewport
        :param py: Parent Y; 0 for viewport
        :return:
        """
        target_x = (pw - self.width) // 2 + px
        target_y = (ph - self.height) // 2 + py
        self.move_to(target_x, target_y)

    def move_to(self, x, y):
        if self.x != x:
            self.move_horizontal(x - self.x)
        if self.y != y:
            self.move_vertical(y - self.y)
            
    def replace_vertex(self, vertex_to_replace: Vertex, new_vertex: Vertex):

        self._copy_contents(vertex_to_replace, new_vertex)

        self.add_vertex(new_vertex)

        for v_from in self.relation_matrix_horizontal.keys():
            if v_from != new_vertex and v_from in self.vertices:
                for v_to in list(self.relation_matrix_horizontal[v_from].keys()):
                    if v_to == vertex_to_replace:
                        rel = self.relation_matrix_horizontal[v_from][v_to]
                        self.add_relation(v_from=v_from, v_to=new_vertex, r=rel)
                        if rel != Relation.UNRELATED:
                            v_from.add_neighbour(new_vertex, rel)
                            v_from.remove_neighbour(vertex_to_replace)
                        self.relation_matrix_horizontal[v_from].pop(vertex_to_replace)

        for v_from in self.relation_matrix_vertical.keys():
            if v_from != new_vertex and v_from in self.vertices:
                for v_to in list(self.relation_matrix_vertical[v_from].keys()):
                    if v_to == vertex_to_replace:
                        rel = self.relation_matrix_vertical[v_from][v_to]
                        self.add_relation(v_from = v_from, v_to = new_vertex, r = rel)
                        if rel != Relation.UNRELATED:
                            v_from.add_neighbour(new_vertex, rel)
                            v_from.remove_neighbour(vertex_to_replace)
                        self.relation_matrix_vertical[v_from].pop(vertex_to_replace)

        # Remove from graph in general
        self.vertices.remove(vertex_to_replace)

        # Remove from horizontal graph
        self.relation_matrix_horizontal.pop(vertex_to_replace)
        self.relation_matrix_horizontal[new_vertex].pop(vertex_to_replace)

        # Remove from vertical graph
        self.relation_matrix_vertical.pop(vertex_to_replace)
        self.relation_matrix_vertical[new_vertex].pop(vertex_to_replace)

    def _copy_contents(self, vertex_to_replace: Vertex, new_vertex: Vertex):

        new_vertex.bb_w = vertex_to_replace.bb_w
        new_vertex.bb_h = vertex_to_replace.bb_h

        new_vertex.updated = vertex_to_replace.updated
        new_vertex.drawn = vertex_to_replace.drawn
        new_vertex.content = vertex_to_replace.content

        #TODO: add IN relation

        relation_set_pairs = zip(
            [new_vertex.LEFT, new_vertex.RIGHT, new_vertex.TOP, new_vertex.BOT,
             new_vertex.CONTAINED, new_vertex.ON, new_vertex.UNDER],
            [vertex_to_replace.LEFT, vertex_to_replace.RIGHT, vertex_to_replace.TOP, vertex_to_replace.BOT,
             vertex_to_replace.CONTAINED, vertex_to_replace.ON, vertex_to_replace.UNDER]
        )

        for new_relation, replaced_relation in relation_set_pairs:
            if new_relation is not None:
                new_relation.update(replaced_relation)
            else:
                new_relation = replaced_relation

        new_vertex.uid = vertex_to_replace.uid
        new_vertex.graph = vertex_to_replace.graph

        new_vertex.adjust_size_based_on_shape()
