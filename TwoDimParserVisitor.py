# Generated from TwoDimParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TwoDimParser import TwoDimParser
else:
    from TwoDimParser import TwoDimParser

# This class defines a complete generic visitor for a parse tree produced by TwoDimParser.

class TwoDimParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TwoDimParser#sourceFile.
    def visitSourceFile(self, ctx:TwoDimParser.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#viewportClause.
    def visitViewportClause(self, ctx:TwoDimParser.ViewportClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#declaration.
    def visitDeclaration(self, ctx:TwoDimParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#identifierList.
    def visitIdentifierList(self, ctx:TwoDimParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#expressionList.
    def visitExpressionList(self, ctx:TwoDimParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#functionDecl.
    def visitFunctionDecl(self, ctx:TwoDimParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#signature.
    def visitSignature(self, ctx:TwoDimParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#parameters.
    def visitParameters(self, ctx:TwoDimParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#parameterDecl.
    def visitParameterDecl(self, ctx:TwoDimParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#functionCall.
    def visitFunctionCall(self, ctx:TwoDimParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#drawClause.
    def visitDrawClause(self, ctx:TwoDimParser.DrawClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#shapeDecl.
    def visitShapeDecl(self, ctx:TwoDimParser.ShapeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#shapeSpec.
    def visitShapeSpec(self, ctx:TwoDimParser.ShapeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#block.
    def visitBlock(self, ctx:TwoDimParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#statementList.
    def visitStatementList(self, ctx:TwoDimParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#statement.
    def visitStatement(self, ctx:TwoDimParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#simpleStmt.
    def visitSimpleStmt(self, ctx:TwoDimParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#expressionStmt.
    def visitExpressionStmt(self, ctx:TwoDimParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#shapeArguments.
    def visitShapeArguments(self, ctx:TwoDimParser.ShapeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#assignment.
    def visitAssignment(self, ctx:TwoDimParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#assign_op.
    def visitAssign_op(self, ctx:TwoDimParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#ifStmt.
    def visitIfStmt(self, ctx:TwoDimParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#switchStmt.
    def visitSwitchStmt(self, ctx:TwoDimParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#exprSwitchStmt.
    def visitExprSwitchStmt(self, ctx:TwoDimParser.ExprSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#exprCaseClause.
    def visitExprCaseClause(self, ctx:TwoDimParser.ExprCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#exprSwitchCase.
    def visitExprSwitchCase(self, ctx:TwoDimParser.ExprSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeName.
    def visitTypeName(self, ctx:TwoDimParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#relationDetailOp.
    def visitRelationDetailOp(self, ctx:TwoDimParser.RelationDetailOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#singleLevelRelationOp.
    def visitSingleLevelRelationOp(self, ctx:TwoDimParser.SingleLevelRelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#multiLevelRelationOp.
    def visitMultiLevelRelationOp(self, ctx:TwoDimParser.MultiLevelRelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#relationExpr.
    def visitRelationExpr(self, ctx:TwoDimParser.RelationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#expression.
    def visitExpression(self, ctx:TwoDimParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:TwoDimParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#operand.
    def visitOperand(self, ctx:TwoDimParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#literal.
    def visitLiteral(self, ctx:TwoDimParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#basicLit.
    def visitBasicLit(self, ctx:TwoDimParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#integer.
    def visitInteger(self, ctx:TwoDimParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#operandName.
    def visitOperandName(self, ctx:TwoDimParser.OperandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#string_.
    def visitString_(self, ctx:TwoDimParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#arguments.
    def visitArguments(self, ctx:TwoDimParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#eos.
    def visitEos(self, ctx:TwoDimParser.EosContext):
        return self.visitChildren(ctx)



del TwoDimParser