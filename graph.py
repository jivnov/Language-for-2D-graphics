import uuid
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import OrderedDict

from svgwrite.container import SVG
from svgwrite.shapes import Rect

import random

import logging


class DisconnectedGraphException(Exception):
    pass


class UndeclaredShapeException(Exception):
    pass


class UndefinedShapeException(Exception):
    pass


class RedundantRelationException(Exception):
    pass


class UndefinedRelationException(Exception):
    pass


class RedefiningExplicitRelationException(Exception):
    pass


class CyclicRelationsException(Exception):
    pass


class UnrelatedShapesException(Exception):
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
            raise UndefinedShapeException(f"Specified shape type is not supported: {shape_name}")


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
    ATLEFT = LEFT * 100  # Meaning: Align the left border of these two shapes
    ATRIGHT = RIGHT * 100
    ATTOP = TOP * 100
    ATBOT = BOT * 100

    def __neg__(self):
        return Relation(-self.value)

    def at(self):
        if self.value % 100 == 0:
            return self
        else:
            return Relation(self.value * 100)

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
        elif relation_name.upper() == "ATLEFT":
            return Relation.ATLEFT
        elif relation_name.upper() == "ATRIGHT":
            return Relation.ATRIGHT
        elif relation_name.upper() == "ATTOP":
            return Relation.ATTOP
        elif relation_name.upper() == "ATBOT":
            return Relation.ATBOT
        else:
            raise UndefinedRelationException(f"Relation named \"{relation_name}\" doesn\'t exist")


