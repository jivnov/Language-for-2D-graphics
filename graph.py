import uuid
from enum import Enum
from typing import Any, Dict, List, Set

import graph


class Shape(Enum):
    SQUARE = 1
    CIRCLE = 2
    RECT = 3
    TRIANGLE = 4
    SHAPE = 5


class UndefinedRelationError(ValueError):
    pass


class Relation(Enum):
    LEFT = 1
    RIGHT = -1
    TOP = 2
    BOT = -2
    IN = 3
    CONTAINED = -3  # Opposite of IN
    ON = 4
    UNDER = -4


class Vertex:
    def __init__(self, parent_graph, var_name: str, shape: str, args: Any, content: graph.Graph):
        # DONE: Vertex should have a reference to its Graph to track some more "global" properties (e.x. the total
        # width and height of the drawing it is a part of)
        self.name = var_name
        self.shape = None
        self.bb_w = 0.0
        self.drawn = False

        self.x = None
        self.y = None
        self.width = None
        self.height = None

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

        if shape == "rect":
            self.shape = Shape.RECT
        if shape == "square":
            self.shape = Shape.SQUARE
        if shape == "circle":
            self.shape = Shape.CIRCLE
        if shape == "triangle":
            self.shape = Shape.TRIANGLE
        if shape == "shape":
            self.shape = Shape.SHAPE

        # Determine Bounding Box fractional size through passed arguments
        if isinstance(args, list) and len(args) > 0:
            self.bb_w = int(args.pop(0).replace('%', '')) / 100
            if len(args) > 0:
                self.bb_h = int(args.pop(0).replace('%', '')) / 100
            else:
                self.bb_h = self.bb_w

        # Adjust Bounding Box fractional size based on shape
        self.adjust_size_based_on_shape()

    def adjust_size_based_on_shape(self):
        # Adjust Bounding Box fractional size based on shape
        if self.shape == Shape.SQUARE or self.shape == Shape.CIRCLE:
            self.bb_h = self.bb_w = min(self.bb_h, self.bb_w)

    def add_neighbour(self, v: graph.Vertex, relation: Relation):
        """
        Adds a new vertex with given relation to this one's neighbours and this one to the new vertex's with an opposite relation
        :param v: New vertex neighbour of self
        :param relation: Relation of self to neighbour vertex
        :return:
        """
        if relation == Relation.LEFT:
            self.LEFT.add(v)
            v.RIGHT.add(self)
        elif relation == Relation.RIGHT:
            self.RIGHT.add(v)
            v.LEFT.add(self)
        elif relation == Relation.TOP:
            self.TOP.add(v)
            v.BOT.add(self)
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
    def __init__(self):
        self.vertices = {}
        self.width = 0
        self.height = 0

    def add_vertex(self, v: Vertex):
        if v not in self.vertices.keys():
            self.vertices[v] = []

    def add_edge(self, v_from: Vertex, v_to: Vertex, r: Relation):
        # TODO: [NOT IMPORTANT RN] Use incidence matrix to store vertex relations in the Graph
        self.add_vertex(v_from)
        self.add_vertex(v_to)

        self.vertices[v_from].append((v_to, r))
        self.vertices[v_to].append((v_from, -r))

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
