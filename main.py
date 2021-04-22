import sys
import drawing
import graph

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener


class MyTwoDimParserListener(TwoDimParserListener):
    relationsGraph = graph.Graph()
    res = None

    def enterSourceFile(self, ctx: TwoDimParser.SourceFileContext):  # XYZContext classes are syntax trees; XYZ is the root node; you can access all the child nodes and their values
        print("I just entered the source file")

    def enterDrawClause(self, ctx: TwoDimParser.DrawClauseContext):
        self.relationsGraph.get_relations(self.relationsGraph.find_vertex(ctx.IDENTIFIER()))
        self.res.canvas.saveSvg('example.svg')
        print(f"Entered draw clause! Drawing shape {ctx.IDENTIFIER()}")  # Here identifier is a single value as drawClause can have 0 or 1 IDENTIFIERs passed to it (check the TwoDimParser.g4 rule)

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        for i, id in enumerate(ctx.IDENTIFIER()):
            #TODO
            #At the moment assuming SIZE is the only argument
            self.relationsGraph.add_vertex(
                graph.Vertex(var_name = id, shape = ctx.typeName().getText(), args = [size_lit.getText() for size_lit in ctx.shapeArguments(i).SIZE_LIT()])
            )
        
    def enterViewportClause(self, ctx: TwoDimParser.ViewportClauseContext):
        #now was here for testing purposes
        self.res = drawing.Drawing2d(int(ctx.DECIMAL_LIT(0).getText()),int(ctx.DECIMAL_LIT(1).getText()))
        
        
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


if __name__ == '__main__':
    main(sys.argv)
