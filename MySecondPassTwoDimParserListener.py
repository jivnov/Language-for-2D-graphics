import sys
from copy import copy

import drawing
import graph
from Function import Function, FunctionSignatureError
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener


def center_graph(d2d: drawing.Drawing2d, g: graph.Graph):
    if g.x != (desired_x := (d2d.viewport_width // 2 - g.width // 2)):
        g.move_horizontal(desired_x - g.x)
    # TODO: Add vertical centering


class SecondPassTwoDimParserListener(TwoDimParserListener):

    def __init__(self, global_context, parser):
        super().__init__()
        self.relations_graph = graph.Graph()
        self.res = None
        self.context = global_context
        self.parser = parser

    def enterSourceFile(self,
                        ctx: TwoDimParser.SourceFileContext):  # XYZContext classes are syntax trees; XYZ is the root
        # node; you can access all the child nodes and their values
        print("I just entered the source file for the 2nd time")

    def enterDrawClause(self, ctx: TwoDimParser.DrawClauseContext):
        self.relations_graph.print_relations(self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText()).data)
        self.relations_graph.center(self.res.viewport_width, self.res.viewport_height)
        self.res.draw(self.context.variables.find_var_by_tag(tag=ctx.IDENTIFIER().getText()).data)
        self.res.canvas.save(pretty=True)

        # Here identifier is a single value as drawClause can have 0 or 1 IDENTIFIERs passed to it (check the TwoDimParser.g4 rule)
        print(f"Entered draw clause! Drawing shape {ctx.IDENTIFIER()}")
        print(
            f"Drawing graph: {self.relations_graph.x=}, {self.relations_graph.y=}; {self.relations_graph.width=}, {self.relations_graph.height=}")

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, var_name in enumerate(ctx.IDENTIFIER()):
            # TODO
            # At the moment assuming SIZE is the only argument

            v = graph.Vertex(parent_graph=self.relations_graph,
                             shape=ctx.typeName().getText(),
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            self.context.variables.add_variable(tag=var_name.getText(), name=v.uid, content=v)
            self.relations_graph.add_vertex(v)

    def enterViewportClause(self, ctx: TwoDimParser.ViewportClauseContext):
        # now was here for testing purposes
        self.res = drawing.Drawing2d(int(ctx.DECIMAL_LIT(0).getText()), int(ctx.DECIMAL_LIT(1).getText()))

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ctx.primaryExpr(0).operand().operandName().getText()
        var_name2 = ctx.primaryExpr(1).operand().operandName().getText()
        try:
            op1 = self.context.variables.find_var_by_tag(var_name1).data
            op2 = self.context.variables.find_var_by_tag(var_name2).data
            self.relations_graph.add_relation(op1, op2,
                                              graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))

            graph_to_return = graph.Graph()
            graph_to_return.add_vertex(op1)
            graph_to_return.add_vertex(op2)
            graph_to_return.add_relation(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))
            return graph_to_return.export_as_vertex()

        except graph.UndeclaredShapeError:
            print(f"Undeclared shape {var_name1} or {var_name2}")

    def enterFunctionDecl(self, ctx: TwoDimParser.FunctionDeclContext):
        del ctx.children[len(ctx.children)-1]

    def enterAssignment(self, ctx: TwoDimParser.AssignmentContext):
        data = None
        if ctx.expression().functionCall() is not None:
            data = self.enterFunctionCall(ctx.expression().functionCall())
        elif ctx.expression().relationExpr() is not None:
            data = self.enterRelationExpr(ctx.expression().relationExpr())
        elif ctx.expression().primaryExpr() is not None:
            data = self.context.variables.find_var_by_tag(
                ctx.expression().primaryExpr()[0].operand().operandName().IDENTIFIER().getText()
            ).data

        self.relations_graph.remove_vertex(self.relations_graph.find_vertex(self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText()).data.uid))
        self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText()).data = copy(data)
        self.relations_graph.add_vertex(self.context.variables.find_var_by_tag(ctx.IDENTIFIER().getText()).data)

    def enterAssignmentDeclarationStmt(self, ctx: TwoDimParser.AssignmentDeclarationStmtContext):
        data = self.enterFunctionCall(ctx.functionCall())

        # Remove the function call after calculating its output so the Walker doesn't enter it a second time
        ctx.removeLastChild()

        # TODO: At the moment assuming SIZE is the only argument
        v = graph.Vertex(parent_graph=self.relations_graph,
                         shape='shape',
                         args=[size_lit.getText() for size_lit in ctx.shapeArguments().SIZE_LIT()],
                         content=data.content)
        self.context.variables.add_variable(tag=ctx.IDENTIFIER().getText(), name=v.uid, content=v)
        self.relations_graph.add_vertex(v)


    def enterFunctionCall(self, ctx: TwoDimParser.FunctionCallContext):
        # checking function call for correctness
        args_for_check = []
        args_for_call = []

        argument_ids = [opName.IDENTIFIER().getText() for opName in ctx.operandName()]

        for id in argument_ids:
            v = self.context.variables.find_var_by_tag(id).data
            shape = v.shape

            if len(args_for_check) == 0 or args_for_check[len(args_for_check)-1][0] != shape:
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

        function_result = self.context.call_function(global_graph=self.relations_graph, name=ctx.IDENTIFIER(), args=args_for_call)

        return function_result

