# Generated from TwoDimParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TwoDimParser import TwoDimParser
else:
    from TwoDimParser import TwoDimParser

# This class defines a complete listener for a parse tree produced by TwoDimParser.
class TwoDimParserListener(ParseTreeListener):

    # Enter a parse tree produced by TwoDimParser#sourceFile.
    def enterSourceFile(self, ctx:TwoDimParser.SourceFileContext):
        pass

    # Exit a parse tree produced by TwoDimParser#sourceFile.
    def exitSourceFile(self, ctx:TwoDimParser.SourceFileContext):
        pass


    # Enter a parse tree produced by TwoDimParser#viewportClause.
    def enterViewportClause(self, ctx:TwoDimParser.ViewportClauseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#viewportClause.
    def exitViewportClause(self, ctx:TwoDimParser.ViewportClauseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#declaration.
    def enterDeclaration(self, ctx:TwoDimParser.DeclarationContext):
        pass

    # Exit a parse tree produced by TwoDimParser#declaration.
    def exitDeclaration(self, ctx:TwoDimParser.DeclarationContext):
        pass


    # Enter a parse tree produced by TwoDimParser#identifierList.
    def enterIdentifierList(self, ctx:TwoDimParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by TwoDimParser#identifierList.
    def exitIdentifierList(self, ctx:TwoDimParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by TwoDimParser#expressionList.
    def enterExpressionList(self, ctx:TwoDimParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by TwoDimParser#expressionList.
    def exitExpressionList(self, ctx:TwoDimParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by TwoDimParser#functionDecl.
    def enterFunctionDecl(self, ctx:TwoDimParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#functionDecl.
    def exitFunctionDecl(self, ctx:TwoDimParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#signature.
    def enterSignature(self, ctx:TwoDimParser.SignatureContext):
        pass

    # Exit a parse tree produced by TwoDimParser#signature.
    def exitSignature(self, ctx:TwoDimParser.SignatureContext):
        pass


    # Enter a parse tree produced by TwoDimParser#parameters.
    def enterParameters(self, ctx:TwoDimParser.ParametersContext):
        pass

    # Exit a parse tree produced by TwoDimParser#parameters.
    def exitParameters(self, ctx:TwoDimParser.ParametersContext):
        pass


    # Enter a parse tree produced by TwoDimParser#parameterDecl.
    def enterParameterDecl(self, ctx:TwoDimParser.ParameterDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#parameterDecl.
    def exitParameterDecl(self, ctx:TwoDimParser.ParameterDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#functionCall.
    def enterFunctionCall(self, ctx:TwoDimParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by TwoDimParser#functionCall.
    def exitFunctionCall(self, ctx:TwoDimParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by TwoDimParser#drawClause.
    def enterDrawClause(self, ctx:TwoDimParser.DrawClauseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#drawClause.
    def exitDrawClause(self, ctx:TwoDimParser.DrawClauseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#shapeDecl.
    def enterShapeDecl(self, ctx:TwoDimParser.ShapeDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#shapeDecl.
    def exitShapeDecl(self, ctx:TwoDimParser.ShapeDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#shapeSpec.
    def enterShapeSpec(self, ctx:TwoDimParser.ShapeSpecContext):
        pass

    # Exit a parse tree produced by TwoDimParser#shapeSpec.
    def exitShapeSpec(self, ctx:TwoDimParser.ShapeSpecContext):
        pass


    # Enter a parse tree produced by TwoDimParser#block.
    def enterBlock(self, ctx:TwoDimParser.BlockContext):
        pass

    # Exit a parse tree produced by TwoDimParser#block.
    def exitBlock(self, ctx:TwoDimParser.BlockContext):
        pass


    # Enter a parse tree produced by TwoDimParser#statementList.
    def enterStatementList(self, ctx:TwoDimParser.StatementListContext):
        pass

    # Exit a parse tree produced by TwoDimParser#statementList.
    def exitStatementList(self, ctx:TwoDimParser.StatementListContext):
        pass


    # Enter a parse tree produced by TwoDimParser#statement.
    def enterStatement(self, ctx:TwoDimParser.StatementContext):
        pass

    # Exit a parse tree produced by TwoDimParser#statement.
    def exitStatement(self, ctx:TwoDimParser.StatementContext):
        pass


    # Enter a parse tree produced by TwoDimParser#simpleStmt.
    def enterSimpleStmt(self, ctx:TwoDimParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#simpleStmt.
    def exitSimpleStmt(self, ctx:TwoDimParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#expressionStmt.
    def enterExpressionStmt(self, ctx:TwoDimParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#expressionStmt.
    def exitExpressionStmt(self, ctx:TwoDimParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#shapeArguments.
    def enterShapeArguments(self, ctx:TwoDimParser.ShapeArgumentsContext):
        pass

    # Exit a parse tree produced by TwoDimParser#shapeArguments.
    def exitShapeArguments(self, ctx:TwoDimParser.ShapeArgumentsContext):
        pass


    # Enter a parse tree produced by TwoDimParser#assignment.
    def enterAssignment(self, ctx:TwoDimParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TwoDimParser#assignment.
    def exitAssignment(self, ctx:TwoDimParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TwoDimParser#assign_op.
    def enterAssign_op(self, ctx:TwoDimParser.Assign_opContext):
        pass

    # Exit a parse tree produced by TwoDimParser#assign_op.
    def exitAssign_op(self, ctx:TwoDimParser.Assign_opContext):
        pass


    # Enter a parse tree produced by TwoDimParser#ifStmt.
    def enterIfStmt(self, ctx:TwoDimParser.IfStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#ifStmt.
    def exitIfStmt(self, ctx:TwoDimParser.IfStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#switchStmt.
    def enterSwitchStmt(self, ctx:TwoDimParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#switchStmt.
    def exitSwitchStmt(self, ctx:TwoDimParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#exprSwitchStmt.
    def enterExprSwitchStmt(self, ctx:TwoDimParser.ExprSwitchStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#exprSwitchStmt.
    def exitExprSwitchStmt(self, ctx:TwoDimParser.ExprSwitchStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#exprCaseClause.
    def enterExprCaseClause(self, ctx:TwoDimParser.ExprCaseClauseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#exprCaseClause.
    def exitExprCaseClause(self, ctx:TwoDimParser.ExprCaseClauseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#exprSwitchCase.
    def enterExprSwitchCase(self, ctx:TwoDimParser.ExprSwitchCaseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#exprSwitchCase.
    def exitExprSwitchCase(self, ctx:TwoDimParser.ExprSwitchCaseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeName.
    def enterTypeName(self, ctx:TwoDimParser.TypeNameContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeName.
    def exitTypeName(self, ctx:TwoDimParser.TypeNameContext):
        pass


    # Enter a parse tree produced by TwoDimParser#relationDetailOp.
    def enterRelationDetailOp(self, ctx:TwoDimParser.RelationDetailOpContext):
        pass

    # Exit a parse tree produced by TwoDimParser#relationDetailOp.
    def exitRelationDetailOp(self, ctx:TwoDimParser.RelationDetailOpContext):
        pass


    # Enter a parse tree produced by TwoDimParser#singleLevelRelationOp.
    def enterSingleLevelRelationOp(self, ctx:TwoDimParser.SingleLevelRelationOpContext):
        pass

    # Exit a parse tree produced by TwoDimParser#singleLevelRelationOp.
    def exitSingleLevelRelationOp(self, ctx:TwoDimParser.SingleLevelRelationOpContext):
        pass


    # Enter a parse tree produced by TwoDimParser#multiLevelRelationOp.
    def enterMultiLevelRelationOp(self, ctx:TwoDimParser.MultiLevelRelationOpContext):
        pass

    # Exit a parse tree produced by TwoDimParser#multiLevelRelationOp.
    def exitMultiLevelRelationOp(self, ctx:TwoDimParser.MultiLevelRelationOpContext):
        pass


    # Enter a parse tree produced by TwoDimParser#relationExpr.
    def enterRelationExpr(self, ctx:TwoDimParser.RelationExprContext):
        pass

    # Exit a parse tree produced by TwoDimParser#relationExpr.
    def exitRelationExpr(self, ctx:TwoDimParser.RelationExprContext):
        pass


    # Enter a parse tree produced by TwoDimParser#expression.
    def enterExpression(self, ctx:TwoDimParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TwoDimParser#expression.
    def exitExpression(self, ctx:TwoDimParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TwoDimParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:TwoDimParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by TwoDimParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:TwoDimParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by TwoDimParser#operand.
    def enterOperand(self, ctx:TwoDimParser.OperandContext):
        pass

    # Exit a parse tree produced by TwoDimParser#operand.
    def exitOperand(self, ctx:TwoDimParser.OperandContext):
        pass


    # Enter a parse tree produced by TwoDimParser#literal.
    def enterLiteral(self, ctx:TwoDimParser.LiteralContext):
        pass

    # Exit a parse tree produced by TwoDimParser#literal.
    def exitLiteral(self, ctx:TwoDimParser.LiteralContext):
        pass


    # Enter a parse tree produced by TwoDimParser#basicLit.
    def enterBasicLit(self, ctx:TwoDimParser.BasicLitContext):
        pass

    # Exit a parse tree produced by TwoDimParser#basicLit.
    def exitBasicLit(self, ctx:TwoDimParser.BasicLitContext):
        pass


    # Enter a parse tree produced by TwoDimParser#integer.
    def enterInteger(self, ctx:TwoDimParser.IntegerContext):
        pass

    # Exit a parse tree produced by TwoDimParser#integer.
    def exitInteger(self, ctx:TwoDimParser.IntegerContext):
        pass


    # Enter a parse tree produced by TwoDimParser#operandName.
    def enterOperandName(self, ctx:TwoDimParser.OperandNameContext):
        pass

    # Exit a parse tree produced by TwoDimParser#operandName.
    def exitOperandName(self, ctx:TwoDimParser.OperandNameContext):
        pass


    # Enter a parse tree produced by TwoDimParser#string_.
    def enterString_(self, ctx:TwoDimParser.String_Context):
        pass

    # Exit a parse tree produced by TwoDimParser#string_.
    def exitString_(self, ctx:TwoDimParser.String_Context):
        pass


    # Enter a parse tree produced by TwoDimParser#arguments.
    def enterArguments(self, ctx:TwoDimParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by TwoDimParser#arguments.
    def exitArguments(self, ctx:TwoDimParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by TwoDimParser#eos.
    def enterEos(self, ctx:TwoDimParser.EosContext):
        pass

    # Exit a parse tree produced by TwoDimParser#eos.
    def exitEos(self, ctx:TwoDimParser.EosContext):
        pass



del TwoDimParser