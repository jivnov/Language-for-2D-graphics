import sys
from antlr4 import *
from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TwoDimLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TwoDimParser(stream)
    tree = parser.sourceFile()

 
if __name__ == '__main__':
    main(sys.argv)