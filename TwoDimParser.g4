parser grammar TwoDimParser;

options {
    tokenVocab=TwoDimLexer;
    superClass=TwoDimParserBase;
}

sourceFile
    : viewportClause  (declaration eos)*
    ;

viewportClause
    : '#viewport' DECIMALS ' ' DECIMALS eos
    ;

declaration
    : varDecl
    ;

identifierList
    : IDENTIFIER (',' IDENTIFIER)*
    ;

// Function declarations

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
    : primitiveType_ '(' arguments ')' ('[' SIZE (',' ' '? SIZE)? ']')?
    ;

assignment
    : expressionList assign_op expressionList
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
    : 'case' expressionList
    | 'default'
    ;

type_
    : typeName
    | '(' type_ ')'
    ;

typeName
    : 'rect' | 'square' | 'circle' | 'triangle' | 'shape'
    ;

elementType
    : type_
    ;

signature
    : {noTerminatorAfterParams(1)}? parameters result
    | parameters
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
    : '{' (elementList ','?)? '}'
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
    : '(' SIZE (',' ' '? SIZE)? ')'
    ;

eos
    : ';'
    | EOF
    | {lineTerminatorAhead()}?
    | {checkPreviousTokenText("}")}?
    ;