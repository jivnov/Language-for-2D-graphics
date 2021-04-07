lexer grammar TwoDimLexer;

// Keywords

FUNC                   : 'func';
SWITCH                 : 'switch';
CASE                   : 'case';
DEFAULT                : 'default';
IF                     : 'if';
ELSE                   : 'else';
TYPE                   : 'type';
PACKAGE                : 'package';
IMPORT                 : 'import';

NIL_LIT                : 'nil';

IDENTIFIER             : [_\p{L}] [_\p{L}\p{Nd}]*;  // L - "Letter" (any case); Nd - "Number Decimal" (see unicode reference in README)

// TwoDim specific keywords:
DRAW                   : 'draw';

// -- Same layer relations
LEFT                   : 'left';
RIGHT                  : 'right';
TOP                    : 'top';
BOT                    : 'bot';
OUTER                  : 'outer';
INNER                  : 'inner';

// -- Multi-layer relations
ON                     : 'on';
UNDER                  : 'under';
IN                     : 'in';



// Punctuation

L_PAREN                : '(';
R_PAREN                : ')';
L_CURLY                : '{';
R_CURLY                : '}';
L_BRACKET              : '[';
R_BRACKET              : ']';
ASSIGN                 : '=';
COMMA                  : ',';
SEMI                   : ';';
COLON                  : ':';
DOT                    : '.';
PLUS_PLUS              : '++';
MINUS_MINUS            : '--';

// Logical

LOGICAL_OR             : 'or';
LOGICAL_AND            : 'and';

// Relation operators

EQUALS                 : '==';
NOT_EQUALS             : '!=';
LESS                   : '<';
LESS_OR_EQUALS         : '<=';
GREATER                : '>';
GREATER_OR_EQUALS      : '>=';

// Arithmetic operators

OR                     : '|';
DIV                    : '/';
MOD                    : '%';
LSHIFT                 : '<<';
RSHIFT                 : '>>';
BIT_CLEAR              : '&^';

// Unary operators

EXCLAMATION            : '!';

// Mixed operators

PLUS                   : '+';
MINUS                  : '-';
CARET                  : '^';
STAR                   : '*';
AMPERSAND              : '&';

// Number literals

DECIMAL_LIT            : [1-9] [0-9]*;

FLOAT_LIT              : DECIMALS ('.' DECIMALS? EXPONENT? | EXPONENT)
                       | '.' DECIMALS EXPONENT?
                       ;


// Rune literals

RUNE_LIT               : '\'' (~[\n\\] | ESCAPED_VALUE) '\'';

// String literals

RAW_STRING_LIT         : '`' ~'`'*                      '`';
INTERPRETED_STRING_LIT : '"' (~["\\] | ESCAPED_VALUE)*  '"';
// Hidden tokens
WS                     : [ \t]+             -> channel(HIDDEN);
COMMENT                : '/*' .*? '*/'      -> channel(HIDDEN);
TERMINATOR             : [\r\n]+            -> channel(HIDDEN);
LINE_COMMENT           : '//' ~[\r\n]*      -> channel(HIDDEN);

// Fragments

fragment ESCAPED_VALUE
    : '\\' [abfnrtv\\'"]
    ;

fragment DECIMALS
    : [0-9]+
    ;

fragment EXPONENT
    : [eE] [+-]? DECIMALS
    ;