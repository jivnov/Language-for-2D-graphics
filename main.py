import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener


class MyTwoDimParserListener(TwoDimParserListener):
    def enterSourceFile(self, ctx: TwoDimParser.SourceFileContext):  # XYZContext classes are syntax trees; XYZ is the root node; you can access all the child nodes and their values
        print("I just entered the source file")

    def enterDrawClause(self, ctx: TwoDimParser.DrawClauseContext):
        print(f"Entered draw clause! Drawing shape {ctx.IDENTIFIER()}")  # Here identifier is a single value as drawClause can have 0 or 1 IDENTIFIERs passed to it (check the TwoDimParser.g4 rule)

    def enterShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        print(f"Planning/declaring shapes {ctx.IDENTIFIER(0)}")  # Here IDENTIFIER is a list, because you can pass multiple IDENTIFIERs in a single shapeSpec call

    def exitShapeSpec(self, ctx: TwoDimParser.ShapeSpecContext):
        print(f"Finished planning/declaring shapes: {ctx.IDENTIFIER(0)}")

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
