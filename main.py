import sys
import drawing
import graph
from graph import UndeclaredShapeError

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener
from TwoDimParserVisitor import TwoDimParserVisitor
from MyFirstPassTwoDimParserListener import FirstPassTwoDimParserListener
from MySecondPassTwoDimParserListener import SecondPassTwoDimParserListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TwoDimLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TwoDimParser(stream)

    # Start rule
    tree = parser.sourceFile()
    print(Trees.toStringTree(tree, ruleNames=parser.ruleNames))  # Print what the parser sees

    ##############################################
    ###############  First Pass  #################
    ##############################################

    # Create listener
    printer = FirstPassTwoDimParserListener()

    # Walk the generated tree with our listener attached
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    global_context = printer.context

    ##############################################
    ###############  Second Pass  ################
    ##############################################

    # Create listener
    printer = SecondPassTwoDimParserListener(global_context=global_context, parser = parser)

    # Walk the generated tree with our listener attached
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    # TODO: Add two-pass compilation (1st step: find Function definitions etc., store them as Graphs for later use; 2nd step: go through "normal" imperative code, use previously defined functions)



if __name__ == '__main__':
    main(sys.argv)
