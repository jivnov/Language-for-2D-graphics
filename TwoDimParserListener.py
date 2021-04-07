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


    # Enter a parse tree produced by TwoDimParser#packageClause.
    def enterPackageClause(self, ctx:TwoDimParser.PackageClauseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#packageClause.
    def exitPackageClause(self, ctx:TwoDimParser.PackageClauseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#importDecl.
    def enterImportDecl(self, ctx:TwoDimParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#importDecl.
    def exitImportDecl(self, ctx:TwoDimParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#importSpec.
    def enterImportSpec(self, ctx:TwoDimParser.ImportSpecContext):
        pass

    # Exit a parse tree produced by TwoDimParser#importSpec.
    def exitImportSpec(self, ctx:TwoDimParser.ImportSpecContext):
        pass


    # Enter a parse tree produced by TwoDimParser#importPath.
    def enterImportPath(self, ctx:TwoDimParser.ImportPathContext):
        pass

    # Exit a parse tree produced by TwoDimParser#importPath.
    def exitImportPath(self, ctx:TwoDimParser.ImportPathContext):
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


    # Enter a parse tree produced by TwoDimParser#typeDecl.
    def enterTypeDecl(self, ctx:TwoDimParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeDecl.
    def exitTypeDecl(self, ctx:TwoDimParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeSpec.
    def enterTypeSpec(self, ctx:TwoDimParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeSpec.
    def exitTypeSpec(self, ctx:TwoDimParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by TwoDimParser#functionDecl.
    def enterFunctionDecl(self, ctx:TwoDimParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#functionDecl.
    def exitFunctionDecl(self, ctx:TwoDimParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#methodDecl.
    def enterMethodDecl(self, ctx:TwoDimParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#methodDecl.
    def exitMethodDecl(self, ctx:TwoDimParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#receiver.
    def enterReceiver(self, ctx:TwoDimParser.ReceiverContext):
        pass

    # Exit a parse tree produced by TwoDimParser#receiver.
    def exitReceiver(self, ctx:TwoDimParser.ReceiverContext):
        pass


    # Enter a parse tree produced by TwoDimParser#varDecl.
    def enterVarDecl(self, ctx:TwoDimParser.VarDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#varDecl.
    def exitVarDecl(self, ctx:TwoDimParser.VarDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#varSpec.
    def enterVarSpec(self, ctx:TwoDimParser.VarSpecContext):
        pass

    # Exit a parse tree produced by TwoDimParser#varSpec.
    def exitVarSpec(self, ctx:TwoDimParser.VarSpecContext):
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


    # Enter a parse tree produced by TwoDimParser#incDecStmt.
    def enterIncDecStmt(self, ctx:TwoDimParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#incDecStmt.
    def exitIncDecStmt(self, ctx:TwoDimParser.IncDecStmtContext):
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


    # Enter a parse tree produced by TwoDimParser#emptyStmt.
    def enterEmptyStmt(self, ctx:TwoDimParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#emptyStmt.
    def exitEmptyStmt(self, ctx:TwoDimParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#labeledStmt.
    def enterLabeledStmt(self, ctx:TwoDimParser.LabeledStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#labeledStmt.
    def exitLabeledStmt(self, ctx:TwoDimParser.LabeledStmtContext):
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


    # Enter a parse tree produced by TwoDimParser#typeSwitchStmt.
    def enterTypeSwitchStmt(self, ctx:TwoDimParser.TypeSwitchStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeSwitchStmt.
    def exitTypeSwitchStmt(self, ctx:TwoDimParser.TypeSwitchStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeSwitchGuard.
    def enterTypeSwitchGuard(self, ctx:TwoDimParser.TypeSwitchGuardContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeSwitchGuard.
    def exitTypeSwitchGuard(self, ctx:TwoDimParser.TypeSwitchGuardContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeCaseClause.
    def enterTypeCaseClause(self, ctx:TwoDimParser.TypeCaseClauseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeCaseClause.
    def exitTypeCaseClause(self, ctx:TwoDimParser.TypeCaseClauseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeSwitchCase.
    def enterTypeSwitchCase(self, ctx:TwoDimParser.TypeSwitchCaseContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeSwitchCase.
    def exitTypeSwitchCase(self, ctx:TwoDimParser.TypeSwitchCaseContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeList.
    def enterTypeList(self, ctx:TwoDimParser.TypeListContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeList.
    def exitTypeList(self, ctx:TwoDimParser.TypeListContext):
        pass


    # Enter a parse tree produced by TwoDimParser#recvStmt.
    def enterRecvStmt(self, ctx:TwoDimParser.RecvStmtContext):
        pass

    # Exit a parse tree produced by TwoDimParser#recvStmt.
    def exitRecvStmt(self, ctx:TwoDimParser.RecvStmtContext):
        pass


    # Enter a parse tree produced by TwoDimParser#type_.
    def enterType_(self, ctx:TwoDimParser.Type_Context):
        pass

    # Exit a parse tree produced by TwoDimParser#type_.
    def exitType_(self, ctx:TwoDimParser.Type_Context):
        pass


    # Enter a parse tree produced by TwoDimParser#typeName.
    def enterTypeName(self, ctx:TwoDimParser.TypeNameContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeName.
    def exitTypeName(self, ctx:TwoDimParser.TypeNameContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeLit.
    def enterTypeLit(self, ctx:TwoDimParser.TypeLitContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeLit.
    def exitTypeLit(self, ctx:TwoDimParser.TypeLitContext):
        pass


    # Enter a parse tree produced by TwoDimParser#elementType.
    def enterElementType(self, ctx:TwoDimParser.ElementTypeContext):
        pass

    # Exit a parse tree produced by TwoDimParser#elementType.
    def exitElementType(self, ctx:TwoDimParser.ElementTypeContext):
        pass


    # Enter a parse tree produced by TwoDimParser#methodSpec.
    def enterMethodSpec(self, ctx:TwoDimParser.MethodSpecContext):
        pass

    # Exit a parse tree produced by TwoDimParser#methodSpec.
    def exitMethodSpec(self, ctx:TwoDimParser.MethodSpecContext):
        pass


    # Enter a parse tree produced by TwoDimParser#functionType.
    def enterFunctionType(self, ctx:TwoDimParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by TwoDimParser#functionType.
    def exitFunctionType(self, ctx:TwoDimParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by TwoDimParser#signature.
    def enterSignature(self, ctx:TwoDimParser.SignatureContext):
        pass

    # Exit a parse tree produced by TwoDimParser#signature.
    def exitSignature(self, ctx:TwoDimParser.SignatureContext):
        pass


    # Enter a parse tree produced by TwoDimParser#result.
    def enterResult(self, ctx:TwoDimParser.ResultContext):
        pass

    # Exit a parse tree produced by TwoDimParser#result.
    def exitResult(self, ctx:TwoDimParser.ResultContext):
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


    # Enter a parse tree produced by TwoDimParser#unaryExpr.
    def enterUnaryExpr(self, ctx:TwoDimParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by TwoDimParser#unaryExpr.
    def exitUnaryExpr(self, ctx:TwoDimParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by TwoDimParser#conversion.
    def enterConversion(self, ctx:TwoDimParser.ConversionContext):
        pass

    # Exit a parse tree produced by TwoDimParser#conversion.
    def exitConversion(self, ctx:TwoDimParser.ConversionContext):
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


    # Enter a parse tree produced by TwoDimParser#qualifiedIdent.
    def enterQualifiedIdent(self, ctx:TwoDimParser.QualifiedIdentContext):
        pass

    # Exit a parse tree produced by TwoDimParser#qualifiedIdent.
    def exitQualifiedIdent(self, ctx:TwoDimParser.QualifiedIdentContext):
        pass


    # Enter a parse tree produced by TwoDimParser#compositeLit.
    def enterCompositeLit(self, ctx:TwoDimParser.CompositeLitContext):
        pass

    # Exit a parse tree produced by TwoDimParser#compositeLit.
    def exitCompositeLit(self, ctx:TwoDimParser.CompositeLitContext):
        pass


    # Enter a parse tree produced by TwoDimParser#literalType.
    def enterLiteralType(self, ctx:TwoDimParser.LiteralTypeContext):
        pass

    # Exit a parse tree produced by TwoDimParser#literalType.
    def exitLiteralType(self, ctx:TwoDimParser.LiteralTypeContext):
        pass


    # Enter a parse tree produced by TwoDimParser#literalValue.
    def enterLiteralValue(self, ctx:TwoDimParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by TwoDimParser#literalValue.
    def exitLiteralValue(self, ctx:TwoDimParser.LiteralValueContext):
        pass


    # Enter a parse tree produced by TwoDimParser#elementList.
    def enterElementList(self, ctx:TwoDimParser.ElementListContext):
        pass

    # Exit a parse tree produced by TwoDimParser#elementList.
    def exitElementList(self, ctx:TwoDimParser.ElementListContext):
        pass


    # Enter a parse tree produced by TwoDimParser#keyedElement.
    def enterKeyedElement(self, ctx:TwoDimParser.KeyedElementContext):
        pass

    # Exit a parse tree produced by TwoDimParser#keyedElement.
    def exitKeyedElement(self, ctx:TwoDimParser.KeyedElementContext):
        pass


    # Enter a parse tree produced by TwoDimParser#key.
    def enterKey(self, ctx:TwoDimParser.KeyContext):
        pass

    # Exit a parse tree produced by TwoDimParser#key.
    def exitKey(self, ctx:TwoDimParser.KeyContext):
        pass


    # Enter a parse tree produced by TwoDimParser#element.
    def enterElement(self, ctx:TwoDimParser.ElementContext):
        pass

    # Exit a parse tree produced by TwoDimParser#element.
    def exitElement(self, ctx:TwoDimParser.ElementContext):
        pass


    # Enter a parse tree produced by TwoDimParser#fieldDecl.
    def enterFieldDecl(self, ctx:TwoDimParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by TwoDimParser#fieldDecl.
    def exitFieldDecl(self, ctx:TwoDimParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by TwoDimParser#string_.
    def enterString_(self, ctx:TwoDimParser.String_Context):
        pass

    # Exit a parse tree produced by TwoDimParser#string_.
    def exitString_(self, ctx:TwoDimParser.String_Context):
        pass


    # Enter a parse tree produced by TwoDimParser#anonymousField.
    def enterAnonymousField(self, ctx:TwoDimParser.AnonymousFieldContext):
        pass

    # Exit a parse tree produced by TwoDimParser#anonymousField.
    def exitAnonymousField(self, ctx:TwoDimParser.AnonymousFieldContext):
        pass


    # Enter a parse tree produced by TwoDimParser#functionLit.
    def enterFunctionLit(self, ctx:TwoDimParser.FunctionLitContext):
        pass

    # Exit a parse tree produced by TwoDimParser#functionLit.
    def exitFunctionLit(self, ctx:TwoDimParser.FunctionLitContext):
        pass


    # Enter a parse tree produced by TwoDimParser#index.
    def enterIndex(self, ctx:TwoDimParser.IndexContext):
        pass

    # Exit a parse tree produced by TwoDimParser#index.
    def exitIndex(self, ctx:TwoDimParser.IndexContext):
        pass


    # Enter a parse tree produced by TwoDimParser#typeAssertion.
    def enterTypeAssertion(self, ctx:TwoDimParser.TypeAssertionContext):
        pass

    # Exit a parse tree produced by TwoDimParser#typeAssertion.
    def exitTypeAssertion(self, ctx:TwoDimParser.TypeAssertionContext):
        pass


    # Enter a parse tree produced by TwoDimParser#arguments.
    def enterArguments(self, ctx:TwoDimParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by TwoDimParser#arguments.
    def exitArguments(self, ctx:TwoDimParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by TwoDimParser#methodExpr.
    def enterMethodExpr(self, ctx:TwoDimParser.MethodExprContext):
        pass

    # Exit a parse tree produced by TwoDimParser#methodExpr.
    def exitMethodExpr(self, ctx:TwoDimParser.MethodExprContext):
        pass


    # Enter a parse tree produced by TwoDimParser#receiverType.
    def enterReceiverType(self, ctx:TwoDimParser.ReceiverTypeContext):
        pass

    # Exit a parse tree produced by TwoDimParser#receiverType.
    def exitReceiverType(self, ctx:TwoDimParser.ReceiverTypeContext):
        pass


    # Enter a parse tree produced by TwoDimParser#eos.
    def enterEos(self, ctx:TwoDimParser.EosContext):
        pass

    # Exit a parse tree produced by TwoDimParser#eos.
    def exitEos(self, ctx:TwoDimParser.EosContext):
        pass



del TwoDimParser