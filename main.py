import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener


class MyTwoDimParserListener(TwoDimParserListener):
    def enterSourceFile(self, ctx):
        print("I just entered the source file part")


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
