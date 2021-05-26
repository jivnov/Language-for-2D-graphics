import sys
import drawing
import graph
import GlobalContext

from antlr4 import *
from antlr4.tree.Trees import Trees

from TwoDimLexer import TwoDimLexer
from TwoDimParser import TwoDimParser
from TwoDimParserListener import TwoDimParserListener


class FirstPassTwoDimParserListener(TwoDimParserListener):

    def __init__(self):
        super().__init__()
        self.context = GlobalContext.GlobalContext()

    def enterSourceFile(self,
                        ctx: TwoDimParser.SourceFileContext):  # XYZContext classes are syntax trees; XYZ is the root
        # node; you can access all the child nodes and their values
        print("I just entered the source file for the 1st time")

    def enterFunctionDecl(self, ctx: TwoDimParser.FunctionDeclContext):
        print(f"Entered function declaration {ctx.IDENTIFIER()}")
        function_args = []
        function_args_names = []
        params = ctx.signature().parameters().parameterDecl()

        for param in params:
            param_names_list = param.identifierList().IDENTIFIER()
            function_args.append([param.typeName().getText(), len(param_names_list)])
            function_args_names.extend(param_names_list)

        statement_list = ctx.children[len(ctx.children) - 1].statementList().statement()
        function = GlobalContext.Function(ctx.IDENTIFIER(), args=function_args, args_names=function_args_names,
                                          body=ctx.block())

        self.context.add_function(function)
