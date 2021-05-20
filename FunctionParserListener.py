import graph

from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener
from Function import Function, FunctionSignatureError

class FunctionParserListener(TwoDimParserListener):

    def __init__(self, global_context, relations_graph, func_relations_graph):
        super().__init__()
        self.relations_graph = relations_graph
        self.func_relations_graph = func_relations_graph
        self.context = global_context

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, var_name in enumerate(ctx.IDENTIFIER()):
            # TODO
            # At the moment assuming SIZE is the only argument
            v = graph.Vertex(parent_graph=self.func_relations_graph, var_name=var_name.getText(), shape=ctx.typeName().getText(),
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            self.func_relations_graph.add_vertex(v)

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ctx.primaryExpr(0).operand().operandName().getText()
        var_name2 = ctx.primaryExpr(1).operand().operandName().getText()
        try:
            op1 = self.func_relations_graph.find_vertex(var_name1)
            op2 = self.func_relations_graph.find_vertex(var_name2)
            self.func_relations_graph.add_relation(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))
        except graph.UndeclaredShapeError:
            print(f"Undeclared shape {var_name1} or {var_name2}")

    def enterFunctionCall(self, ctx: TwoDimParser.FunctionCallContext):
        # checking function call for correctness
        args_for_check = []
        args_for_call = []

        argument_ids = [opName.IDENTIFIER().getText() for opName in ctx.operandName()]

        for id in argument_ids:
            try:
                v = self.func_relations_graph.find_vertex(id)

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
                v = self.relations_graph.find_vertex(id)
                shape = v.shape

                if len(args_for_check) == 0 or args_for_check[len(args_for_check) - 1][0] != shape:
                    args_for_check.append([shape, 1])
                else:
                    args_for_check[len(args_for_check) - 1][1] += 1

                if (v.unreachable):
                    print(f"Undeclared shape {v.name}")
                    raise graph.UndeclaredShapeError

                args_for_call.append(v)

        function_called = Function(name=ctx.IDENTIFIER(), args=args_for_check)

        if not self.context.check_call(function_called):
            raise FunctionSignatureError(function_called.name)

        function_result = self.context.call_function(global_graph=self.func_relations_graph, name=ctx.IDENTIFIER(), args=args_for_call)

        self.func_relations_graph.merge_with(function_result)

    def exitFunctionCall(self, ctx:TwoDimParser.FunctionCallContext):
        args_for_call = []

        argument_ids = [opName.IDENTIFIER().getText() for opName in ctx.operandName()]

        for id in argument_ids:
           v = self.func_relations_graph.find_vertex(id)
           args_for_call.append(v)

        for v in self.func_relations_graph.vertices:
            if v not in args_for_call:
                v.unreachable = True


