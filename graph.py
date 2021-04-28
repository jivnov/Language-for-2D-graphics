import uuid
from enum import Enum
from typing import Any, Dict


class Shape(Enum):
    SQUARE = 1
    CIRCLE = 2
    RECT = 3
    TRIANGLE = 4
    SHAPE = 5


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
    def __init__(self, parent_graph, var_name: str, shape: str, args: Any, content):
        # DONE: Vertex should have a reference to its Graph to track some more "global" properties (e.x. the total
        # width and height of the drawing it is a part of)
        self.name = var_name
        self.shape = None
        self.bb_w = 0.0
        self.drawn = False

        self.content = None  # Should only be not-None if this Vertex is actually a Graph (this allows defining Vertex to Graph relations)

        self.neighbours: Dict[Vertex, Relation] = dict()
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
        if (isinstance(args, list) and len(args) > 0):
            self.bb_w = int(args.pop(0).replace('%', '')) / 100
            if (len(args) > 0):
                self.bb_h = int(args.pop(0).replace('%', '')) / 100
            else:
                self.bb_h = self.bb_h
        if self.shape == Shape.SQUARE or self.shape == Shape.CIRCLE:
            self.bb_h = self.bb_w = min(self.bb_h, self.bb_w)


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

        v_from.neighbours[v_to] = r
        v_to.neighbours[v_from] = -r

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
