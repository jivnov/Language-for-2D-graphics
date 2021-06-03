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
        try:
            for i, var_name in enumerate(ctx.IDENTIFIER()):
                # TODO
                # At the moment assuming SIZE is the only argument
                color_vals = None
                if ctx.shapeColor(i) is not None:
                    color_vals = tuple(int(decimal_lit.getText()) for decimal_lit in ctx.shapeColor(i).DECIMAL_LIT())

                v = graph.Vertex(parent_graph=self.func_relations_graph,
                                 shape=ctx.typeName().getText(),
                                 args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()],
                                 color=color_vals
                                 )
                self.func_relations_graph.add_vertex(v)
                self.context.variables.add_variable(tag=var_name.getText(), name=v.uid, content=v, scope=self.function_call_id)
        except Exception as e:
            message = f"Line {ctx.start.line}, {type(e).__name__}: {'' if len(e.args) == 0 else e.args[0]}"
            exception_type = e.__class__
            raise exception_type(message)

    def enterAssignmentDeclarationStmt(self, ctx: TwoDimParser.AssignmentDeclarationStmtContext):
        try:
            v_from_func: graph.Vertex = self.enterFunctionCall(ctx.functionCall())

            # Remove the function call after calculating its output so the Walker doesn't enter it a second time
            ctx.removeLastChild()

            # TODO: At the moment assuming SIZE is the only argument
            v = graph.Vertex(parent_graph=self.func_relations_graph,
                             shape='shape',
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments().SIZE_LIT()],
                             content=v_from_func.content)
            self.func_relations_graph.add_vertex(v)
            self.context.variables.add_variable(tag=ctx.IDENTIFIER().getText(), name=v.uid, content=v)
        except Exception as e:
            message = f"Line {ctx.start.line}, {type(e).__name__}: {'' if len(e.args) == 0 else e.args[0]}"
            exception_type = e.__class__
            raise exception_type(message)

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ''
        var_name2 = ''
        try:
            for relation_op_index in range(len(ctx.singleLevelRelationOp())):
                var_name1 = ctx.primaryExpr(relation_op_index).operand().operandName().getText()
                var_name2 = ctx.primaryExpr(relation_op_index + 1).operand().operandName().getText()

                op1 = self.context.variables.find_var_by_tag(tag=var_name1, scope=self.function_call_id).data
                op2 = self.context.variables.find_var_by_tag(tag=var_name2, scope=self.function_call_id).data
                self.func_relations_graph\
                    .add_relation(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp(relation_op_index).getText()))
        except Exception as e:
            message = f"Line {ctx.start.line}, {type(e).__name__}: {'' if len(e.args) == 0 else e.args[0]}"
            exception_type = e.__class__
            raise exception_type(message)

    def enterFunctionCall(self, ctx: TwoDimParser.FunctionCallContext):
        try:
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

                    if v.unreachable:
                        raise graph.UndeclaredShapeException(id)

                    args_for_call.append(v)
                except:
                    v = self.context.variables.find_var_by_tag(tag=id, scope=self.function_call_id).data
                    shape = v.shape

                    if len(args_for_check) == 0 or args_for_check[len(args_for_check) - 1][0] != shape:
                        args_for_check.append([shape, 1])
                    else:
                        args_for_check[len(args_for_check) - 1][1] += 1

                    if v.unreachable:
                        raise graph.UndeclaredShapeException(id)

                    args_for_call.append(v)

            function_called = Function(name=ctx.IDENTIFIER().getText(), args=args_for_check)

            if not self.context.check_call(function_called):
                raise FunctionSignatureError(function_called.name)

            function_result = self.context.call_function(global_graph=self.func_relations_graph,
                                                         name=ctx.IDENTIFIER().getText(), args=args_for_call,
                                                         parent_id=self.function_call_id)

            return function_result
        except Exception as e:
            message = f"Line {ctx.start.line}, {type(e).__name__}: {'' if len(e.args) == 0 else e.args[0]}"
            exception_type = e.__class__
            raise exception_type(message)



