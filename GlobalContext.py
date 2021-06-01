import uuid
from typing import List
from graph import Shape, Graph, Vertex
from FunctionParserListener import FunctionParserListener
from Function import Function, FunctionNotExistsError
import VariablesTree

from antlr4 import *

class GlobalContext:
    def __init__(self):
        self.functions_list = set()
        self.variables = VariablesTree.VariablesTree()

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

    def call_function(self, global_graph, name: str, args: List, parent_id=None):
        f = self._find_function_by_name(name)
        call_id = uuid.uuid1()
        self.variables.add_scope_subtree(tag=f.name.getText(), name=call_id, scope=parent_id)
        graph = Graph()

        for i, vertex_name in enumerate(f.args_names):
            v = Vertex(args[i].shape, parent_graph=graph)
            v.width = args[i].width
            v.height = args[i].height
            graph.add_vertex(v)
            self.variables.add_variable(tag=vertex_name.getText(), name=v.uid, content=v, scope=call_id)

        printer = FunctionParserListener(global_context=self, func_relations_graph=graph, call_id=call_id)
        walker = ParseTreeWalker()
        walker.walk(printer, f.body)

        # Some randomish vertex name
        return graph.export_as_vertex()

    def _find_function_by_name(self, name: str):
        functions_list = list(self.functions_list)
        function_names = [str(f.name) for f in functions_list]
        return functions_list[function_names.index(str(name))]