class Vertex:
    def __init__(self, shape: str = 'shape', args: Any = None, content = None, parent_graph = None, color: Tuple[int, ...] = None):
        """

        :param parent_graph: Graph that contains this Vertex
        :param shape: Type of this variable
        :param args: Arguments passed to the variable initialization in code
        :param content: Type should be Graph or None; allows for comparison between graphs and shapes
        """
        self.uid = uuid.uuid1() # This will allow editting svg files after calling draw() on parts of the graph; the
        # program can reference any shape by its unique ID or at least try to make a unique variable for each unique ID

        self.updated = False
        self.drawn = False

        self.graph = parent_graph # Graph that this shape is a part of
  
        self.LEFT: OrderedDict[Vertex, Any] = OrderedDict()
        self.RIGHT: OrderedDict[Vertex, Any] = OrderedDict()
        self.TOP: OrderedDict[Vertex, Any] = OrderedDict()
        self.BOT: OrderedDict[Vertex, Any] = OrderedDict()

        self.ATLEFT: OrderedDict[Vertex, Any] = OrderedDict()
        self.ATRIGHT: OrderedDict[Vertex, Any] = OrderedDict()
        self.ATTOP: OrderedDict[Vertex, Any] = OrderedDict()
        self.ATBOT: OrderedDict[Vertex, Any] = OrderedDict()

        self.IN: Vertex = None
        self.CONTAINED: OrderedDict[Vertex, Any] = OrderedDict()
        self.ON: OrderedDict[Vertex, Any] = OrderedDict()
        self.UNDER: OrderedDict[Vertex, Any] = OrderedDict()

        self.unreachable = False

        self.content = content

        if isinstance(shape, Shape):
            self.shape = shape
        else:
            self.shape = Shape.from_string(shape)

        # Determine Bounding Box fractional size through passed arguments
        self.bb_w = 100.0
        self.bb_h = 100.0
        if isinstance(args, list) and len(args) > 0:
            self.bb_w = float(args.pop(0).replace('%', ''))

            # If second dimension was passed use it for height
            if len(args) > 0:
                self.bb_h = float(args.pop(0).replace('%', ''))

        # Adjust Bounding Box fractional size based on shape
        self.adjust_size_based_on_shape()

        width = self.bb_w
        height = self.bb_h

        x = 100.0 - self.bb_w
        y = 100.0 - self.bb_h

        # Use svgwrite features for shape properties
        if isinstance(color, tuple) and len(color) > 0:
            if len(color) == 3:
                self.color = color
            elif len(color) > 3:
                self.color = tuple(list(color)[:3])
            else:
                self.color = tuple(list(color) + [0] * (3 - len(color)))
        else:
            self.color = (0, 0, 0)

        if self.shape == Shape.RECT:
            self.content = Rect(insert=(f"{x}%", f"{y}%"), size=(f"{width}%", f"{height}%"), fill="rgb" + str(self.color))
        elif self.shape == Shape.SHAPE:
            if self.content is None:
                self.content = SVG(insert=(f"{x}%", f"{y}%"), size=(f"{width}%", f"{height}%"))
            else:
                # This is (probably) assignment declaration; constraint the content size but do not create new content
                self.width = self.bb_w
                self.height = self.bb_h
        else:
            raise UndefinedShapeException(f"Specified shape type is not supported: {self.shape}")

    def __str__(self):
        return f"{self.shape} [{self.width_perc}, {self.height_perc}] at: (x={self.x_perc}, y={self.y_perc})"

    @property
    def neighbours(self) -> OrderedDict:
        result = self.LEFT.copy()
        for d in (self.RIGHT, self.TOP, self.BOT, self.ATLEFT, self.ATRIGHT, self.ATTOP, self.ATBOT):
            result.update(d)
        return result

    def draw(self, canvas):
        """
        Pass drawing responsibility to parent graph;
        :param canvas:
        :return:
        """
        self.graph.draw(canvas, caller_vertex=self)

    def adjust_size_based_on_shape(self):
        # Adjust Bounding Box fractional size based on shape
        if self.shape == Shape.SQUARE or self.shape == Shape.CIRCLE:
            self.bb_h = self.bb_w = min(self.bb_h, self.bb_w)

    # Getters and setters for SVG element position - you should only be passing and receiving floats from these parameters (instead of strings like "10.5%")
    @property
    def x_perc(self):
        """
        :return: Element's 'x' coordinate in a string formatted like: "10.5%" "25%" etc.
        """
        return self.content['x']

    @property
    def x(self):
        return float(self.content['x'].replace("%", ""))

    @x.setter
    def x(self, val):
        self.content['x'] = f"{val}%"

    @property
    def y_perc(self):
        return self.content['y']

    @property
    def y(self):
        return float(self.content['y'].replace("%", ""))

    @y.setter
    def y(self, val):
        self.content['y'] = f"{val}%"

    @property
    def width_perc(self):
        return self.content['width']

    @property
    def width(self):
        return float(self.content['width'].replace("%", ""))

    @width.setter
    def width(self, val):
        self.content['width'] = f"{val}%"

    @property
    def height_perc(self):
        return self.content['height']

    @property
    def height(self):
        return float(self.content['height'].replace("%", ""))

    @height.setter
    def height(self, val):
        self.content['height'] = f"{val}%"

    def center_horizontally_if_legal(self):
        if len(self.LEFT) == 0 and len(self.RIGHT) == 0 and len(self.ATLEFT) == 0 and len(self.ATRIGHT) == 0:
            self.x = (100 - self.width) / 2

    def center_vertically_if_legal(self):
        if len(self.TOP) == 0 and len(self.BOT) == 0 and len(self.ATTOP) == 0 and len(self.ATBOT) == 0:
            self.y = (100 - self.height) / 2

    def center_if_legal(self):
        self.center_horizontally_if_legal()
        self.center_vertically_if_legal()

    # HORIZONTAL RELATIONS
    def is_left(self, other) -> bool:
        return self.x <= other.x - self.width

    def is_right(self, other) -> bool:
        return self.x >= other.x + other.width

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

    # HORIZONTAL "ALIGN/AT" RELATIONS
    def is_atleft(self, other) -> bool:
        return self.x == other.x

    def is_atright(self, other) -> bool:
        return self.x + self.width == other.x + other.width

    def to_atleft_of(self, other):
        self.x = other.x

    def to_atright_of(self, other):
        self.x = other.x + other.width - self.width

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
        # Basic 2D relations are antagonistic
        if relation == Relation.LEFT:
            v.LEFT[self] = None
            self.RIGHT[v] = None
        elif relation == Relation.RIGHT:
            v.RIGHT[self] = None
            self.LEFT[v] = None
        elif relation == Relation.TOP:
            v.TOP[self] = None
            self.BOT[v] = None
        elif relation == Relation.BOT:
            v.BOT[self] = None
            self.TOP[v] = None

        # AT-xyz relations are mutual (bidirectional)
        elif relation == Relation.ATLEFT:
            v.ATLEFT[self] = None
            self.ATLEFT[v] = None
        elif relation == Relation.ATRIGHT:
            v.ATRIGHT[self] = None
            self.ATRIGHT[v] = None
        elif relation == Relation.ATTOP:
            v.ATTOP[self] = None
            self.ATTOP[v] = None
        elif relation == Relation.ATBOT:
            v.ATBOT[self] = None
            self.ATBOT[v] = None

        # TODO: Z-axis relations
        elif relation == Relation.IN:
            v.IN = self
            self.CONTAINED[v] = None
        elif relation == Relation.CONTAINED:
            v.CONTAINED[self] = None
            self.IN = v
        elif relation == Relation.ON:
            v.ON[self] = None
            self.UNDER[v] = None
        elif relation == Relation.UNDER:
            v.UNDER[self] = None
            self.ON[v] = None
        else:
            raise UndefinedRelationException(str(relation))

    def get_neighbours_by_relation(self, r: Relation):
        if r == Relation.UNRELATED:
            raise UnrelatedShapesException("You tried retrieving all shapes UNRELATED to this one which is an illegal operation")
        elif r == Relation.LEFT:
            return self.LEFT
        elif r == Relation.RIGHT:
            return self.RIGHT
        elif r == Relation.TOP:
            return self.TOP
        elif r == Relation.BOT:
            return self.BOT
        elif r == Relation.ATLEFT:
            return self.ATLEFT
        elif r == Relation.ATRIGHT:
            return self.ATRIGHT
        elif r == Relation.ATTOP:
            return self.ATTOP
        elif r == Relation.ATBOT:
            return self.ATBOT
        else:
            raise UndefinedRelationException(f"Relation denoted by {r} is not defined")

    def remove_neighbour(self, neighbour):
        """
        WARNING: This function is deprecated (for the time being); don't use it
        :param neighbour:
        :return:
        """
        if neighbour in self.LEFT:
            self.LEFT.pop(neighbour)
            neighbour.RIGHT.pop(self)
        elif neighbour in self.RIGHT:
            self.RIGHT.pop(neighbour)
            neighbour.LEFT.pop(self)
        elif neighbour in self.TOP:
            self.TOP.pop(neighbour)
            neighbour.BOT.pop(self)
        elif neighbour in self.BOT:
            self.BOT.pop(neighbour)
            neighbour.TOP.pop(self)
        elif neighbour == self.IN:
            self.IN = None
            neighbour.CONTAINED.pop(self)
        elif neighbour in self.CONTAINED:
            self.CONTAINED.pop(neighbour)
            neighbour.IN = None
        elif neighbour in self.ON:
            self.ON.pop(neighbour)
            neighbour.UNDER.pop(self)
        elif neighbour in self.UNDER:
            self.UNDER.pop(neighbour)
            neighbour.ON.pop(self)


