import sys
import drawing
import graph
from graph import UndeclaredShapeError

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener


class MyTwoDimParserListener(TwoDimParserListener):
    def __init__(self):
        super().__init__()
        self.relations_graph = graph.Graph()
        self.res = None

    def enterSourceFile(self,
                        ctx: TwoDimParser.SourceFileContext):  # XYZContext classes are syntax trees; XYZ is the root
        # node; you can access all the child nodes and their values
        print("I just entered the source file")

    def enterDrawClause(self, ctx: TwoDimParser.DrawClauseContext):
        self.relations_graph.get_relations(self.relations_graph.find_vertex(ctx.IDENTIFIER()))
        self.res.draw(self.relations_graph.find_vertex(vertex_name = ctx.IDENTIFIER()))
        self.res.canvas.save(pretty = True)
        # Here identifier is a single value as drawClause can have 0 or 1 IDENTIFIERs passed to it (check the TwoDimParser.g4 rule)
        print(f"Entered draw clause! Drawing shape {ctx.IDENTIFIER()}")  

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, var_name in enumerate(ctx.IDENTIFIER()):
            # TODO
            # At the moment assuming SIZE is the only argument
            self.relations_graph.add_vertex(
                graph.Vertex(parent_graph=self.relations_graph, var_name=var_name, shape=ctx.typeName().getText(),
                             args=[size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            )

    def enterViewportClause(self, ctx: TwoDimParser.ViewportClauseContext):
        # now was here for testing purposes
        self.res = drawing.Drawing2d(int(ctx.DECIMAL_LIT(0).getText()), int(ctx.DECIMAL_LIT(1).getText()))

    def enterRelationExpr(self, ctx: TwoDimParser.RelationExprContext):
        var_name1 = ctx.primaryExpr(0).operand().operandName().getText()
        var_name2 = ctx.primaryExpr(1).operand().operandName().getText()
        try:
            op1 = self.relations_graph.find_vertex(var_name1)
            op2 = self.relations_graph.find_vertex(var_name2)
            self.relations_graph.add_edge(op1, op2, graph.Relation.from_string(ctx.singleLevelRelationOp().getText()))
        except UndeclaredShapeError:
            print(f"Undeclared shape {var_name1} or {var_name2}")


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TwoDimLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TwoDimParser(stream)

    # Start rule
    tree = parser.sourceFile()
    print(Trees.toStringTree(tree, ruleNames=parser.ruleNames))  # Print what the parser sees

    # Create listener
    printer = MyTwoDimParserListener()

    # Walk the generated tree with our listener attached
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    # TODO: Add two-pass compilation (1st step: find Function definitions etc., store them as Graphs for later use; 2nd step: go through "normal" imperative code, use previously defined functions)


if __name__ == '__main__':
    main(sys.argv)
