# Generated from TwoDimParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if __name__ is not None and "." in __name__:
    from .TwoDimParserBase import TwoDimParserBase
else:
    from TwoDimParserBase import TwoDimParserBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u012d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\3\2\3\2\3\2\3\2\7\2Q\n\2\f\2\16\2T\13\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5b\n\5\f\5\16\5")
        buf.write("e\13\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7o\n\7\f\7\16")
        buf.write("\7r\13\7\3\7\5\7u\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("~\n\t\3\t\3\t\3\n\3\n\3\n\6\n\u0085\n\n\r\n\16\n\u0086")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u008e\n\13\3\f\3\f\5\f")
        buf.write("\u0092\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u009e\n\16\3\16\5\16\u00a1\n\16\3\16\5\16\u00a4")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00b0\n\21\3\21\3\21\3\21\3\21\3\21\5\21\u00b7\n")
        buf.write("\21\5\21\u00b9\n\21\3\22\3\22\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00c1\n\23\3\23\5\23\u00c4\n\23\3\23\3\23\7\23\u00c8")
        buf.write("\n\23\f\23\16\23\u00cb\13\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\5\24\u00d2\n\24\3\25\3\25\3\25\5\25\u00d7\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u00de\n\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u00e8\n\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00f4\n\31\3\32")
        buf.write("\3\32\3\33\3\33\5\33\u00fa\n\33\3\34\3\34\5\34\u00fe\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\5\35\u0105\n\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\5\"\u0112\n\"\3\"\3")
        buf.write("\"\3#\3#\5#\u0118\n#\3$\3$\3%\3%\3%\3%\5%\u0120\n%\3%")
        buf.write("\5%\u0123\n%\3%\3%\3&\3&\3&\3&\5&\u012b\n&\3&\2\2\'\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJ\2\t\3\2\16\22\3\2\25\30\3\2\31\32\3\2\33")
        buf.write("\35\3\2:;\4\2??AA\3\2BC\2\u012f\2L\3\2\2\2\4U\3\2\2\2")
        buf.write("\6\\\3\2\2\2\b^\3\2\2\2\nf\3\2\2\2\ft\3\2\2\2\16v\3\2")
        buf.write("\2\2\20{\3\2\2\2\22\u0084\3\2\2\2\24\u008d\3\2\2\2\26")
        buf.write("\u0091\3\2\2\2\30\u0093\3\2\2\2\32\u0095\3\2\2\2\34\u00a5")
        buf.write("\3\2\2\2\36\u00a9\3\2\2\2 \u00ab\3\2\2\2\"\u00ba\3\2\2")
        buf.write("\2$\u00bc\3\2\2\2&\u00ce\3\2\2\2(\u00d6\3\2\2\2*\u00dd")
        buf.write("\3\2\2\2,\u00df\3\2\2\2.\u00e1\3\2\2\2\60\u00f3\3\2\2")
        buf.write("\2\62\u00f5\3\2\2\2\64\u00f9\3\2\2\2\66\u00fd\3\2\2\2")
        buf.write("8\u0104\3\2\2\2:\u0106\3\2\2\2<\u0108\3\2\2\2>\u010a\3")
        buf.write("\2\2\2@\u010d\3\2\2\2B\u010f\3\2\2\2D\u0117\3\2\2\2F\u0119")
        buf.write("\3\2\2\2H\u011b\3\2\2\2J\u012a\3\2\2\2LR\5\4\3\2MN\5\6")
        buf.write("\4\2NO\5J&\2OQ\3\2\2\2PM\3\2\2\2QT\3\2\2\2RP\3\2\2\2R")
        buf.write("S\3\2\2\2S\3\3\2\2\2TR\3\2\2\2UV\7\24\2\2VW\7D\2\2WX\7")
        buf.write("H\2\2XY\7D\2\2YZ\7H\2\2Z[\5J&\2[\5\3\2\2\2\\]\5\f\7\2")
        buf.write("]\7\3\2\2\2^c\7\r\2\2_`\7%\2\2`b\7\r\2\2a_\3\2\2\2be\3")
        buf.write("\2\2\2ca\3\2\2\2cd\3\2\2\2d\t\3\2\2\2ec\3\2\2\2fg\7\23")
        buf.write("\2\2gh\7\r\2\2h\13\3\2\2\2iu\5\16\b\2jp\7\36\2\2kl\5\16")
        buf.write("\b\2lm\5J&\2mo\3\2\2\2nk\3\2\2\2or\3\2\2\2pn\3\2\2\2p")
        buf.write("q\3\2\2\2qs\3\2\2\2rp\3\2\2\2su\7\37\2\2ti\3\2\2\2tj\3")
        buf.write("\2\2\2u\r\3\2\2\2vw\5*\26\2wx\5\b\5\2xy\7$\2\2yz\5\32")
        buf.write("\16\2z\17\3\2\2\2{}\7 \2\2|~\5\22\n\2}|\3\2\2\2}~\3\2")
        buf.write("\2\2~\177\3\2\2\2\177\u0080\7!\2\2\u0080\21\3\2\2\2\u0081")
        buf.write("\u0082\5\24\13\2\u0082\u0083\5J&\2\u0083\u0085\3\2\2\2")
        buf.write("\u0084\u0081\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3")
        buf.write("\2\2\2\u0086\u0087\3\2\2\2\u0087\23\3\2\2\2\u0088\u008e")
        buf.write("\5\6\4\2\u0089\u008e\5\26\f\2\u008a\u008e\5\20\t\2\u008b")
        buf.write("\u008e\5 \21\2\u008c\u008e\5\"\22\2\u008d\u0088\3\2\2")
        buf.write("\2\u008d\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\25\3\2\2\2\u008f\u0092")
        buf.write("\5\30\r\2\u0090\u0092\5\34\17\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\27\3\2\2\2\u0093\u0094\5\60\31\2")
        buf.write("\u0094\31\3\2\2\2\u0095\u0096\5*\26\2\u0096\u0097\7\36")
        buf.write("\2\2\u0097\u0098\5H%\2\u0098\u00a3\7\37\2\2\u0099\u009a")
        buf.write("\7\"\2\2\u009a\u00a0\7I\2\2\u009b\u009d\7%\2\2\u009c\u009e")
        buf.write("\7D\2\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\7I\2\2\u00a0\u009b\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\7")
        buf.write("#\2\2\u00a3\u0099\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\33")
        buf.write("\3\2\2\2\u00a5\u00a6\7\r\2\2\u00a6\u00a7\5\36\20\2\u00a7")
        buf.write("\u00a8\5\60\31\2\u00a8\35\3\2\2\2\u00a9\u00aa\7$\2\2\u00aa")
        buf.write("\37\3\2\2\2\u00ab\u00af\7\7\2\2\u00ac\u00ad\5\26\f\2\u00ad")
        buf.write("\u00ae\7&\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ac\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\5")
        buf.write("\60\31\2\u00b2\u00b8\5\20\t\2\u00b3\u00b6\7\b\2\2\u00b4")
        buf.write("\u00b7\5 \21\2\u00b5\u00b7\5\20\t\2\u00b6\u00b4\3\2\2")
        buf.write("\2\u00b6\u00b5\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b3")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9!\3\2\2\2\u00ba\u00bb")
        buf.write("\5$\23\2\u00bb#\3\2\2\2\u00bc\u00c0\7\4\2\2\u00bd\u00be")
        buf.write("\5\26\f\2\u00be\u00bf\7&\2\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("\u00bd\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c4\5\60\31\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c9\7 \2\2\u00c6")
        buf.write("\u00c8\5&\24\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\7!\2\2\u00cd%\3")
        buf.write("\2\2\2\u00ce\u00cf\5(\25\2\u00cf\u00d1\7\'\2\2\u00d0\u00d2")
        buf.write("\5\22\n\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\'\3\2\2\2\u00d3\u00d4\7\5\2\2\u00d4\u00d7\5\60\31\2\u00d5")
        buf.write("\u00d7\7\6\2\2\u00d6\u00d3\3\2\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7)\3\2\2\2\u00d8\u00de\5,\27\2\u00d9\u00da\7\36\2")
        buf.write("\2\u00da\u00db\5*\26\2\u00db\u00dc\7\37\2\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00d8\3\2\2\2\u00dd\u00d9\3\2\2\2\u00de")
        buf.write("+\3\2\2\2\u00df\u00e0\t\2\2\2\u00e0-\3\2\2\2\u00e1\u00e2")
        buf.write("\5*\26\2\u00e2/\3\2\2\2\u00e3\u00f4\5\62\32\2\u00e4\u00e5")
        buf.write("\5\62\32\2\u00e5\u00e7\t\3\2\2\u00e6\u00e8\t\4\2\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\u00ea\5\62\32\2\u00ea\u00f4\3\2\2\2\u00eb\u00ec")
        buf.write("\5\62\32\2\u00ec\u00ed\t\5\2\2\u00ed\u00ee\5\62\32\2\u00ee")
        buf.write("\u00f4\3\2\2\2\u00ef\u00f0\5\62\32\2\u00f0\u00f1\t\6\2")
        buf.write("\2\u00f1\u00f2\5\62\32\2\u00f2\u00f4\3\2\2\2\u00f3\u00e3")
        buf.write("\3\2\2\2\u00f3\u00e4\3\2\2\2\u00f3\u00eb\3\2\2\2\u00f3")
        buf.write("\u00ef\3\2\2\2\u00f4\61\3\2\2\2\u00f5\u00f6\5\64\33\2")
        buf.write("\u00f6\63\3\2\2\2\u00f7\u00fa\5\66\34\2\u00f8\u00fa\5")
        buf.write("<\37\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\65")
        buf.write("\3\2\2\2\u00fb\u00fe\58\35\2\u00fc\u00fe\5> \2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\67\3\2\2\2\u00ff\u0105")
        buf.write("\7\f\2\2\u0100\u0105\5:\36\2\u0101\u0105\5F$\2\u0102\u0105")
        buf.write("\7@\2\2\u0103\u0105\7A\2\2\u0104\u00ff\3\2\2\2\u0104\u0100")
        buf.write("\3\2\2\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u01059\3\2\2\2\u0106\u0107\t\7\2\2\u0107")
        buf.write(";\3\2\2\2\u0108\u0109\7\r\2\2\u0109=\3\2\2\2\u010a\u010b")
        buf.write("\5@!\2\u010b\u010c\5B\"\2\u010c?\3\2\2\2\u010d\u010e\5")
        buf.write(".\30\2\u010eA\3\2\2\2\u010f\u0111\7 \2\2\u0110\u0112\5")
        buf.write("D#\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\7!\2\2\u0114C\3\2\2\2\u0115\u0118")
        buf.write("\5\60\31\2\u0116\u0118\5B\"\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118E\3\2\2\2\u0119\u011a\t\b\2\2\u011a")
        buf.write("G\3\2\2\2\u011b\u011c\7\36\2\2\u011c\u0122\7I\2\2\u011d")
        buf.write("\u011f\7%\2\2\u011e\u0120\7D\2\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\7I\2\2")
        buf.write("\u0122\u011d\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3")
        buf.write("\2\2\2\u0124\u0125\7\37\2\2\u0125I\3\2\2\2\u0126\u012b")
        buf.write("\7&\2\2\u0127\u012b\7\2\2\3\u0128\u012b\6&\2\2\u0129\u012b")
        buf.write("\6&\3\2\u012a\u0126\3\2\2\2\u012a\u0127\3\2\2\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012bK\3\2\2\2 Rcp")
        buf.write("t}\u0086\u008d\u0091\u009d\u00a0\u00a3\u00af\u00b6\u00b8")
        buf.write("\u00c0\u00c3\u00c9\u00d1\u00d6\u00dd\u00e7\u00f3\u00f9")
        buf.write("\u00fd\u0104\u0111\u0117\u011f\u0122\u012a")
        return buf.getvalue()


class TwoDimParser ( TwoDimParserBase ):

    grammarFileName = "TwoDimParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'switch'", "'case'", "'default'", 
                     "'if'", "'else'", "'type'", "'package'", "'import'", 
                     "'nil'", "<INVALID>", "'square'", "'rect'", "'circle'", 
                     "'triangle'", "'shape'", "'draw'", "'#viewport'", "'left'", 
                     "'right'", "'top'", "'bot'", "'outer'", "'inner'", 
                     "'on'", "'under'", "'in'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'='", "','", "';'", "':'", "'.'", "'++'", 
                     "'--'", "'or'", "'and'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'|'", "'/'", "'%'", "'<<'", "'>>'", 
                     "'&^'", "'!'", "'+'", "'-'", "'^'", "'*'", "'&'" ]

    symbolicNames = [ "<INVALID>", "FUNC", "SWITCH", "CASE", "DEFAULT", 
                      "IF", "ELSE", "TYPE", "PACKAGE", "IMPORT", "NIL_LIT", 
                      "IDENTIFIER", "SQUARE", "RECT", "CIRCLE", "TRIANGLE", 
                      "SHAPE", "DRAW", "VIEWPORT", "LEFT", "RIGHT", "TOP", 
                      "BOT", "OUTER", "INNER", "ON", "UNDER", "IN", "L_PAREN", 
                      "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", 
                      "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", "PLUS_PLUS", 
                      "MINUS_MINUS", "LOGICAL_OR", "LOGICAL_AND", "EQUALS", 
                      "NOT_EQUALS", "LESS", "LESS_OR_EQUALS", "GREATER", 
                      "GREATER_OR_EQUALS", "OR", "DIV", "MOD", "LSHIFT", 
                      "RSHIFT", "BIT_CLEAR", "EXCLAMATION", "PLUS", "MINUS", 
                      "CARET", "STAR", "AMPERSAND", "DECIMAL_LIT", "FLOAT_LIT", 
                      "RUNE_LIT", "RAW_STRING_LIT", "INTERPRETED_STRING_LIT", 
                      "WS", "COMMENT", "TERMINATOR", "LINE_COMMENT", "DECIMALS", 
                      "SIZE" ]

    RULE_sourceFile = 0
    RULE_viewportClause = 1
    RULE_declaration = 2
    RULE_identifierList = 3
    RULE_drawClause = 4
    RULE_varDecl = 5
    RULE_varSpec = 6
    RULE_block = 7
    RULE_statementList = 8
    RULE_statement = 9
    RULE_simpleStmt = 10
    RULE_expressionStmt = 11
    RULE_declStmt = 12
    RULE_assignment = 13
    RULE_assign_op = 14
    RULE_ifStmt = 15
    RULE_switchStmt = 16
    RULE_exprSwitchStmt = 17
    RULE_exprCaseClause = 18
    RULE_exprSwitchCase = 19
    RULE_type_ = 20
    RULE_typeName = 21
    RULE_elementType = 22
    RULE_expression = 23
    RULE_primaryExpr = 24
    RULE_operand = 25
    RULE_literal = 26
    RULE_basicLit = 27
    RULE_integer = 28
    RULE_operandName = 29
    RULE_compositeLit = 30
    RULE_literalType = 31
    RULE_literalValue = 32
    RULE_element = 33
    RULE_string_ = 34
    RULE_arguments = 35
    RULE_eos = 36

    ruleNames =  [ "sourceFile", "viewportClause", "declaration", "identifierList", 
                   "drawClause", "varDecl", "varSpec", "block", "statementList", 
                   "statement", "simpleStmt", "expressionStmt", "declStmt", 
                   "assignment", "assign_op", "ifStmt", "switchStmt", "exprSwitchStmt", 
                   "exprCaseClause", "exprSwitchCase", "type_", "typeName", 
                   "elementType", "expression", "primaryExpr", "operand", 
                   "literal", "basicLit", "integer", "operandName", "compositeLit", 
                   "literalType", "literalValue", "element", "string_", 
                   "arguments", "eos" ]

    EOF = Token.EOF
    FUNC=1
    SWITCH=2
    CASE=3
    DEFAULT=4
    IF=5
    ELSE=6
    TYPE=7
    PACKAGE=8
    IMPORT=9
    NIL_LIT=10
    IDENTIFIER=11
    SQUARE=12
    RECT=13
    CIRCLE=14
    TRIANGLE=15
    SHAPE=16
    DRAW=17
    VIEWPORT=18
    LEFT=19
    RIGHT=20
    TOP=21
    BOT=22
    OUTER=23
    INNER=24
    ON=25
    UNDER=26
    IN=27
    L_PAREN=28
    R_PAREN=29
    L_CURLY=30
    R_CURLY=31
    L_BRACKET=32
    R_BRACKET=33
    ASSIGN=34
    COMMA=35
    SEMI=36
    COLON=37
    DOT=38
    PLUS_PLUS=39
    MINUS_MINUS=40
    LOGICAL_OR=41
    LOGICAL_AND=42
    EQUALS=43
    NOT_EQUALS=44
    LESS=45
    LESS_OR_EQUALS=46
    GREATER=47
    GREATER_OR_EQUALS=48
    OR=49
    DIV=50
    MOD=51
    LSHIFT=52
    RSHIFT=53
    BIT_CLEAR=54
    EXCLAMATION=55
    PLUS=56
    MINUS=57
    CARET=58
    STAR=59
    AMPERSAND=60
    DECIMAL_LIT=61
    FLOAT_LIT=62
    RUNE_LIT=63
    RAW_STRING_LIT=64
    INTERPRETED_STRING_LIT=65
    WS=66
    COMMENT=67
    TERMINATOR=68
    LINE_COMMENT=69
    DECIMALS=70
    SIZE=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def viewportClause(self):
            return self.getTypedRuleContext(TwoDimParser.ViewportClauseContext,0)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.DeclarationContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.EosContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.EosContext,i)


        def getRuleIndex(self):
            return TwoDimParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)




    def sourceFile(self):

        localctx = TwoDimParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.viewportClause()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE) | (1 << TwoDimParser.L_PAREN))) != 0):
                self.state = 75
                self.declaration()
                self.state = 76
                self.eos()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ViewportClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIEWPORT(self):
            return self.getToken(TwoDimParser.VIEWPORT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.WS)
            else:
                return self.getToken(TwoDimParser.WS, i)

        def DECIMALS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.DECIMALS)
            else:
                return self.getToken(TwoDimParser.DECIMALS, i)

        def eos(self):
            return self.getTypedRuleContext(TwoDimParser.EosContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_viewportClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewportClause" ):
                listener.enterViewportClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewportClause" ):
                listener.exitViewportClause(self)




    def viewportClause(self):

        localctx = TwoDimParser.ViewportClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_viewportClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(TwoDimParser.VIEWPORT)
            self.state = 84
            self.match(TwoDimParser.WS)
            self.state = 85
            self.match(TwoDimParser.DECIMALS)
            self.state = 86
            self.match(TwoDimParser.WS)
            self.state = 87
            self.match(TwoDimParser.DECIMALS)
            self.state = 88
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(TwoDimParser.VarDeclContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = TwoDimParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.varDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.IDENTIFIER)
            else:
                return self.getToken(TwoDimParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = TwoDimParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.COMMA:
                self.state = 93
                self.match(TwoDimParser.COMMA)
                self.state = 94
                self.match(TwoDimParser.IDENTIFIER)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAW(self):
            return self.getToken(TwoDimParser.DRAW, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_drawClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawClause" ):
                listener.enterDrawClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawClause" ):
                listener.exitDrawClause(self)




    def drawClause(self):

        localctx = TwoDimParser.DrawClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_drawClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(TwoDimParser.DRAW)
            self.state = 101
            self.match(TwoDimParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.VarSpecContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.VarSpecContext,i)


        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.EosContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.EosContext,i)


        def getRuleIndex(self):
            return TwoDimParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = TwoDimParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 103
                self.varSpec()
                pass

            elif la_ == 2:
                self.state = 104
                self.match(TwoDimParser.L_PAREN)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE) | (1 << TwoDimParser.L_PAREN))) != 0):
                    self.state = 105
                    self.varSpec()
                    self.state = 106
                    self.eos()
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self.match(TwoDimParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def identifierList(self):
            return self.getTypedRuleContext(TwoDimParser.IdentifierListContext,0)


        def ASSIGN(self):
            return self.getToken(TwoDimParser.ASSIGN, 0)

        def declStmt(self):
            return self.getTypedRuleContext(TwoDimParser.DeclStmtContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_varSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarSpec" ):
                listener.enterVarSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarSpec" ):
                listener.exitVarSpec(self)




    def varSpec(self):

        localctx = TwoDimParser.VarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.type_()
            self.state = 117
            self.identifierList()
            self.state = 118
            self.match(TwoDimParser.ASSIGN)
            self.state = 119
            self.declStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(TwoDimParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(TwoDimParser.R_CURLY, 0)

        def statementList(self):
            return self.getTypedRuleContext(TwoDimParser.StatementListContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = TwoDimParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(TwoDimParser.L_CURLY)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 2)) & ~0x3f) == 0 and ((1 << (_la - 2)) & ((1 << (TwoDimParser.SWITCH - 2)) | (1 << (TwoDimParser.IF - 2)) | (1 << (TwoDimParser.NIL_LIT - 2)) | (1 << (TwoDimParser.IDENTIFIER - 2)) | (1 << (TwoDimParser.SQUARE - 2)) | (1 << (TwoDimParser.RECT - 2)) | (1 << (TwoDimParser.CIRCLE - 2)) | (1 << (TwoDimParser.TRIANGLE - 2)) | (1 << (TwoDimParser.SHAPE - 2)) | (1 << (TwoDimParser.L_PAREN - 2)) | (1 << (TwoDimParser.L_CURLY - 2)) | (1 << (TwoDimParser.DECIMAL_LIT - 2)) | (1 << (TwoDimParser.FLOAT_LIT - 2)) | (1 << (TwoDimParser.RUNE_LIT - 2)) | (1 << (TwoDimParser.RAW_STRING_LIT - 2)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 2)))) != 0):
                self.state = 122
                self.statementList()


            self.state = 125
            self.match(TwoDimParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.StatementContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.StatementContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.EosContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.EosContext,i)


        def getRuleIndex(self):
            return TwoDimParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = TwoDimParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.statement()
                self.state = 128
                self.eos()
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 2)) & ~0x3f) == 0 and ((1 << (_la - 2)) & ((1 << (TwoDimParser.SWITCH - 2)) | (1 << (TwoDimParser.IF - 2)) | (1 << (TwoDimParser.NIL_LIT - 2)) | (1 << (TwoDimParser.IDENTIFIER - 2)) | (1 << (TwoDimParser.SQUARE - 2)) | (1 << (TwoDimParser.RECT - 2)) | (1 << (TwoDimParser.CIRCLE - 2)) | (1 << (TwoDimParser.TRIANGLE - 2)) | (1 << (TwoDimParser.SHAPE - 2)) | (1 << (TwoDimParser.L_PAREN - 2)) | (1 << (TwoDimParser.L_CURLY - 2)) | (1 << (TwoDimParser.DECIMAL_LIT - 2)) | (1 << (TwoDimParser.FLOAT_LIT - 2)) | (1 << (TwoDimParser.RUNE_LIT - 2)) | (1 << (TwoDimParser.RAW_STRING_LIT - 2)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 2)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(TwoDimParser.DeclarationContext,0)


        def simpleStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SimpleStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(TwoDimParser.BlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(TwoDimParser.IfStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SwitchStmtContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TwoDimParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.simpleStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.switchStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStmt(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(TwoDimParser.AssignmentContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_simpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStmt" ):
                listener.enterSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStmt" ):
                listener.exitSimpleStmt(self)




    def simpleStmt(self):

        localctx = TwoDimParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_simpleStmt)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.expressionStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_expressionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStmt" ):
                listener.enterExpressionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStmt" ):
                listener.exitExpressionStmt(self)




    def expressionStmt(self):

        localctx = TwoDimParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(TwoDimParser.ArgumentsContext,0)


        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def L_BRACKET(self):
            return self.getToken(TwoDimParser.L_BRACKET, 0)

        def SIZE(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.SIZE)
            else:
                return self.getToken(TwoDimParser.SIZE, i)

        def R_BRACKET(self):
            return self.getToken(TwoDimParser.R_BRACKET, 0)

        def COMMA(self):
            return self.getToken(TwoDimParser.COMMA, 0)

        def WS(self):
            return self.getToken(TwoDimParser.WS, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_declStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclStmt" ):
                listener.enterDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclStmt" ):
                listener.exitDeclStmt(self)




    def declStmt(self):

        localctx = TwoDimParser.DeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.type_()
            self.state = 148
            self.match(TwoDimParser.L_PAREN)
            self.state = 149
            self.arguments()
            self.state = 150
            self.match(TwoDimParser.R_PAREN)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 151
                self.match(TwoDimParser.L_BRACKET)
                self.state = 152
                self.match(TwoDimParser.SIZE)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.COMMA:
                    self.state = 153
                    self.match(TwoDimParser.COMMA)
                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==TwoDimParser.WS:
                        self.state = 154
                        self.match(TwoDimParser.WS)


                    self.state = 157
                    self.match(TwoDimParser.SIZE)


                self.state = 160
                self.match(TwoDimParser.R_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def assign_op(self):
            return self.getTypedRuleContext(TwoDimParser.Assign_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = TwoDimParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 164
            self.assign_op()
            self.state = 165
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(TwoDimParser.ASSIGN, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_assign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_op" ):
                listener.enterAssign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_op" ):
                listener.exitAssign_op(self)




    def assign_op(self):

        localctx = TwoDimParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(TwoDimParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TwoDimParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.BlockContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.BlockContext,i)


        def simpleStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(TwoDimParser.SEMI, 0)

        def ELSE(self):
            return self.getToken(TwoDimParser.ELSE, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(TwoDimParser.IfStmtContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = TwoDimParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(TwoDimParser.IF)
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 170
                self.simpleStmt()
                self.state = 171
                self.match(TwoDimParser.SEMI)


            self.state = 175
            self.expression()
            self.state = 176
            self.block()
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(TwoDimParser.ELSE)
                self.state = 180
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TwoDimParser.IF]:
                    self.state = 178
                    self.ifStmt()
                    pass
                elif token in [TwoDimParser.L_CURLY]:
                    self.state = 179
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprSwitchStmt(self):
            return self.getTypedRuleContext(TwoDimParser.ExprSwitchStmtContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = TwoDimParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_switchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.exprSwitchStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprSwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TwoDimParser.SWITCH, 0)

        def L_CURLY(self):
            return self.getToken(TwoDimParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(TwoDimParser.R_CURLY, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(TwoDimParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def exprCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ExprCaseClauseContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ExprCaseClauseContext,i)


        def getRuleIndex(self):
            return TwoDimParser.RULE_exprSwitchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSwitchStmt" ):
                listener.enterExprSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSwitchStmt" ):
                listener.exitExprSwitchStmt(self)




    def exprSwitchStmt(self):

        localctx = TwoDimParser.ExprSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(TwoDimParser.SWITCH)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 187
                self.simpleStmt()
                self.state = 188
                self.match(TwoDimParser.SEMI)


            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (TwoDimParser.NIL_LIT - 10)) | (1 << (TwoDimParser.IDENTIFIER - 10)) | (1 << (TwoDimParser.SQUARE - 10)) | (1 << (TwoDimParser.RECT - 10)) | (1 << (TwoDimParser.CIRCLE - 10)) | (1 << (TwoDimParser.TRIANGLE - 10)) | (1 << (TwoDimParser.SHAPE - 10)) | (1 << (TwoDimParser.L_PAREN - 10)) | (1 << (TwoDimParser.DECIMAL_LIT - 10)) | (1 << (TwoDimParser.FLOAT_LIT - 10)) | (1 << (TwoDimParser.RUNE_LIT - 10)) | (1 << (TwoDimParser.RAW_STRING_LIT - 10)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 10)))) != 0):
                self.state = 192
                self.expression()


            self.state = 195
            self.match(TwoDimParser.L_CURLY)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.CASE or _la==TwoDimParser.DEFAULT:
                self.state = 196
                self.exprCaseClause()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(TwoDimParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprCaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprSwitchCase(self):
            return self.getTypedRuleContext(TwoDimParser.ExprSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(TwoDimParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(TwoDimParser.StatementListContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_exprCaseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprCaseClause" ):
                listener.enterExprCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprCaseClause" ):
                listener.exitExprCaseClause(self)




    def exprCaseClause(self):

        localctx = TwoDimParser.ExprCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.exprSwitchCase()
            self.state = 205
            self.match(TwoDimParser.COLON)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 2)) & ~0x3f) == 0 and ((1 << (_la - 2)) & ((1 << (TwoDimParser.SWITCH - 2)) | (1 << (TwoDimParser.IF - 2)) | (1 << (TwoDimParser.NIL_LIT - 2)) | (1 << (TwoDimParser.IDENTIFIER - 2)) | (1 << (TwoDimParser.SQUARE - 2)) | (1 << (TwoDimParser.RECT - 2)) | (1 << (TwoDimParser.CIRCLE - 2)) | (1 << (TwoDimParser.TRIANGLE - 2)) | (1 << (TwoDimParser.SHAPE - 2)) | (1 << (TwoDimParser.L_PAREN - 2)) | (1 << (TwoDimParser.L_CURLY - 2)) | (1 << (TwoDimParser.DECIMAL_LIT - 2)) | (1 << (TwoDimParser.FLOAT_LIT - 2)) | (1 << (TwoDimParser.RUNE_LIT - 2)) | (1 << (TwoDimParser.RAW_STRING_LIT - 2)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 2)))) != 0):
                self.state = 206
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprSwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TwoDimParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def DEFAULT(self):
            return self.getToken(TwoDimParser.DEFAULT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_exprSwitchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSwitchCase" ):
                listener.enterExprSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSwitchCase" ):
                listener.exitExprSwitchCase(self)




    def exprSwitchCase(self):

        localctx = TwoDimParser.ExprSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprSwitchCase)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(TwoDimParser.CASE)
                self.state = 210
                self.expression()
                pass
            elif token in [TwoDimParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(TwoDimParser.DEFAULT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)




    def type_(self):

        localctx = TwoDimParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_type_)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.typeName()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(TwoDimParser.L_PAREN)
                self.state = 216
                self.type_()
                self.state = 217
                self.match(TwoDimParser.R_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECT(self):
            return self.getToken(TwoDimParser.RECT, 0)

        def SQUARE(self):
            return self.getToken(TwoDimParser.SQUARE, 0)

        def CIRCLE(self):
            return self.getToken(TwoDimParser.CIRCLE, 0)

        def TRIANGLE(self):
            return self.getToken(TwoDimParser.TRIANGLE, 0)

        def SHAPE(self):
            return self.getToken(TwoDimParser.SHAPE, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = TwoDimParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_elementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementType" ):
                listener.enterElementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementType" ):
                listener.exitElementType(self)




    def elementType(self):

        localctx = TwoDimParser.ElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elementType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.PrimaryExprContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.PrimaryExprContext,i)


        def LEFT(self):
            return self.getToken(TwoDimParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(TwoDimParser.RIGHT, 0)

        def TOP(self):
            return self.getToken(TwoDimParser.TOP, 0)

        def BOT(self):
            return self.getToken(TwoDimParser.BOT, 0)

        def INNER(self):
            return self.getToken(TwoDimParser.INNER, 0)

        def OUTER(self):
            return self.getToken(TwoDimParser.OUTER, 0)

        def IN(self):
            return self.getToken(TwoDimParser.IN, 0)

        def ON(self):
            return self.getToken(TwoDimParser.ON, 0)

        def UNDER(self):
            return self.getToken(TwoDimParser.UNDER, 0)

        def PLUS(self):
            return self.getToken(TwoDimParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(TwoDimParser.MINUS, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = TwoDimParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.primaryExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.primaryExpr()
                self.state = 227
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.LEFT) | (1 << TwoDimParser.RIGHT) | (1 << TwoDimParser.TOP) | (1 << TwoDimParser.BOT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.OUTER or _la==TwoDimParser.INNER:
                    self.state = 228
                    _la = self._input.LA(1)
                    if not(_la==TwoDimParser.OUTER or _la==TwoDimParser.INNER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 231
                self.primaryExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.primaryExpr()
                self.state = 234
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.ON) | (1 << TwoDimParser.UNDER) | (1 << TwoDimParser.IN))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 235
                self.primaryExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.primaryExpr()
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==TwoDimParser.PLUS or _la==TwoDimParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.primaryExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TwoDimParser.OperandContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)




    def primaryExpr(self):

        localctx = TwoDimParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(TwoDimParser.LiteralContext,0)


        def operandName(self):
            return self.getTypedRuleContext(TwoDimParser.OperandNameContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = TwoDimParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operand)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.NIL_LIT, TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE, TwoDimParser.L_PAREN, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.literal()
                pass
            elif token in [TwoDimParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.operandName()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicLit(self):
            return self.getTypedRuleContext(TwoDimParser.BasicLitContext,0)


        def compositeLit(self):
            return self.getTypedRuleContext(TwoDimParser.CompositeLitContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = TwoDimParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.NIL_LIT, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.basicLit()
                pass
            elif token in [TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE, TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.compositeLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL_LIT(self):
            return self.getToken(TwoDimParser.NIL_LIT, 0)

        def integer(self):
            return self.getTypedRuleContext(TwoDimParser.IntegerContext,0)


        def string_(self):
            return self.getTypedRuleContext(TwoDimParser.String_Context,0)


        def FLOAT_LIT(self):
            return self.getToken(TwoDimParser.FLOAT_LIT, 0)

        def RUNE_LIT(self):
            return self.getToken(TwoDimParser.RUNE_LIT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_basicLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicLit" ):
                listener.enterBasicLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicLit" ):
                listener.exitBasicLit(self)




    def basicLit(self):

        localctx = TwoDimParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_basicLit)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(TwoDimParser.NIL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.integer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.string_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(TwoDimParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.match(TwoDimParser.RUNE_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(TwoDimParser.DECIMAL_LIT, 0)

        def RUNE_LIT(self):
            return self.getToken(TwoDimParser.RUNE_LIT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = TwoDimParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not(_la==TwoDimParser.DECIMAL_LIT or _la==TwoDimParser.RUNE_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_operandName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandName" ):
                listener.enterOperandName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandName" ):
                listener.exitOperandName(self)




    def operandName(self):

        localctx = TwoDimParser.OperandNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operandName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(TwoDimParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalType(self):
            return self.getTypedRuleContext(TwoDimParser.LiteralTypeContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(TwoDimParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_compositeLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompositeLit" ):
                listener.enterCompositeLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompositeLit" ):
                listener.exitCompositeLit(self)




    def compositeLit(self):

        localctx = TwoDimParser.CompositeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_compositeLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.literalType()
            self.state = 265
            self.literalValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementType(self):
            return self.getTypedRuleContext(TwoDimParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_literalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralType" ):
                listener.enterLiteralType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralType" ):
                listener.exitLiteralType(self)




    def literalType(self):

        localctx = TwoDimParser.LiteralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_literalType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(TwoDimParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(TwoDimParser.R_CURLY, 0)

        def element(self):
            return self.getTypedRuleContext(TwoDimParser.ElementContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)




    def literalValue(self):

        localctx = TwoDimParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(TwoDimParser.L_CURLY)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (TwoDimParser.NIL_LIT - 10)) | (1 << (TwoDimParser.IDENTIFIER - 10)) | (1 << (TwoDimParser.SQUARE - 10)) | (1 << (TwoDimParser.RECT - 10)) | (1 << (TwoDimParser.CIRCLE - 10)) | (1 << (TwoDimParser.TRIANGLE - 10)) | (1 << (TwoDimParser.SHAPE - 10)) | (1 << (TwoDimParser.L_PAREN - 10)) | (1 << (TwoDimParser.L_CURLY - 10)) | (1 << (TwoDimParser.DECIMAL_LIT - 10)) | (1 << (TwoDimParser.FLOAT_LIT - 10)) | (1 << (TwoDimParser.RUNE_LIT - 10)) | (1 << (TwoDimParser.RAW_STRING_LIT - 10)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 10)))) != 0):
                self.state = 270
                self.element()


            self.state = 273
            self.match(TwoDimParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(TwoDimParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = TwoDimParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_element)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.NIL_LIT, TwoDimParser.IDENTIFIER, TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE, TwoDimParser.L_PAREN, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.expression()
                pass
            elif token in [TwoDimParser.L_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.literalValue()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAW_STRING_LIT(self):
            return self.getToken(TwoDimParser.RAW_STRING_LIT, 0)

        def INTERPRETED_STRING_LIT(self):
            return self.getToken(TwoDimParser.INTERPRETED_STRING_LIT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)




    def string_(self):

        localctx = TwoDimParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not(_la==TwoDimParser.RAW_STRING_LIT or _la==TwoDimParser.INTERPRETED_STRING_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def SIZE(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.SIZE)
            else:
                return self.getToken(TwoDimParser.SIZE, i)

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def COMMA(self):
            return self.getToken(TwoDimParser.COMMA, 0)

        def WS(self):
            return self.getToken(TwoDimParser.WS, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = TwoDimParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(TwoDimParser.L_PAREN)
            self.state = 282
            self.match(TwoDimParser.SIZE)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.COMMA:
                self.state = 283
                self.match(TwoDimParser.COMMA)
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.WS:
                    self.state = 284
                    self.match(TwoDimParser.WS)


                self.state = 287
                self.match(TwoDimParser.SIZE)


            self.state = 290
            self.match(TwoDimParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(TwoDimParser.SEMI, 0)

        def EOF(self):
            return self.getToken(TwoDimParser.EOF, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)




    def eos(self):

        localctx = TwoDimParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_eos)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(TwoDimParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(TwoDimParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                if not lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                if not checkPreviousTokenText("}"):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "checkPreviousTokenText(\"}\")")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 0:
                return lineTerminatorAhead()
         

            if predIndex == 1:
                return checkPreviousTokenText("}")
         




