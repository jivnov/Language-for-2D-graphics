from typing import List
from graph import Shape, Graph, Vertex
from FunctionParserListener import FunctionParserListener


from antlr4 import *


class FunctionSignatureError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name

    def __str__(self):
        return f"Function {self.function_name}() signature does not match the declaration."


class FunctionNotExistsError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name

    def __str__(self):
        return f"Function {self.function_name}() is not defined."


class Function:
    def __init__(self, name: str, args: List, args_names: List = None, body = None): #expecting to receive list of pairs [Shape, Int] where Int is a counter for provided shape
        self.name = name
        self.args = []
        self.args_names = args_names

        for shape, count in args:
            if shape == "rect":
                shape = Shape.RECT
            elif shape == "square":
                shape = Shape.SQUARE
            elif shape == "circle":
                shape = Shape.CIRCLE
            elif shape == "triangle":
                shape = Shape.TRIANGLE
            elif shape == "shape":
                shape = Shape.SHAPE
            self.args.append((shape, count))

        self.body = body
    

class GlobalContext:
    def __init__(self):
        self.functions_list = set()

    def add_function(self, foo: Function):
        self.functions_list.add(foo)

    def check_call(self, foo: Function) -> bool:
        f = self._find_function_by_name(foo.name)

        if not f:
            raise FunctionNotExistsError(foo.name)

        if len(foo.args) != len(f.args):
            return False

        for i in range(len(foo.args)):
            if foo.args[i] != f.args[i]:
                return False
        return True

    def call_function(self, parser, name: str, args: List):
        f = self._find_function_by_name(name)
        graph = Graph()

        for i, vertex_name in enumerate(f.args_names):
            graph.add_vertex(Vertex(graph, vertex_name, args[i].shape))

        printer = FunctionParserListener(global_context = self, relations_graph = graph)
        walker = ParseTreeWalker()
        walker.walk(printer, f.body)

        for i in range(len(f.args_names)):
            graph.replace_vertex(vertex_to_replace = graph.find_vertex(f.args_names[i]), new_vertex = args[i])
        
        for v in list(graph.vertices):
            if v.name not in [_.name for _ in list(args)]:
                v.name = f"{name}_{v.name}"
                v.unreachable = True

        return graph

    
    def _find_function_by_name(self, name: str):
        functions_list = list(self.functions_list)
        function_names = [str(f.name) for f in functions_list]
        return functions_list[function_names.index(str(name))]
        


        
