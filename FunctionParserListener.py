import uuid
from copy import copy

import graph

from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener
from Function import Function, FunctionSignatureError

class FunctionParserListener(TwoDimParserListener):

    def __init__(self, global_context, func_relations_graph, call_id=None):
        super().__init__()
        self.func_relations_graph = func_relations_graph
        self.context = global_context
        self.function_call_id = call_id

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, var_name in enumerate(ctx.IDENTIFIER()):
            # TODO
            # At the moment assuming SIZE is the only argument
            v = graph.Vertex(parent_graph=self.func_relations_graph, shape=ctx.typeName().getText(),
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            self.func_relations_graph.add_vertex(v)
            self.context.variables.add_variable(tag=var_name.getText(), name=v.uid, content=v, scope=self.function_call_id)

    def enterAssignment(self, ctx:TwoDimParser.AssignmentContext):
        data = None
        if ctx.expression().functionCall() is not None:
            data = self.enterFunctionCall(ctx.expression().functionCall())
        elif ctx.expression().primaryExpr() is not None:
            data = self.context.variables.find_var_by_tag(
                tag=ctx.expression().primaryExpr()[0].operand().operandName().IDENTIFIER().getText(),
                scope=self.function_call_id
            ).data
        self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText(), self.function_call_id).data = data
        self.func_relations_graph.remove_vertex(
            self.func_relations_graph.find_vertex(self.context.variables.find_var_by_tag(
                tag=ctx.IDENTIFIER().getText(), scope=self.function_call_id).data.uid))
        self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText(), scope=self.function_call_id).data = graph.Vertex(shape=data.shape)
        self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText(), scope=self.function_call_id).data.width = data.width
        self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText(), scope=self.function_call_id).data.height = data.height
        self.func_relations_graph.add_vertex(
            self.context.variables.find_var_by_tag(tag=ctx.IDENTIFIER().getText(), scope=self.function_call_id).data)

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ctx.primaryExpr(0).operand().operandName().getText()
        var_name2 = ctx.primaryExpr(1).operand().operandName().getText()
        try:
            op1 = self.context.variables.find_var_by_tag(tag=var_name1, scope=self.function_call_id).data
            op2 = self.context.variables.find_var_by_tag(tag=var_name2, scope=self.function_call_id).data
            self.func_relations_graph\
                .add_relation(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp().getText())) #!!!!!!!!!!!!!!

        except graph.UndeclaredShapeError:
            print(f"Undeclared shape {var_name1} or {var_name2}")

    def enterFunctionCall(self, ctx: TwoDimParser.FunctionCallContext):
        # checking function call for correctness

        args_for_check = []
        args_for_call = []

        argument_ids = [opName.IDENTIFIER().getText() for opName in ctx.operandName()]

        for id in argument_ids:
            try:
                v = self.context.variables.find_var_by_tag(tag=id, scope=self.function_call_id)

                shape = v.shape

                if len(args_for_check) == 0 or args_for_check[len(args_for_check) - 1][0] != shape:
                    args_for_check.append([shape, 1])
                else:
                    args_for_check[len(args_for_check) - 1][1] += 1

                if (v.unreachable):
                    print(f"Undeclared shape {v.name}")
                    raise graph.UndeclaredShapeError

                args_for_call.append(v)
            except:
                v = self.context.variables.find_var_by_tag(tag=id, scope=self.function_call_id).data
                shape = v.shape

                if len(args_for_check) == 0 or args_for_check[len(args_for_check) - 1][0] != shape:
                    args_for_check.append([shape, 1])
                else:
                    args_for_check[len(args_for_check) - 1][1] += 1

                if (v.unreachable):
                    print(f"Undeclared shape {v.name}")
                    raise graph.UndeclaredShapeError

                args_for_call.append(v)

        function_called = Function(name=ctx.IDENTIFIER().getText(), args=args_for_check)

        if not self.context.check_call(function_called):
            raise FunctionSignatureError(function_called.name)

        function_result = self.context.call_function(global_graph=self.func_relations_graph,
                                                     name=ctx.IDENTIFIER().getText(), args=args_for_call,
                                                     parent_id=self.function_call_id)

        return function_result


