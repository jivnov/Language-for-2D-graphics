from enum import Enum

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
    def __init__(self, var_name: str,  shape: Shape,  args):
        self.name = var_name
        self.shape = shape

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v: Vertex):
        if (v not in self.vertices.keys()):
            self.vertices[v] = []

    def add_edge(self, v_from: Vertex, v_to: Vertex, r: Relation):
        if (v_from not in self.vertices.keys()):
            add_vertex(v_from)
        if (v_to not in self.vertices.keys()):
            add_vertex(v_to)
        self.vertices[v_from].append([v_to, r])

    def get_relations(self, v: Vertex):
        #TODO generate SVG for provided parameters
        if v not in self.vertices:
            print("not in graph")
        else:
            for el in self.vertices[v]:
                vertex_name = el[0].name
                vertex_relation = el[1]
                print(f"{el[0].shape}:{vertex_name} {vertex_relation}")