class Graph:
    def __init__(self, x=0, y=0, width=100, height=100, viewport_size=None):
        self.vertices: OrderedDict[Vertex, Any] = OrderedDict()  # all unique vertices in a graph

        # Position of the top-left corner of this graph's bounding box
        self.x = x
        self.y = y

        # Width and height of this graph's bounding box (width in the widest point and height in the highest point)
        self.width = width
        self.height = height

        # SVG elem that contains this graph's elements
        self.svg_elem = SVG(insert=(f"{x}%", f"{y}%"), size=(f"{width}%", f"{height}%"))

        self.relation_matrix_horizontal: Dict[
            Vertex, Dict[Vertex, Relation]] = OrderedDict()  # all horizontal relations in the shape graph

        self.relation_matrix_vertical: Dict[
            Vertex, Dict[Vertex, Relation]] = OrderedDict()  # all vertical relations in the shape graph

    @property
    def content_width(self):
        return 0 if len(self.vertices) == 0 else max(v.x + v.width for v in self.vertices.keys()) - min(v.x for v in self.vertices.keys())

    @property
    def content_height(self):
        return 0 if len(self.vertices) == 0 else max(v.y + v.height for v in self.vertices.keys()) - min(v.y for v in self.vertices.keys())

    @property
    def content_x(self):
        return 0 if len(self.vertices) == 0 else min(v.x for v in self.vertices.keys())

    @property
    def content_y(self):
        return 0 if len(self.vertices) == 0 else min(v.y for v in self.vertices.keys())

    def add_vertex(self, v: Vertex):
        if v not in self.vertices.keys():
            # Add relations between this new vertex and other old vertices
            self.relation_matrix_horizontal[v] = {other_v: Relation.UNRELATED for other_v in self.vertices.keys()}
            self.relation_matrix_vertical[v] = {other_v: Relation.UNRELATED for other_v in self.vertices.keys()}

            # Add relations between other old vertices and this new vertex
            for key in self.relation_matrix_horizontal.keys():
                if key is not v:
                    self.relation_matrix_horizontal[key][v] = Relation.UNRELATED

            for key in self.relation_matrix_vertical.keys():
                if key is not v:
                    self.relation_matrix_vertical[key][v] = Relation.UNRELATED

            # Add new vertex to vertices set
            self.vertices[v] = None

            # Give the vertex a reference to this Graph
            v.graph = self

    def add_relation(self, v_from: Vertex, v_to: Vertex, r: Relation):
        # TODO: A |top B  - A jest powyżej od B, przylega do jego górnej krawędzi
        # TODO: rect A [10%, EXPAND_TO_FILL]  - EXPAND_TO_FILL means 100% - the rest of the shapes
        """
        :param v_from:
        :param v_to:
        :param r:

        :raises UndeclaredShapeException
        :raises RedundantRelationException
        :raises CyclicRelationsException

        :return:
        """
        # Both shapes should have already been added to this graph before defining relations between them
        if v_from is None or v_to is None or v_from not in self.vertices.keys() or v_to not in self.vertices.keys():
            logging.info(f"{v_from=} {v_to=}")
            raise UndeclaredShapeException(f"{v_from=} {v_to=}")

        if v_from is v_to:
            raise RedundantRelationException

        # Modify relation in respective matrix; note that you need to modify it for both vertices
        if r in (Relation.LEFT, Relation.RIGHT, Relation.ATLEFT, Relation.ATRIGHT):
            self.relation_matrix_horizontal[v_from][v_to] = r

            if r == Relation.LEFT:
                # Add this relation to all ATRIGHT neighbours of v_from and opposite to all ATLEFT of v_to
                for atr in v_from.ATRIGHT.keys():
                    self.relation_matrix_horizontal[atr][v_to] = r
                    self.relation_matrix_horizontal[v_to][atr] = -r
                    atr.add_neighbour(v_to, r)

                for atl in v_to.ATLEFT.keys():
                    self.relation_matrix_horizontal[atl][v_from] = -r
                    self.relation_matrix_horizontal[v_from][atl] = r
                    atl.add_neighbour(v_from, -r)

                for atl in v_to.ATLEFT.keys():
                    for atr, _ in v_from.ATRIGHT.keys():
                        self.relation_matrix_horizontal[atr][atl] = r
                        self.relation_matrix_horizontal[atl][atr] = -r
                        atr.add_neighbour(atl, r)

            elif r == Relation.RIGHT:
                # Add this relation to all ATLEFT neighbours of v_from and opposite to all ATRIGHT of v_to
                for atl in v_from.ATLEFT.keys():
                    self.relation_matrix_horizontal[atl][v_to] = r
                    self.relation_matrix_horizontal[v_to][atl] = -r
                    atl.add_neighbour(v_to, r)

                for atr in v_to.ATRIGHT.keys():
                    self.relation_matrix_horizontal[atr][v_from] = -r
                    self.relation_matrix_horizontal[v_from][atr] = r
                    atr.add_neighbour(v_from, -r)

                for atr in v_to.ATRIGHT.keys():
                    for atl, _ in v_from.ATLEFT.keys():
                        self.relation_matrix_horizontal[atr][atl] = -r
                        self.relation_matrix_horizontal[atl][atr] = r
                        atr.add_neighbour(atl, -r)

            elif r == Relation.ATLEFT:
                # Snapshot pre-changes sets of neighbours so we don't mutate structures that we work on
                atla = v_from.ATLEFT.copy()
                atlb = v_to.ATLEFT.copy()
                la = v_from.LEFT.copy()
                lb = v_to.LEFT.copy()
                for atl in atla.keys():
                    self.relation_matrix_horizontal[atl][v_to] = r
                    self.relation_matrix_horizontal[v_to][atl] = r
                    atl.add_neighbour(v_to, r)

                for atl in atlb.keys():
                    self.relation_matrix_horizontal[atl][v_from] = r
                    self.relation_matrix_horizontal[v_from][atl] = r
                    atl.add_neighbour(v_from, r)

                for aatl in atla.keys():
                    for batl in atlb.keys():
                        self.relation_matrix_horizontal[aatl][batl] = r
                        self.relation_matrix_horizontal[batl][aatl] = r
                        aatl.add_neighbour(batl, r)

                for l in la.keys():
                    self.relation_matrix_horizontal[l][v_to] = Relation.LEFT
                    self.relation_matrix_horizontal[v_to][l] = Relation.RIGHT
                    l.add_neighbour(v_to, Relation.LEFT)

                for l in lb.keys():
                    self.relation_matrix_horizontal[l][v_from] = Relation.LEFT
                    self.relation_matrix_horizontal[v_from][l] = Relation.RIGHT
                    l.add_neighbour(v_from, Relation.LEFT)

                for al in la.keys():
                    for bl in lb.keys():
                        self.relation_matrix_horizontal[al][bl] = (-r).at()
                        self.relation_matrix_horizontal[bl][al] = (-r).at()
                        al.add_neighbour(bl, (-r).at())


            # Inline if is crucial - AT-xyz relations are bidirectional:
            #       "A ATLEFT B" is the same as "B ATLEFT A"
            self.relation_matrix_horizontal[v_to][v_from] = r if r in (Relation.ATLEFT, Relation.ATRIGHT) else -r

            if self._invalid_horizontal_relations():
                raise CyclicRelationsException(f"Relation {r=} between {v_from.uid=} and {v_to.uid=} causes a cycle in horizontal relations")
        elif r in (Relation.TOP, Relation.BOT, Relation.ATTOP, Relation.ATBOT):
            self.relation_matrix_vertical[v_from][v_to] = r

            # Inline if is crucial - AT-xyz relations are bidirectional:
            #       "A ATTOP B" is the same as "B ATTOP A"
            self.relation_matrix_vertical[v_to][v_from] = r if r in (Relation.ATTOP, Relation.ATBOT) else -r

            if self._invalid_vertical_relations():
                raise CyclicRelationsException(f"Relation {r=} between {v_from.uid=} and {v_to.uid=} causes a cycle in vertical relations")
            # TODO: Implement incidence matrices for other relations
        else:
            return

        # TODO: [Note for the future] This method might not be necessary as querying graph.relation_matrix_XYZ[v1][v2] is quite intuitive BUT every vertex has to be a part of some graph
        # Give vertex info about new neighbour
        v_from.add_neighbour(v_to, r)

    def _cross_at_relations(self, v_from: Vertex, v_to: Vertex, r: Relation):
        """
        When "r" is ATx: add v_from and its ATx neighbours to v_to and all its ATx neighbours; and vice versa
        :param v_from:
        :param v_to:
        :param r:
        :return:
        """
        v_from_group = v_from.get_neighbours_by_relation(r.at()).copy()
        v_from_group[v_from] = None

        v_to_group = v_to.get_neighbours_by_relation(r.at()).copy()
        v_to_group[v_to] = None

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
        visited = {v: False for v in self.vertices.keys()}
        rec_stack = {v: False for v in self.vertices.keys()}
        for node in self.vertices.keys():
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
        visited = {v: False for v in self.vertices.keys()}
        rec_stack = {v: False for v in self.vertices.keys()}
        for node in self.vertices.keys():
            if not visited[node]:
                if self._is_cyclic_vertical_util(node, visited, rec_stack):
                    return True
        return False

    def print_relations(self, v: Vertex) -> None:
        # TODO generate SVG for provided parameters
        if v not in self.vertices.keys():
            logging.debug("Not in graph")
        else:
            logging.info(f"Found vertex {v.shape}:{v.uid}")
            for v2, relation in self.relation_matrix_horizontal[v].items():
                logging.info(f"{v2.shape}:{v2.uid}")

    def merge_with(self, other, r: Relation = Relation.UNRELATED):
        # TODO: Parameter "r" taken into account (as stated in docstring)
        """
        Merge vertices and relations of the other graph into this one
        :param r: [optional] Make all self.vertices satisfy relation "r" with all other.vertices
        :param other: Other Graph
        :return:
        """
        # Add all new vertices
        for vertex in other.vertices.keys():
            self.add_vertex(vertex)

        # Add all new relations
        for v1, relation_dict in other.relation_matrix_horizontal.items():
            for v2, relation in relation_dict.items():
                self.add_relation(v1, v2, relation)

        # Clear vertex data from other Graph (they are now a part of this one)
        other.vertices.clear()
        other.relation_matrix_horizontal.clear()

    def find_vertex(self, vertex_id: str) -> Vertex:
        for vertex in self.vertices.keys():
            if str(vertex.uid) == str(vertex_id):
                return vertex
        raise UndeclaredShapeException(vertex_id)

    def remove_vertex(self, v: Vertex):
        if v in self.vertices:
            # Add relations between this new vertex and other old vertices
            self.relation_matrix_horizontal.pop(v)
            self.relation_matrix_vertical.pop(v)

            # Add relations between other old vertices and this new vertex
            for key in self.relation_matrix_horizontal.keys():
                if key is not v:
                    del self.relation_matrix_horizontal[key][v]

            for key in self.relation_matrix_vertical.keys():
                if key is not v:
                    del self.relation_matrix_vertical[key][v]

            # Remove from vertices list
            self.vertices.pop(v)

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
                elif relation is Relation.ATLEFT and not v1.is_atleft(v2):
                    v2.to_atleft_of(v1)
                elif relation is Relation.ATRIGHT and not v1.is_atright(v2):
                    v2.to_atright_of(v1)

                # # UPDATE GRAPH BOUNDING BOX VALUES
                # self._update_horizontal()

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
                #
                # # UPDATE GRAPH BOUNDING BOX VALUES
                # self._update_vertical()
                # self._update_horizontal()

    def _update_x(self):
        self.x = min(v.x for v in self.vertices.keys())

    def _update_y(self):
        self.y = min(v.y for v in self.vertices.keys())

    def _update_horizontal(self):
        self._update_x()
        self.width = max(v.x + v.width for v in self.vertices.keys()) - self.x

    def _update_vertical(self):
        self._update_y()
        self.height = max(v.y + v.height for v in self.vertices.keys()) - self.y

    def update_position_and_size(self):
        """
        Recalculate graph's X, Y, width and height based on its vertices
        :return:
        """
        self._update_horizontal()
        self._update_vertical()

    def content_move_horizontal(self, dist: int, parent_width=1):
        """
        Shift all shapes by the given distance in the X axis.

        :param dist: Positive integer to move right, negative to move left
        :return:
        """
        for v in self.vertices.keys():
            v.x += dist
        self.x += dist

    def content_move_vertical(self, dist: int):
        """
        Shift all shapes by the given distance in the Y axis.

        :param dist: Positive integer to move down, negative to move up
        :return:
        """
        for v in self.vertices.keys():
            v.y += dist
        self.y += dist

    def center(self, pw=100, ph=100, px: int = 0, py: int = 0):
        """
        Center this graph in given parent dimensions
        :param pw: Parent width
        :param ph: Parent height
        :param px: Parent X; 0 for viewport
        :param py: Parent Y; 0 for viewport
        :return:
        """
        target_x = (100 - self.width) / 2
        target_y = (100 - self.height) / 2

        self.x = target_x
        self.y = target_y

    def content_center_in_self(self):
        target_x = (100 - self.content_width) / 2
        target_y = (100 - self.content_height) / 2
        if self.content_x != target_x:
            self.content_move_to(target_x, self.content_y)
        if self.content_y != target_y:
            self.content_move_to(self.content_x, target_y)

    def content_move_to(self, x, y):
        self.content_move_horizontal(x - self.content_x)
        self.content_move_vertical(y - self.content_y)
            
    def replace_vertex(self, vertex_to_replace: Vertex, new_vertex: Vertex):

        self._copy_contents(vertex_to_replace, new_vertex)

        self.add_vertex(new_vertex)

        for v_from in self.relation_matrix_horizontal.keys():
            if v_from != new_vertex and v_from in self.vertices.keys():
                for v_to in list(self.relation_matrix_horizontal[v_from].keys()):
                    if v_to == vertex_to_replace:
                        rel = self.relation_matrix_horizontal[v_from][v_to]
                        self.add_relation(v_from=v_from, v_to=new_vertex, r=rel)
                        if rel != Relation.UNRELATED:
                            v_from.add_neighbour(new_vertex, rel)
                            v_from.remove_neighbour(vertex_to_replace)
                        self.relation_matrix_horizontal[v_from].pop(vertex_to_replace)

        for v_from in self.relation_matrix_vertical.keys():
            if v_from != new_vertex and v_from in self.vertices.keys():
                for v_to in list(self.relation_matrix_vertical[v_from].keys()):
                    if v_to == vertex_to_replace:
                        rel = self.relation_matrix_vertical[v_from][v_to]
                        self.add_relation(v_from = v_from, v_to = new_vertex, r = rel)
                        if rel != Relation.UNRELATED:
                            v_from.add_neighbour(new_vertex, rel)
                            v_from.remove_neighbour(vertex_to_replace)
                        self.relation_matrix_vertical[v_from].pop(vertex_to_replace)

        # Remove from graph in general
        self.vertices.pop(vertex_to_replace)

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

    @property
    def disconnected(self):
        if len(self.vertices) == 0:
            raise StopIteration("No vertices in this graph")
        visited = OrderedDict()
        tbv = OrderedDict()  # To Be Visited

        any_v, _ = self.vertices.copy().popitem()
        tbv[any_v] = None  # Take any element of the graph
        while len(tbv) > 0:
            curr, _ = tbv.popitem()
            visited[curr] = None
            for n in curr.neighbours:
                if n not in visited.keys() and n not in tbv.keys():
                    tbv[n] = None
        return len(visited.keys()) != len(self.vertices.keys())

    def _draw_vertex(self, v: Vertex, from_caller=False):
        # TODO: Draw all neighbours and neighbours' neighbours etc.
        """
        Basic algo:
        1. Go "up" (check the IN reference) until you reach the root of the graph
        NOTE: When adding a neighbour A to a Vertex B CONTAINED in some shape X, you should add "A IN X" relation automatically as well
        2. Draw root shape parent_graphX
        3. Call algo for each of X's neighbours until there are no neighbours to draw
        :param v:
        :param from_caller:
        :return:
        """
        if v.drawn:
            return

        self.svg_elem.add(v.content)
        v.drawn = True

        if from_caller:
            for n in v.neighbours:
                self._draw_vertex(n, from_caller=True)

    def export_as_vertex(self) -> Vertex:
        if self.disconnected:
            raise DisconnectedGraphException(f"Some shapes have no clear relations to each other. Aborting drawing\n{self.relation_matrix_horizontal=}\n{self.relation_matrix_vertical=}")

        self.sort_horizontal()
        self.sort_vertical()
        self.content_center_in_self()

        for v in self.vertices.keys():
            v.center_if_legal()

        for v in self.vertices.keys():
            self.svg_elem.add(v.content)
        return Vertex(content=self.svg_elem.copy())

    def draw(self, canvas, caller_vertex: Vertex = None):
        """
        :param canvas:
        :param caller_vertex: In 2Dim you can draw a graph itself via Graph.draw(), or Graph.draw() can be called by its child vertex; in latter case only the vertices connected to caller or its neighbours or their neighbours etc. are drawn
        :return:
        """
        if self.disconnected:
            raise DisconnectedGraphException(f"Some shapes have no clear relations to each other. Aborting drawing\n{self.relation_matrix_horizontal=}\n{self.relation_matrix_vertical=}")

        self.sort_horizontal()
        self.sort_vertical()
        self.content_center_in_self()

        for v in self.vertices.keys():
            v.center_if_legal()

        if caller_vertex is not None:
            # Only draw vertices connected to the caller of Graph.draw()
            self._draw_vertex(caller_vertex, from_caller=True)
        else:
            # Draw all vertices (might produce a disjointed graph)
            for v in self.vertices.keys():
                self._draw_vertex(v, from_caller=False)
        canvas.add(self.svg_elem)
        canvas.save()
