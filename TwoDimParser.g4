parser grammar TwoDimParser;

options {
    tokenVocab=TwoDimLexer;
    superClass=TwoDimParserBase;
}

sourceFile
    : packageClause eos (importDecl eos)* ((functionDecl | methodDecl | declaration) eos)*
    ;

packageClause
    : 'package' IDENTIFIER
    ;

importDecl
    : 'import' (importSpec | '(' (importSpec eos)* ')')
    ;

importSpec
    : ('.' | IDENTIFIER)? importPath
    ;

importPath
    : string_
    ;

declaration
    : typeDecl
    | varDecl
    ;

identifierList
    : IDENTIFIER (',' IDENTIFIER)*
    ;

expressionList
    : expression (',' expression)*
    ;

typeDecl
    : 'type' (typeSpec | '(' (typeSpec eos)* ')')
    ;

typeSpec
    : IDENTIFIER ASSIGN? type_
    ;

// Function declarations

functionDecl
    : 'func' IDENTIFIER (signature block?)
    ;

methodDecl
    : 'func' receiver IDENTIFIER (signature block?)
    ;

receiver
    : parameters
    ;

varDecl
    : (varSpec | '(' (varSpec eos)* ')')
    ;

varSpec
    : type_ identifierList '=' expressionList
    ;

block
    : '{' statementList? '}'
    ;

statementList
    : (statement eos)+
    ;

statement
    : declaration
    | labeledStmt
    | simpleStmt
    | block
    | ifStmt
    | switchStmt
    ;

simpleStmt
    : expressionStmt
    | incDecStmt
    | assignment
    | emptyStmt
    ;

expressionStmt
    : expression
    ;

incDecStmt
    : expression (PLUS_PLUS | MINUS_MINUS)
    ;

assignment
    : expressionList assign_op expressionList
    ;

assign_op
    : ('+' | '-')? '='
    ;

emptyStmt
    : ';'
    ;

labeledStmt
    : IDENTIFIER ':' statement
    ;

ifStmt
    : 'if' (simpleStmt ';')? expression block ('else' (ifStmt | block))?
    ;

switchStmt
    : exprSwitchStmt
    | typeSwitchStmt
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

typeSwitchStmt
    : 'switch' (simpleStmt ';')? typeSwitchGuard '{' typeCaseClause* '}'
    ;

typeSwitchGuard
    : primaryExpr '.' '(' 'type' ')'
    ;

typeCaseClause
    : typeSwitchCase ':' statementList?
    ;

typeSwitchCase
    : 'case' typeList
    | 'default'
    ;

typeList
    : (type_ | NIL_LIT) (',' (type_ | NIL_LIT))*
    ;

recvStmt
    : (expressionList '=')? expression
    ;

type_
    : typeName
    | typeLit
    | '(' type_ ')'
    ;

typeName
    : IDENTIFIER
    | qualifiedIdent
    ;

typeLit
    : functionType
    ;

elementType
    : type_
    ;

methodSpec
    : {noTerminatorAfterParams(2)}? IDENTIFIER parameters result
    | typeName
    | IDENTIFIER parameters
    ;

functionType
    : 'func' signature
    ;

signature
    : {noTerminatorAfterParams(1)}? parameters result
    | parameters
    ;

result
    : parameters
    | type_
    ;

parameters
    : '(' (parameterDecl (COMMA parameterDecl)* COMMA?)? ')'
    ;

parameterDecl
    : identifierList? type_
    ;

expression
    : primaryExpr
    | unaryExpr
    | expression ('*' | '/' | '%' | '<<' | '>>' | '&' | '&^') expression
    | expression ('+' | '-' | '|' | '^') expression
    | expression ('==' | '!=' | '<' | '<=' | '>' | '>=') expression
    | expression 'and' expression
    | expression 'or' expression
    ;

primaryExpr
    : operand
    | conversion
    | primaryExpr ( DOT IDENTIFIER
                  | index
                  | typeAssertion
                  | arguments)
    ;

unaryExpr
    : primaryExpr
    | ('+' | '-' | '!' | '^' | '*' | '&') expression
    ;

conversion
    : type_ '(' expression ','? ')'
    ;

operand
    : literal
    | operandName
    | methodExpr
    | '(' expression ')'
    ;

literal
    : basicLit
    | compositeLit
    | functionLit
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
    | qualifiedIdent
    ;

qualifiedIdent
    : IDENTIFIER '.' IDENTIFIER
    ;

compositeLit
    : literalType literalValue
    ;

literalType
    : '[' ']' elementType
    | typeName
    ;

literalValue
    : '{' (elementList ','?)? '}'
    ;

elementList
    : keyedElement (',' keyedElement)*
    ;

keyedElement
    : (key ':')? element
    ;

key
    : IDENTIFIER
    | expression
    | literalValue
    ;

element
    : expression
    | literalValue
    ;

fieldDecl
    : ({noTerminatorBetween(2)}? identifierList type_ | anonymousField) string_?
    ;

string_
    : RAW_STRING_LIT
    | INTERPRETED_STRING_LIT
    ;

anonymousField
    : '*'? typeName
    ;

functionLit
    : 'func' signature block // function
    ;

index
    : '[' expression ']'
    ;

typeAssertion
    : '.' '(' type_ ')'
    ;

arguments
    : '(' ((expressionList | type_ (',' expressionList)?) ','?)? ')'
    ;

methodExpr
    : receiverType DOT IDENTIFIER
    ;

receiverType
    : typeName
    | '(' ('*' typeName | receiverType) ')'
    ;

eos
    : ';'
    | EOF
    | {lineTerminatorAhead()}?
    | {checkPreviousTokenText("}")}?
    ;