import sys
import drawing
import graph
#from GlobalContext import GlobalContext, Function

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener

class FunctionParserListener(TwoDimParserListener):

    def __init__(self, global_context, relations_graph):
        super().__init__()
        self.relations_graph = relations_graph
        self.context = global_context

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, var_name in enumerate(ctx.IDENTIFIER()):
            # TODO
            # At the moment assuming SIZE is the only argument
            self.relations_graph.add_vertex(
                graph.Vertex(parent_graph=self.relations_graph, var_name=var_name, shape=ctx.typeName().getText(),
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            )

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ctx.primaryExpr(0).operand().operandName().getText()
        var_name2 = ctx.primaryExpr(1).operand().operandName().getText()
        try:
            op1 = self.relations_graph.find_vertex(var_name1)
            op2 = self.relations_graph.find_vertex(var_name2)
            self.relations_graph.add_relation(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))
        except UndeclaredShapeError:
            print(f"Undeclared shape {var_name1} or {var_name2}")

    def enterFunctionCall(self, ctx: TwoDimParser.FunctionCallContext):
        #checking function call for correctness
        args_for_check = []
        args_for_call = []
        argument_ids = [opName.IDENTIFIER() for opName in ctx.operandName()]
        for id in argument_ids:
            v = self.relations_graph.find_vertex(id)
            shape = v.shape

            if len(args_for_check) == 0 or args_for_check[len(args_for_check)-1][0] != shape:
                args_for_check.append([shape, 1])
            else:
                args_for_check[len(args_for_check) - 1][1] += 1

            args_for_call.append(v)

        function_called = Function(name = ctx.IDENTIFIER(), args = args_for_check)

        if not self.context.check_call(function_called):
            raise FunctionSignatureError(function_called.name)

        self.context.call_function(name = ctx.IDENTIFIER(), args = args_for_call)
        

