import graph

from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener
from Function import Function, FunctionSignatureError

class FunctionParserListener(TwoDimParserListener):

    def __init__(self, global_context, relations_graph, func_relations_graph, call_id=None):
        super().__init__()
        self.relations_graph = relations_graph
        self.func_relations_graph = func_relations_graph
        self.context = global_context
        self.function_call_id = call_id

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, var_name in enumerate(ctx.IDENTIFIER()):
            # TODO
            # At the moment assuming SIZE is the only argument
            v = graph.Vertex(parent_graph=self.func_relations_graph, var_name=var_name.getText(), shape=ctx.typeName().getText(),
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            self.func_relations_graph.add_vertex(v)
            self.context.variables.add_variable(tag=v.name, name=v.uid, content=v, scope=self.function_call_id)

    def enterAssignment(self, ctx:TwoDimParser.AssignmentContext):
        data = None
        if ctx.expression().functionCall() is not None:
            data = self.enterFunctionCall(ctx.expression().functionCall())
        elif ctx.expression().relationExpr() is not None:
            data = self.enterRelationExpr(ctx.expression().relationExpr())
        elif ctx.expression().primaryExpr() is not None:
            data = self.context.variables.find_var_by_tag(
                tag=ctx.expression().primaryExpr()[0].operand().operandName().IDENTIFIER().getText(),
                scope=self.function_call_id
            ).data
        self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText(), self.function_call_id).data = data

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ctx.primaryExpr(0).operand().operandName().getText()
        var_name2 = ctx.primaryExpr(1).operand().operandName().getText()
        try:
            op1 = self.context.variables.find_var_by_tag(tag=var_name1, scope=self.function_call_id).data
            op2 = self.context.variables.find_var_by_tag(tag=var_name2, scope=self.function_call_id).data
            self.func_relations_graph.add_relation(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))

            graph_to_return = graph.Graph()
            graph_to_return.add_vertex(op1)
            graph_to_return.add_vertex(op2)
            graph_to_return.add_relation(op1, op2,
                                         graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))
            return graph_to_return

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

        function_called = Function(name=ctx.IDENTIFIER().getText(), args=args_for_check)

        if not self.context.check_call(function_called):
            raise FunctionSignatureError(function_called.name)

        function_result = self.context.call_function(global_graph=self.func_relations_graph,
                                                     name=ctx.IDENTIFIER().getText(), args=args_for_call,
                                                     parent_id=self.function_call_id)

        for v in function_result.vertices:
            if v not in args_for_call:
                v.unreachable = True
                v.name = f"{ctx.IDENTIFIER()}_{v.name}_{v.uid}"

        self.func_relations_graph.merge_with(function_result)

        return function_result


