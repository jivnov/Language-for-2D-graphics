from enum import Enum
from typing import Any


class Shape(Enum):
    SQUARE = 1
    CIRCLE = 2
    RECT = 3
    TRIANGLE = 4
    SHAPE = 5


class Relation(Enum):
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOT = 4
    IN = 5
    ON = 6
    UNDER = 7


class Vertex:
    def __init__(self, var_name: str, shape: str, args: Any):
        self.name = var_name
        self.shape = None
        self.bb_w = 0.0
        if shape == "rect":
            self.shape = Shape.RECT
        if shape == "square":
            self.shape = Shape.SQUARE
        if shape == "circle":
            self.shape = Shape.CIRCLE
        if shape == "triangle":
            self.shape = Shape.TRIANGLE
        if shape == "shape":
            self.shape == Shape.SHAPE
        if (isinstance(args, list) and len(args)>0):
            self.bb_w = int(args.pop(0).replace('%', ''))/100
            if (len(args) > 0):
                self.bb_h = int(args.pop(0).replace('%', ''))/100
            else:
                self.bb_h = self.bb_h
        if self.shape == Shape.SQUARE or self.shape == Shape.CIRCLE:
            self.bb_h = self.bb_w = min(self.bb_h, self.bb_w)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v: Vertex):
        if v not in self.vertices.keys():
            self.vertices[v] = []

    def add_edge(self, v_from: Vertex, v_to: Vertex, r: Relation):
        if v_from not in self.vertices.keys():
            self.add_vertex(v_from)
        if v_to not in self.vertices.keys():
            self.add_vertex(v_to)
        self.vertices[v_from].append([v_to, r])

    def get_relations(self, v: Vertex):
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
