import uuid
from enum import Enum
from typing import Any, Dict, List, Set, Tuple


class UndeclaredShapeError(NameError):
    pass


class UndefinedShapeError(ValueError):
    pass


class RedundantRelationError(NameError):
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


class UndefinedRelationError(ValueError):
    pass


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
    def __init__(self, parent_graph, var_name: str, shape: str, args: Any, content=None):
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

    def adjust_size_based_on_shape(self):
        # Adjust Bounding Box fractional size based on shape
        if self.shape == Shape.SQUARE or self.shape == Shape.CIRCLE:
            self.bb_h = self.bb_w = min(self.bb_h, self.bb_w)

    def update_peers(self):
        if self.updated:
            return
        for v in self.LEFT:
            v.x = self.x - v.width
            v.updated = True
            v.update_peers()
        for v in self.RIGHT:
            v.x = self.x + self.width
            v.updated = True
            v.update_peers()

    def is_left(self, v) -> bool:
        return self.x <= v.x - self.width

    def is_right(self, v) -> bool:
        return self.x >= v.x + v.width

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
        # TODO: Rewrite below relations to conform to this method's docs in "param: relation"
        elif relation == Relation.BOT:
            self.BOT.add(v)
            v.TOP.add(self)
        elif relation == Relation.IN:
            self.IN = v
            v.CONTAINED.add(self)
        elif relation == Relation.CONTAINED:
            self.CONTAINED.add(v)
            v.IN = self
        elif relation == Relation.ON:
            self.ON.add(v)
            v.UNDER.add(self)
        elif relation == Relation.UNDER:
            self.UNDER.add(v)
            v.ON.add(self)
        else:
            raise UndefinedRelationError()


class Graph:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.vertices: Set[Vertex] = set()  # all unique vertices in a graph
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.relation_matrix_horizontal: Dict[Vertex, Dict[Vertex, Relation]] = dict()  # all horizontal relations in the shape graph

    def add_vertex(self, v: Vertex):
        if v not in self.vertices:
            # Add all relations to other vertices for the new vertex for all relation matrices
            self.relation_matrix_horizontal[v] = {other_v: Relation.UNRELATED for other_v in self.vertices}

            # Add new vertex relation for all other vertices in all relation matrices
            for key in self.relation_matrix_horizontal.keys():
                if key is not v:
                    self.relation_matrix_horizontal[key][v] = Relation.UNRELATED

            # Add new vertex to vertices set
            self.vertices.add(v)

            # Give the vertex a reference to this Graph
            v.graph = self

    def add_relation(self, v_from: Vertex, v_to: Vertex, r: Relation):
        """
        :param v_from:
        :param v_to:
        :param r:

        :raises UndeclaredShapeError

        :return:
        """
        if v_from is None or v_to is None:
            raise UndeclaredShapeError

        if v_from is v_to:
            raise RedundantRelationError

        # TODO: Implement incidence matrices for other relations
        if r not in (Relation.LEFT, Relation.RIGHT):
            # TODO: Change this when working on other types of relations
            return

        # Check if at least one of the shapes is a part of this graph, otherwise throw error
        if v_from not in self.vertices and v_to not in self.vertices:
            raise UndeclaredShapeError

        # Handle shapes from different graphs
        if v_from.graph is not v_to.graph:
            # TODO: Support relations between 2 graphs;
            if v_from.graph is self:
                self.merge_with(v_to.graph)

            elif v_to.graph is self:
                self.merge_with(v_from.graph)
            else:
                # Just to be safe; this case should be handled in the previous checks
                raise UndeclaredShapeError

        # Modify relation in respective matrix; note that you need to modify it for both vertices
        self.relation_matrix_horizontal[v_from][v_to] = r
        self.relation_matrix_horizontal[v_to][v_from] = -r

        # Give vertex info about new neighbour
        # TODO: [Note for the future] This method might not be necessary as querying graph.relation_matrix_XYZ[v1][v2] is quite intuitive BUT every vertex has to be a part of some graph
        v_from.add_neighbour(v_to, r)

    def print_relations(self, v: Vertex) -> None:
        # TODO generate SVG for provided parameters
        if v not in self.vertices:
            print("not in graph")
        else:
            print(f"Found vertex {v.name}")
            for v2, relation in self.relation_matrix_horizontal[v].items():
                vertex_name = v2.name
                vertex_relation = relation
                print(f"{v2.shape}:{vertex_name} {vertex_relation}")

    def merge_with(self, other):
        """
        Merge vertices and relations of the other graph into this one
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

    def find_vertex(self, vertex_name: str) -> Vertex:
        for vertex in self.vertices:
            if str(vertex.name) == str(vertex_name):
                return vertex
        raise UndeclaredShapeError

    def check_horizontal(self) -> Tuple[Vertex, Vertex, Relation, Relation]:
        """
        Check if all relations in horizontal incidence matrix are valid
        :return:
        """
        # TODO: Return a set of changes that need to be applied in order to make this Graph valid
        for v1, relation_map in self.relation_matrix_horizontal.items():
            for v2, relation in relation_map:
                if relation is Relation.LEFT:
                    v1.is_left(v2)
                elif relation is Relation.RIGHT:
                    v1.is_right(v2)
        return
        return (v1, v2, current_relation, desired_relation)

    def center(self):
        """
        Shift all shapes of the graph equally so the bounding box of this graph is centered in its parent
        :return:
        """
        pass
