parser grammar TwoDimParser;

options {
    tokenVocab=TwoDimLexer;
    superClass=TwoDimParserBase;
}

sourceFile
    : viewportClause? ((functionDecl | declaration) eos)* statementList? drawClause eos
    ;

viewportClause
    : VIEWPORT DECIMAL_LIT DECIMAL_LIT eos
    ;

declaration
    : shapeDecl
    ;

identifierList
    : IDENTIFIER (',' IDENTIFIER)*
    ;

expressionList
    : expression (',' expression)*
    ;

// Function declarations
functionDecl
    : FUNC IDENTIFIER (signature block?)
    ;

signature
    : {self.noTerminatorAfterParams(1)}? parameters
    | parameters
    ;

parameters
    : '(' (parameterDecl (COMMA parameterDecl)*)? ')'
    ;

parameterDecl
    : typeName identifierList?
    ;

functionCall
    : IDENTIFIER WS? L_PAREN WS? operandName? (COMMA WS? operandName)* R_PAREN
    ;

drawClause
    : DRAW IDENTIFIER
    ;

shapeDecl
    : shapeSpec
    ;

shapeSpec
    : typeName IDENTIFIER WS? shapeArguments shapeColor? (',' WS? IDENTIFIER shapeArguments shapeColor?)*  // e.x. 'square A(20%) [15%], B(30%) [15%]'
    ;

shapeColor
    : '<' DECIMAL_LIT (',' WS? DECIMAL_LIT)* '>'
    ;

block
    : '{' TERMINATOR? statementList? '}'
    ;

statementList
    : (statement eos)+
    ;

statement
    : declaration
    | functionDecl
    | functionCall
    | simpleStmt
    | ifStmt
    | switchStmt
    | assignmentDeclarationStmt
    ;

simpleStmt
    : expressionStmt
    | assignment
    | drawClause
    ;

expressionStmt
    : expression
    ;

shapeArguments
    : arguments? WS? (L_BRACKET WS? SIZE_LIT (COMMA WS? SIZE_LIT)? WS? R_BRACKET)?
    ;

assignmentDeclarationStmt
    : SHAPE IDENTIFIER WS? shapeArguments WS? assign_op WS? functionCall
    ;

assignment
    : IDENTIFIER assign_op expression
    ;

assign_op
    : '='
    ;

ifStmt
    : 'if' (simpleStmt ';')? expression block ('else' (ifStmt | block))?
    ;

switchStmt
    : exprSwitchStmt
    ;

exprSwitchStmt
    : 'switch' (simpleStmt ';')? expression? '{' exprCaseClause* '}'
    ;

exprCaseClause
    : exprSwitchCase ':' statementList?
    ;

exprSwitchCase
    : 'case' expression
    | 'default'
    ;

typeName
    : RECT 
    | SQUARE 
    | CIRCLE 
    | TRIANGLE 
    | SHAPE
    ;

relationDetailOp
    : INNER
    | OUTER
    ;

singleLevelRelationOp
    : LEFT
    | RIGHT
    | TOP
    | BOT
    ;

multiLevelRelationOp
    : IN
    | ON
    | UNDER
    ;

relationExpr
    : primaryExpr (singleLevelRelationOp relationDetailOp? primaryExpr)+
    | primaryExpr multiLevelRelationOp primaryExpr
    ;

expression
    : primaryExpr
    | relationExpr
    | primaryExpr ('+' | '-') primaryExpr
    | functionCall
    ;

primaryExpr
    : operand
    ;

operand
    : literal
    | operandName
    | '(' expression ')'
    ;

literal
    : basicLit
    ;

basicLit
    : NIL_LIT
    | integer
    | string_
    | FLOAT_LIT
    | RUNE_LIT
    ;

integer
    : DECIMAL_LIT
    | RUNE_LIT
    ;

operandName
    : IDENTIFIER
    ;

string_
    : RAW_STRING_LIT
    | INTERPRETED_STRING_LIT
    ;

arguments
    : '{' WS* (expressionList)? WS* '}'
    ;

eos
    : ';'
    | ';' EOF
    | {self.checkPreviousTokenText("}")}?
    ;