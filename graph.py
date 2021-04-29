import uuid
from enum import Enum
from typing import Any, Dict, List, Set


class UndeclaredShapeError(NameError):
    pass


class UndefinedShapeError(ValueError):
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

    def add_neighbour(self, v, relation: Relation):
        """
        Adds a new vertex with given relation to this one's neighbours and this one to the new vertex's with an opposite relation
        :param v: New vertex neighbour of self
        :param relation: Relation of self to neighbour vertex
        :return:
        """
        if relation == Relation.LEFT:
            v.LEFT.add(self)
            self.RIGHT.add(v)
            # v.x = self.x + self.width
            # v.y = self.y
        elif relation == Relation.RIGHT:
            v.RIGHT.add(self)
            self.LEFT.add(v)
            # v.x = self.x - v.width
            # v.y = self.y
        elif relation == Relation.TOP:
            self.TOP.add(v)
            v.BOT.add(self)
            v.x = self.x
            v.y = self.y + v.height
        elif relation == Relation.BOT:
            self.BOT.add(v)
            v.TOP.add(self)
            v.x = self.x
            v.y = self.y - v.height
        elif relation == Relation.IN:
            self.IN = v
            v.CONTAINED.add(self)
            v.x = self.x + self.width / 2
            v.y = self.y + self.height / 2
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
    def __init__(self):
        self.vertices = {}
        self.x = None
        self.y = None
        self.width = 0
        self.height = 0

        self.relation_matrix_horizontal = {}

    def add_vertex(self, v: Vertex):
        if v not in self.vertices.keys():
            self.vertices[v] = []

    def deupdate_vertices(self):
        """
        Should be called after all shapes have been updated to prep them for further updates; this is equivalent to graph node coloring
        :return:
        """

    def center(self):
        """
        Shift all shapes of the graph equally so the bounding box of this graph is centered in its parent
        :return:
        """
        pass

    def add_edge(self, v_from: Vertex, v_to: Vertex, r: Relation):
        # TODO: [NOT IMPORTANT RN] Use incidence matrix to store vertex relations in the Graph
        self.vertices[v_from].append((v_to, r))
        self.vertices[v_to].append((v_from, Relation(-r.value)))

        v_from.add_neighbour(v_to, r)

    def get_relations(self, v: Vertex) -> None:
        # TODO generate SVG for provided parameters
        if v not in self.vertices:
            print("not in graph")
        else:
            print("found vertex...")
            for el in self.vertices[v]:
                vertex_name = el[0].name
                vertex_relation = el[1]
                print(f"{el[0].shape}:{vertex_name} {vertex_relation}")

    def find_vertex(self, vertex_name: str) -> Vertex:
        for v in self.vertices.keys():
            if str(v.name) == str(vertex_name):
                return v
        return None
