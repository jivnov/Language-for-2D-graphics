import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from MyFirstPassTwoDimParserListener import FirstPassTwoDimParserListener
from MySecondPassTwoDimParserListener import SecondPassTwoDimParserListener
from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser

import logging
import os


def main(argv):
    try:
        input_stream = FileStream(argv[1])
        lexer = TwoDimLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = TwoDimParser(stream)

        # Start rule
        tree = parser.sourceFile()
        logging.info(Trees.toStringTree(tree, ruleNames=parser.ruleNames))  # Print what the parser sees

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
        if len(argv) >= 3:  # If output path was specified
            printer = SecondPassTwoDimParserListener(global_context=global_context, parser = parser, output_path=argv[2])
        else:
            printer = SecondPassTwoDimParserListener(global_context=global_context, parser = parser, output_path='generated_images/output.svg')

        # Walk the generated tree with our listener attached
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
    except FileNotFoundError as e:
        logging.error(e)
    except Exception as e:
        message = f"File {'' if len(argv) < 2 else os.path.abspath(argv[1])}\n{'' if len(e.args) == 0 else e.args[0]}"
        exception_type = e.__class__
        logging.error(message)

if __name__ == '__main__':
    main(sys.argv)
