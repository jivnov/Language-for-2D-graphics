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
    : 'func' IDENTIFIER (signature block?)
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

drawClause
    : DRAW IDENTIFIER
    ;

shapeDecl
    : shapeSpec
    ;

shapeSpec
    : typeName IDENTIFIER WS? shapeArguments (',' WS? IDENTIFIER shapeArguments)*  // e.x. 'square A(20%) [15%], B(30%) [15%]'
    ;

block
    : '{' statementList? '}'
    ;

statementList
    : (statement eos)+
    ;

statement
    : declaration
    | simpleStmt
    | block
    | ifStmt
    | switchStmt
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

expression
    : primaryExpr
    | primaryExpr (LEFT | RIGHT | TOP | BOT) (INNER | OUTER)? primaryExpr
    | primaryExpr (IN | ON | UNDER) primaryExpr
    | primaryExpr ('+' | '-') primaryExpr
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
    : '(' (expressionList)? ')'
    ;

eos
    : ';'
    | ';' EOF
    | {self.lineTerminatorAhead()}?
    | {self.checkPreviousTokenText("}")}?
    ;