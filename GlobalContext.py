from graph import Shape, Graph, Vertex
from typing import List
from FunctionParserListener import FunctionParserListener
from Function import Function, FunctionNotExistsError

from antlr4 import *

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

    def call_function(self, global_graph, name: str, args: List):
        f = self._find_function_by_name(name)
        graph = Graph()

        for i, vertex_name in enumerate(f.args_names):
            graph.add_vertex(Vertex(graph, vertex_name, args[i].shape))

        printer = FunctionParserListener(global_context=self, relations_graph=global_graph, func_relations_graph=graph)
        walker = ParseTreeWalker()
        walker.walk(printer, f.body)

        for i in range(len(f.args_names)):
            graph.replace_vertex(vertex_to_replace=graph.find_vertex(f.args_names[i]), new_vertex=args[i])

        for v in graph.vertices:
            if v.unreachable:
                v.name = f"{name}_{v.name}_{v.uid}"

        return graph

    def _find_function_by_name(self, name: str):
        functions_list = list(self.functions_list)
        function_names = [str(f.name) for f in functions_list]
        return functions_list[function_names.index(str(name))]
