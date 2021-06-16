import sys

from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

from MyFirstPassTwoDimParserListener import FirstPassTwoDimParserListener
from MySecondPassTwoDimParserListener import SecondPassTwoDimParserListener
from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser

import logging
import os

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        if e.input.tokens[offending_symbol.tokenIndex-1].text.upper() in ["RIGHT", "LEFT", "TOP", "BOT", "IN"] or (e.input.tokens[offending_symbol.tokenIndex-1].text.upper()==" " and e.input.tokens[offending_symbol.tokenIndex-2].text.upper() in ["RIGHT", "LEFT", "TOP", "BOT", "IN"]):
            raise SyntaxError(f"Syntax error in relational operation at line {line} column {column}. Check the operation declaration.")
        raise SyntaxError(f"Symbol \"{offending_symbol.text}\" at line {line} column {column} not recognized. \n"
                          f"Tip: If \"{offending_symbol.text}\" is what you meant here, check if preceding symbols"
                          f" are also correct and conforms with syntax. Also check if there is a semicolon in "
                          f"the preceding line.")  # e.input.tokenSource.inputStream.strdata[:offending_symbol.start]

class LexerErrorListener(ErrorListener):
    def __init__(self):
        super(LexerErrorListener, self).__init__()

    def syntaxError(self, recognizer, offending_token, line, column, msg, e):
        endIndex = e.input.index
        offset = len(str(e.input.strdata)) - e.input.index
        for c in [' ', ';', '(', ')', '[', ']', '{', '}', '<', '>', ',']:
            if str(e.input.strdata)[e.input.index:].find(c) >= 0 and str(e.input.strdata)[e.input.index:].find(c) < offset:
                offset = str(e.input.strdata)[e.input.index:].find(c)
        endIndex += offset

        offending_token = str(e.input.strdata)[e.startIndex:endIndex]
        raise SyntaxError(f"Syntax Error: failed to parse token \"{offending_token}\" at line {line} column {column}."
                          f"Check if it fits in syntax rules, is typed correctly and the register used is appropriate.")


def main(argv):
    try:
        input_stream = FileStream(argv[1])
        lexer = TwoDimLexer(input_stream)
        lexer.addErrorListener(LexerErrorListener())
        stream = CommonTokenStream(lexer)
        parser = TwoDimParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SyntaxErrorListener())

        # Start rule
        tree = parser.sourceFile()

        logging.info(Trees.toStringTree(tree, ruleNames=parser.ruleNames))

        print(Trees.toStringTree(tree, ruleNames=parser.ruleNames))
        # Print what the parser sees

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
    except IndexError as e:
        logging.error(e)
        if len(argv) < 2:
            logging.error("Not all necessary arguments have been provided.")
    except FileNotFoundError as e:
        logging.error(e)
    except Exception as e:
        message = f"File {'' if len(argv) < 2 else os.path.abspath(argv[1])}\n{e}"
        exception_type = e.__class__
        logging.error(message)

if __name__ == '__main__':
    try:
        main(sys.argv)
    except:
        print("fuyfllgkg")
