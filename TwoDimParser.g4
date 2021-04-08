parser grammar TwoDimParser;

options {
    tokenVocab=TwoDimLexer;
    superClass=TwoDimParserBase;
}

sourceFile
    : viewportClause  (declaration eos)* drawClause eos
    ;

viewportClause
    : VIEWPORT WS DECIMALS WS DECIMALS eos
    ;

declaration
    : varDecl
    ;

identifierList
    : IDENTIFIER (',' IDENTIFIER)*
    ;

// Function declarations

drawClause
    : DRAW IDENTIFIER
    ;

varDecl
    : (varSpec | '(' (varSpec eos)* ')')
    ;

varSpec
    : type_ identifierList '=' declStmt
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
    ;

expressionStmt
    : expression
    ;

declStmt
    : type_ L_PAREN arguments R_PAREN (L_BRACKET SIZE (COMMA WS? SIZE)? R_BRACKET)?
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

type_
    : typeName
    | '(' type_ ')'
    ;

typeName
    : RECT 
    | SQUARE 
    | CIRCLE 
    | TRIANGLE 
    | SHAPE
    ;

elementType
    : type_
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
    ;

literal
    : basicLit
    | compositeLit
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

compositeLit
    : literalType literalValue
    ;

literalType
    : elementType
    ;

literalValue
    : '{' (element)? '}'
    ;

element
    : expression
    | literalValue
    ;

string_
    : RAW_STRING_LIT
    | INTERPRETED_STRING_LIT
    ;

arguments
    : L_PAREN SIZE (COMMA WS? SIZE)? R_PAREN
    ;

eos
    : ';'
    | EOF
    | {lineTerminatorAhead()}?
    | {checkPreviousTokenText("}")}?
    ;