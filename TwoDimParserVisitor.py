# Generated from TwoDimParser.g4 by ANTLR 4.9.2
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


    # Visit a parse tree produced by TwoDimParser#packageClause.
    def visitPackageClause(self, ctx:TwoDimParser.PackageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#importDecl.
    def visitImportDecl(self, ctx:TwoDimParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#importSpec.
    def visitImportSpec(self, ctx:TwoDimParser.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#importPath.
    def visitImportPath(self, ctx:TwoDimParser.ImportPathContext):
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


    # Visit a parse tree produced by TwoDimParser#typeDecl.
    def visitTypeDecl(self, ctx:TwoDimParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeSpec.
    def visitTypeSpec(self, ctx:TwoDimParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#functionDecl.
    def visitFunctionDecl(self, ctx:TwoDimParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#methodDecl.
    def visitMethodDecl(self, ctx:TwoDimParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#receiver.
    def visitReceiver(self, ctx:TwoDimParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#varDecl.
    def visitVarDecl(self, ctx:TwoDimParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#varSpec.
    def visitVarSpec(self, ctx:TwoDimParser.VarSpecContext):
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


    # Visit a parse tree produced by TwoDimParser#incDecStmt.
    def visitIncDecStmt(self, ctx:TwoDimParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#assignment.
    def visitAssignment(self, ctx:TwoDimParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#assign_op.
    def visitAssign_op(self, ctx:TwoDimParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#emptyStmt.
    def visitEmptyStmt(self, ctx:TwoDimParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#labeledStmt.
    def visitLabeledStmt(self, ctx:TwoDimParser.LabeledStmtContext):
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


    # Visit a parse tree produced by TwoDimParser#typeSwitchStmt.
    def visitTypeSwitchStmt(self, ctx:TwoDimParser.TypeSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeSwitchGuard.
    def visitTypeSwitchGuard(self, ctx:TwoDimParser.TypeSwitchGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeCaseClause.
    def visitTypeCaseClause(self, ctx:TwoDimParser.TypeCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeSwitchCase.
    def visitTypeSwitchCase(self, ctx:TwoDimParser.TypeSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeList.
    def visitTypeList(self, ctx:TwoDimParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#recvStmt.
    def visitRecvStmt(self, ctx:TwoDimParser.RecvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#type_.
    def visitType_(self, ctx:TwoDimParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeName.
    def visitTypeName(self, ctx:TwoDimParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeLit.
    def visitTypeLit(self, ctx:TwoDimParser.TypeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#elementType.
    def visitElementType(self, ctx:TwoDimParser.ElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#methodSpec.
    def visitMethodSpec(self, ctx:TwoDimParser.MethodSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#functionType.
    def visitFunctionType(self, ctx:TwoDimParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#signature.
    def visitSignature(self, ctx:TwoDimParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#result.
    def visitResult(self, ctx:TwoDimParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#parameters.
    def visitParameters(self, ctx:TwoDimParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#parameterDecl.
    def visitParameterDecl(self, ctx:TwoDimParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#expression.
    def visitExpression(self, ctx:TwoDimParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:TwoDimParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#unaryExpr.
    def visitUnaryExpr(self, ctx:TwoDimParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#conversion.
    def visitConversion(self, ctx:TwoDimParser.ConversionContext):
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


    # Visit a parse tree produced by TwoDimParser#qualifiedIdent.
    def visitQualifiedIdent(self, ctx:TwoDimParser.QualifiedIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#compositeLit.
    def visitCompositeLit(self, ctx:TwoDimParser.CompositeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#literalType.
    def visitLiteralType(self, ctx:TwoDimParser.LiteralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#literalValue.
    def visitLiteralValue(self, ctx:TwoDimParser.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#elementList.
    def visitElementList(self, ctx:TwoDimParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#keyedElement.
    def visitKeyedElement(self, ctx:TwoDimParser.KeyedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#key.
    def visitKey(self, ctx:TwoDimParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#element.
    def visitElement(self, ctx:TwoDimParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#fieldDecl.
    def visitFieldDecl(self, ctx:TwoDimParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#string_.
    def visitString_(self, ctx:TwoDimParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#anonymousField.
    def visitAnonymousField(self, ctx:TwoDimParser.AnonymousFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#functionLit.
    def visitFunctionLit(self, ctx:TwoDimParser.FunctionLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#index.
    def visitIndex(self, ctx:TwoDimParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#typeAssertion.
    def visitTypeAssertion(self, ctx:TwoDimParser.TypeAssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#arguments.
    def visitArguments(self, ctx:TwoDimParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#methodExpr.
    def visitMethodExpr(self, ctx:TwoDimParser.MethodExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#receiverType.
    def visitReceiverType(self, ctx:TwoDimParser.ReceiverTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TwoDimParser#eos.
    def visitEos(self, ctx:TwoDimParser.EosContext):
        return self.visitChildren(ctx)



del TwoDimParser