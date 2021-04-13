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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u0148\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\5")
        buf.write("\2L\n\2\3\2\3\2\5\2P\n\2\3\2\3\2\7\2T\n\2\f\2\16\2W\13")
        buf.write("\2\3\2\5\2Z\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\5\7\5i\n\5\f\5\16\5l\13\5\3\6\3\6\3\6\7\6")
        buf.write("q\n\6\f\6\16\6t\13\6\3\7\3\7\3\7\3\7\5\7z\n\7\3\b\3\b")
        buf.write("\3\b\5\b\177\n\b\3\t\3\t\3\t\3\t\7\t\u0085\n\t\f\t\16")
        buf.write("\t\u0088\13\t\5\t\u008a\n\t\3\t\3\t\3\n\3\n\5\n\u0090")
        buf.write("\n\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r\u009a\n\r")
        buf.write("\3\r\3\r\3\r\5\r\u009f\n\r\3\r\3\r\7\r\u00a3\n\r\f\r\16")
        buf.write("\r\u00a6\13\r\3\16\3\16\5\16\u00aa\n\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\6\17\u00b1\n\17\r\17\16\17\u00b2\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00ba\n\20\3\21\3\21\3\21\5\21\u00bf")
        buf.write("\n\21\3\22\3\22\3\23\5\23\u00c4\n\23\3\23\5\23\u00c7\n")
        buf.write("\23\3\23\3\23\5\23\u00cb\n\23\3\23\3\23\3\23\5\23\u00d0")
        buf.write("\n\23\3\23\5\23\u00d3\n\23\3\23\5\23\u00d6\n\23\3\23\5")
        buf.write("\23\u00d9\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00e5\n\26\3\26\3\26\3\26\3\26\3\26\5")
        buf.write("\26\u00ec\n\26\5\26\u00ee\n\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u00f6\n\30\3\30\5\30\u00f9\n\30\3\30\3\30\7")
        buf.write("\30\u00fd\n\30\f\30\16\30\u0100\13\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\5\31\u0107\n\31\3\32\3\32\3\32\5\32\u010c\n\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0114\n\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0120")
        buf.write("\n\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u012a")
        buf.write("\n\36\3\37\3\37\3 \3 \3 \3 \3 \5 \u0133\n \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\5$\u013d\n$\3$\3$\3%\3%\3%\3%\3%\5%\u0146")
        buf.write("\n%\3%\2\2&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFH\2\t\3\2\16\22\3\2\25\30\3")
        buf.write("\2\31\32\3\2\33\35\3\2:;\4\2??AA\3\2BC\2\u0156\2K\3\2")
        buf.write("\2\2\4^\3\2\2\2\6c\3\2\2\2\be\3\2\2\2\nm\3\2\2\2\fu\3")
        buf.write("\2\2\2\16~\3\2\2\2\20\u0080\3\2\2\2\22\u008d\3\2\2\2\24")
        buf.write("\u0091\3\2\2\2\26\u0094\3\2\2\2\30\u0096\3\2\2\2\32\u00a7")
        buf.write("\3\2\2\2\34\u00b0\3\2\2\2\36\u00b9\3\2\2\2 \u00be\3\2")
        buf.write("\2\2\"\u00c0\3\2\2\2$\u00c3\3\2\2\2&\u00da\3\2\2\2(\u00de")
        buf.write("\3\2\2\2*\u00e0\3\2\2\2,\u00ef\3\2\2\2.\u00f1\3\2\2\2")
        buf.write("\60\u0103\3\2\2\2\62\u010b\3\2\2\2\64\u010d\3\2\2\2\66")
        buf.write("\u011f\3\2\2\28\u0121\3\2\2\2:\u0129\3\2\2\2<\u012b\3")
        buf.write("\2\2\2>\u0132\3\2\2\2@\u0134\3\2\2\2B\u0136\3\2\2\2D\u0138")
        buf.write("\3\2\2\2F\u013a\3\2\2\2H\u0145\3\2\2\2JL\5\4\3\2KJ\3\2")
        buf.write("\2\2KL\3\2\2\2LU\3\2\2\2MP\5\f\7\2NP\5\6\4\2OM\3\2\2\2")
        buf.write("ON\3\2\2\2PQ\3\2\2\2QR\5H%\2RT\3\2\2\2SO\3\2\2\2TW\3\2")
        buf.write("\2\2US\3\2\2\2UV\3\2\2\2VY\3\2\2\2WU\3\2\2\2XZ\5\34\17")
        buf.write("\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\5\24\13\2\\]\5H%\2")
        buf.write("]\3\3\2\2\2^_\7\24\2\2_`\7?\2\2`a\7?\2\2ab\5H%\2b\5\3")
        buf.write("\2\2\2cd\5\26\f\2d\7\3\2\2\2ej\7\r\2\2fg\7%\2\2gi\7\r")
        buf.write("\2\2hf\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\t\3\2\2")
        buf.write("\2lj\3\2\2\2mr\5\66\34\2no\7%\2\2oq\5\66\34\2pn\3\2\2")
        buf.write("\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\13\3\2\2\2tr\3\2\2\2")
        buf.write("uv\7\3\2\2vw\7\r\2\2wy\5\16\b\2xz\5\32\16\2yx\3\2\2\2")
        buf.write("yz\3\2\2\2z\r\3\2\2\2{|\6\b\2\2|\177\5\20\t\2}\177\5\20")
        buf.write("\t\2~{\3\2\2\2~}\3\2\2\2\177\17\3\2\2\2\u0080\u0089\7")
        buf.write("\36\2\2\u0081\u0086\5\22\n\2\u0082\u0083\7%\2\2\u0083")
        buf.write("\u0085\5\22\n\2\u0084\u0082\3\2\2\2\u0085\u0088\3\2\2")
        buf.write("\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u008a")
        buf.write("\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u0081\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7\37\2")
        buf.write("\2\u008c\21\3\2\2\2\u008d\u008f\5\64\33\2\u008e\u0090")
        buf.write("\5\b\5\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\23\3\2\2\2\u0091\u0092\7\23\2\2\u0092\u0093\7\r\2\2\u0093")
        buf.write("\25\3\2\2\2\u0094\u0095\5\30\r\2\u0095\27\3\2\2\2\u0096")
        buf.write("\u0097\5\64\33\2\u0097\u0099\7\r\2\2\u0098\u009a\7E\2")
        buf.write("\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\u00a4\5$\23\2\u009c\u009e\7%\2\2\u009d")
        buf.write("\u009f\7E\2\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\r\2\2\u00a1\u00a3\5")
        buf.write("$\23\2\u00a2\u009c\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\31\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a7\u00a9\7 \2\2\u00a8\u00aa\5\34\17\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\7!\2\2\u00ac\33\3\2\2\2\u00ad\u00ae\5\36")
        buf.write("\20\2\u00ae\u00af\5H%\2\u00af\u00b1\3\2\2\2\u00b0\u00ad")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\35\3\2\2\2\u00b4\u00ba\5\6\4\2\u00b5")
        buf.write("\u00ba\5 \21\2\u00b6\u00ba\5\32\16\2\u00b7\u00ba\5*\26")
        buf.write("\2\u00b8\u00ba\5,\27\2\u00b9\u00b4\3\2\2\2\u00b9\u00b5")
        buf.write("\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00ba\37\3\2\2\2\u00bb\u00bf\5\"\22\2\u00bc")
        buf.write("\u00bf\5&\24\2\u00bd\u00bf\5\24\13\2\u00be\u00bb\3\2\2")
        buf.write("\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf!\3\2")
        buf.write("\2\2\u00c0\u00c1\5\66\34\2\u00c1#\3\2\2\2\u00c2\u00c4")
        buf.write("\5F$\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6")
        buf.write("\3\2\2\2\u00c5\u00c7\7E\2\2\u00c6\u00c5\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00d8\3\2\2\2\u00c8\u00ca\7\"\2\2")
        buf.write("\u00c9\u00cb\7E\2\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00d2\7D\2\2\u00cd\u00cf")
        buf.write("\7%\2\2\u00ce\u00d0\7E\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\7D\2\2\u00d2")
        buf.write("\u00cd\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2")
        buf.write("\u00d4\u00d6\7E\2\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3")
        buf.write("\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\7#\2\2\u00d8\u00c8")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9%\3\2\2\2\u00da\u00db")
        buf.write("\7\r\2\2\u00db\u00dc\5(\25\2\u00dc\u00dd\5\66\34\2\u00dd")
        buf.write("\'\3\2\2\2\u00de\u00df\7$\2\2\u00df)\3\2\2\2\u00e0\u00e4")
        buf.write("\7\7\2\2\u00e1\u00e2\5 \21\2\u00e2\u00e3\7&\2\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e7\5\66\34\2\u00e7\u00ed")
        buf.write("\5\32\16\2\u00e8\u00eb\7\b\2\2\u00e9\u00ec\5*\26\2\u00ea")
        buf.write("\u00ec\5\32\16\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2")
        buf.write("\2\u00ec\u00ee\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee+\3\2\2\2\u00ef\u00f0\5.\30\2\u00f0-\3\2")
        buf.write("\2\2\u00f1\u00f5\7\4\2\2\u00f2\u00f3\5 \21\2\u00f3\u00f4")
        buf.write("\7&\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f2\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f9\5\66\34")
        buf.write("\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa\u00fe\7 \2\2\u00fb\u00fd\5\60\31\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3")
        buf.write("\2\2\2\u0101\u0102\7!\2\2\u0102/\3\2\2\2\u0103\u0104\5")
        buf.write("\62\32\2\u0104\u0106\7\'\2\2\u0105\u0107\5\34\17\2\u0106")
        buf.write("\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\61\3\2\2\2\u0108")
        buf.write("\u0109\7\5\2\2\u0109\u010c\5\66\34\2\u010a\u010c\7\6\2")
        buf.write("\2\u010b\u0108\3\2\2\2\u010b\u010a\3\2\2\2\u010c\63\3")
        buf.write("\2\2\2\u010d\u010e\t\2\2\2\u010e\65\3\2\2\2\u010f\u0120")
        buf.write("\58\35\2\u0110\u0111\58\35\2\u0111\u0113\t\3\2\2\u0112")
        buf.write("\u0114\t\4\2\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115\u0116\58\35\2\u0116\u0120\3")
        buf.write("\2\2\2\u0117\u0118\58\35\2\u0118\u0119\t\5\2\2\u0119\u011a")
        buf.write("\58\35\2\u011a\u0120\3\2\2\2\u011b\u011c\58\35\2\u011c")
        buf.write("\u011d\t\6\2\2\u011d\u011e\58\35\2\u011e\u0120\3\2\2\2")
        buf.write("\u011f\u010f\3\2\2\2\u011f\u0110\3\2\2\2\u011f\u0117\3")
        buf.write("\2\2\2\u011f\u011b\3\2\2\2\u0120\67\3\2\2\2\u0121\u0122")
        buf.write("\5:\36\2\u01229\3\2\2\2\u0123\u012a\5<\37\2\u0124\u012a")
        buf.write("\5B\"\2\u0125\u0126\7\36\2\2\u0126\u0127\5\66\34\2\u0127")
        buf.write("\u0128\7\37\2\2\u0128\u012a\3\2\2\2\u0129\u0123\3\2\2")
        buf.write("\2\u0129\u0124\3\2\2\2\u0129\u0125\3\2\2\2\u012a;\3\2")
        buf.write("\2\2\u012b\u012c\5> \2\u012c=\3\2\2\2\u012d\u0133\7\f")
        buf.write("\2\2\u012e\u0133\5@!\2\u012f\u0133\5D#\2\u0130\u0133\7")
        buf.write("@\2\2\u0131\u0133\7A\2\2\u0132\u012d\3\2\2\2\u0132\u012e")
        buf.write("\3\2\2\2\u0132\u012f\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133?\3\2\2\2\u0134\u0135\t\7\2\2\u0135")
        buf.write("A\3\2\2\2\u0136\u0137\7\r\2\2\u0137C\3\2\2\2\u0138\u0139")
        buf.write("\t\b\2\2\u0139E\3\2\2\2\u013a\u013c\7\36\2\2\u013b\u013d")
        buf.write("\5\n\6\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u013f\7\37\2\2\u013fG\3\2\2\2\u0140")
        buf.write("\u0146\7&\2\2\u0141\u0142\7&\2\2\u0142\u0146\7\2\2\3\u0143")
        buf.write("\u0146\6%\3\2\u0144\u0146\6%\4\2\u0145\u0140\3\2\2\2\u0145")
        buf.write("\u0141\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u0146I\3\2\2\2)KOUYjry~\u0086\u0089\u008f\u0099\u009e")
        buf.write("\u00a4\u00a9\u00b2\u00b9\u00be\u00c3\u00c6\u00ca\u00cf")
        buf.write("\u00d2\u00d5\u00d8\u00e4\u00eb\u00ed\u00f5\u00f8\u00fe")
        buf.write("\u0106\u010b\u0113\u011f\u0129\u0132\u013c\u0145")
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
                      "SIZE_LIT", "WS", "COMMENT", "TERMINATOR", "LINE_COMMENT" ]

    RULE_sourceFile = 0
    RULE_viewportClause = 1
    RULE_declaration = 2
    RULE_identifierList = 3
    RULE_expressionList = 4
    RULE_functionDecl = 5
    RULE_signature = 6
    RULE_parameters = 7
    RULE_parameterDecl = 8
    RULE_drawClause = 9
    RULE_shapeDecl = 10
    RULE_shapeSpec = 11
    RULE_block = 12
    RULE_statementList = 13
    RULE_statement = 14
    RULE_simpleStmt = 15
    RULE_expressionStmt = 16
    RULE_shapeArguments = 17
    RULE_assignment = 18
    RULE_assign_op = 19
    RULE_ifStmt = 20
    RULE_switchStmt = 21
    RULE_exprSwitchStmt = 22
    RULE_exprCaseClause = 23
    RULE_exprSwitchCase = 24
    RULE_typeName = 25
    RULE_expression = 26
    RULE_primaryExpr = 27
    RULE_operand = 28
    RULE_literal = 29
    RULE_basicLit = 30
    RULE_integer = 31
    RULE_operandName = 32
    RULE_string_ = 33
    RULE_arguments = 34
    RULE_eos = 35

    ruleNames =  [ "sourceFile", "viewportClause", "declaration", "identifierList", 
                   "expressionList", "functionDecl", "signature", "parameters", 
                   "parameterDecl", "drawClause", "shapeDecl", "shapeSpec", 
                   "block", "statementList", "statement", "simpleStmt", 
                   "expressionStmt", "shapeArguments", "assignment", "assign_op", 
                   "ifStmt", "switchStmt", "exprSwitchStmt", "exprCaseClause", 
                   "exprSwitchCase", "typeName", "expression", "primaryExpr", 
                   "operand", "literal", "basicLit", "integer", "operandName", 
                   "string_", "arguments", "eos" ]

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
    SIZE_LIT=66
    WS=67
    COMMENT=68
    TERMINATOR=69
    LINE_COMMENT=70

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

        def drawClause(self):
            return self.getTypedRuleContext(TwoDimParser.DrawClauseContext,0)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.EosContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.EosContext,i)


        def viewportClause(self):
            return self.getTypedRuleContext(TwoDimParser.ViewportClauseContext,0)


        def statementList(self):
            return self.getTypedRuleContext(TwoDimParser.StatementListContext,0)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.FunctionDeclContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.DeclarationContext,i)


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
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.VIEWPORT:
                self.state = 72
                self.viewportClause()


            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [TwoDimParser.FUNC]:
                        self.state = 75
                        self.functionDecl()
                        pass
                    elif token in [TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE]:
                        self.state = 76
                        self.declaration()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 79
                    self.eos() 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 86
                self.statementList()


            self.state = 89
            self.drawClause()
            self.state = 90
            self.eos()
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

        def DECIMAL_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.DECIMAL_LIT)
            else:
                return self.getToken(TwoDimParser.DECIMAL_LIT, i)

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
            self.state = 92
            self.match(TwoDimParser.VIEWPORT)
            self.state = 93
            self.match(TwoDimParser.DECIMAL_LIT)
            self.state = 94
            self.match(TwoDimParser.DECIMAL_LIT)
            self.state = 95
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

        def shapeDecl(self):
            return self.getTypedRuleContext(TwoDimParser.ShapeDeclContext,0)


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
            self.state = 97
            self.shapeDecl()
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 100
                    self.match(TwoDimParser.COMMA)
                    self.state = 101
                    self.match(TwoDimParser.IDENTIFIER) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = TwoDimParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expression()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.COMMA:
                self.state = 108
                self.match(TwoDimParser.COMMA)
                self.state = 109
                self.expression()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TwoDimParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(TwoDimParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(TwoDimParser.BlockContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = TwoDimParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(TwoDimParser.FUNC)
            self.state = 116
            self.match(TwoDimParser.IDENTIFIER)

            self.state = 117
            self.signature()
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 118
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(TwoDimParser.ParametersContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignature" ):
                listener.enterSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignature" ):
                listener.exitSignature(self)




    def signature(self):

        localctx = TwoDimParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_signature)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                if not self.noTerminatorAfterParams(1):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.noTerminatorAfterParams(1)")
                self.state = 122
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def parameterDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ParameterDeclContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ParameterDeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = TwoDimParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(TwoDimParser.L_PAREN)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE))) != 0):
                self.state = 127
                self.parameterDecl()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TwoDimParser.COMMA:
                    self.state = 128
                    self.match(TwoDimParser.COMMA)
                    self.state = 129
                    self.parameterDecl()
                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 137
            self.match(TwoDimParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def identifierList(self):
            return self.getTypedRuleContext(TwoDimParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_parameterDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterDecl" ):
                listener.enterParameterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterDecl" ):
                listener.exitParameterDecl(self)




    def parameterDecl(self):

        localctx = TwoDimParser.ParameterDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.typeName()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.IDENTIFIER:
                self.state = 140
                self.identifierList()


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
        self.enterRule(localctx, 18, self.RULE_drawClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(TwoDimParser.DRAW)
            self.state = 144
            self.match(TwoDimParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shapeSpec(self):
            return self.getTypedRuleContext(TwoDimParser.ShapeSpecContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_shapeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeDecl" ):
                listener.enterShapeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeDecl" ):
                listener.exitShapeDecl(self)




    def shapeDecl(self):

        localctx = TwoDimParser.ShapeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_shapeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.shapeSpec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.IDENTIFIER)
            else:
                return self.getToken(TwoDimParser.IDENTIFIER, i)

        def shapeArguments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ShapeArgumentsContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ShapeArgumentsContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.WS)
            else:
                return self.getToken(TwoDimParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_shapeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeSpec" ):
                listener.enterShapeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeSpec" ):
                listener.exitShapeSpec(self)




    def shapeSpec(self):

        localctx = TwoDimParser.ShapeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_shapeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.typeName()
            self.state = 149
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 150
                self.match(TwoDimParser.WS)


            self.state = 153
            self.shapeArguments()
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    self.match(TwoDimParser.COMMA)
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==TwoDimParser.WS:
                        self.state = 155
                        self.match(TwoDimParser.WS)


                    self.state = 158
                    self.match(TwoDimParser.IDENTIFIER)
                    self.state = 159
                    self.shapeArguments() 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(TwoDimParser.L_CURLY)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 2)) & ~0x3f) == 0 and ((1 << (_la - 2)) & ((1 << (TwoDimParser.SWITCH - 2)) | (1 << (TwoDimParser.IF - 2)) | (1 << (TwoDimParser.NIL_LIT - 2)) | (1 << (TwoDimParser.IDENTIFIER - 2)) | (1 << (TwoDimParser.SQUARE - 2)) | (1 << (TwoDimParser.RECT - 2)) | (1 << (TwoDimParser.CIRCLE - 2)) | (1 << (TwoDimParser.TRIANGLE - 2)) | (1 << (TwoDimParser.SHAPE - 2)) | (1 << (TwoDimParser.DRAW - 2)) | (1 << (TwoDimParser.L_PAREN - 2)) | (1 << (TwoDimParser.L_CURLY - 2)) | (1 << (TwoDimParser.DECIMAL_LIT - 2)) | (1 << (TwoDimParser.FLOAT_LIT - 2)) | (1 << (TwoDimParser.RUNE_LIT - 2)) | (1 << (TwoDimParser.RAW_STRING_LIT - 2)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 2)))) != 0):
                self.state = 166
                self.statementList()


            self.state = 169
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
        self.enterRule(localctx, 26, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 171
                    self.statement()
                    self.state = 172
                    self.eos()

                else:
                    raise NoViableAltException(self)
                self.state = 176 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.declaration()
                pass
            elif token in [TwoDimParser.NIL_LIT, TwoDimParser.IDENTIFIER, TwoDimParser.DRAW, TwoDimParser.L_PAREN, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.simpleStmt()
                pass
            elif token in [TwoDimParser.L_CURLY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.block()
                pass
            elif token in [TwoDimParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.ifStmt()
                pass
            elif token in [TwoDimParser.SWITCH]:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.switchStmt()
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


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStmt(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(TwoDimParser.AssignmentContext,0)


        def drawClause(self):
            return self.getTypedRuleContext(TwoDimParser.DrawClauseContext,0)


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
        self.enterRule(localctx, 30, self.RULE_simpleStmt)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.expressionStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.drawClause()
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
        self.enterRule(localctx, 32, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguments(self):
            return self.getTypedRuleContext(TwoDimParser.ArgumentsContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.WS)
            else:
                return self.getToken(TwoDimParser.WS, i)

        def L_BRACKET(self):
            return self.getToken(TwoDimParser.L_BRACKET, 0)

        def SIZE_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.SIZE_LIT)
            else:
                return self.getToken(TwoDimParser.SIZE_LIT, i)

        def R_BRACKET(self):
            return self.getToken(TwoDimParser.R_BRACKET, 0)

        def COMMA(self):
            return self.getToken(TwoDimParser.COMMA, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_shapeArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeArguments" ):
                listener.enterShapeArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeArguments" ):
                listener.exitShapeArguments(self)




    def shapeArguments(self):

        localctx = TwoDimParser.ShapeArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_shapeArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 192
                self.arguments()


            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 195
                self.match(TwoDimParser.WS)


            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 198
                self.match(TwoDimParser.L_BRACKET)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.WS:
                    self.state = 199
                    self.match(TwoDimParser.WS)


                self.state = 202
                self.match(TwoDimParser.SIZE_LIT)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.COMMA:
                    self.state = 203
                    self.match(TwoDimParser.COMMA)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==TwoDimParser.WS:
                        self.state = 204
                        self.match(TwoDimParser.WS)


                    self.state = 207
                    self.match(TwoDimParser.SIZE_LIT)


                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.WS:
                    self.state = 210
                    self.match(TwoDimParser.WS)


                self.state = 213
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
        self.enterRule(localctx, 36, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 217
            self.assign_op()
            self.state = 218
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
        self.enterRule(localctx, 38, self.RULE_assign_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
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
        self.enterRule(localctx, 40, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(TwoDimParser.IF)
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 223
                self.simpleStmt()
                self.state = 224
                self.match(TwoDimParser.SEMI)


            self.state = 228
            self.expression()
            self.state = 229
            self.block()
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(TwoDimParser.ELSE)
                self.state = 233
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TwoDimParser.IF]:
                    self.state = 231
                    self.ifStmt()
                    pass
                elif token in [TwoDimParser.L_CURLY]:
                    self.state = 232
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
        self.enterRule(localctx, 42, self.RULE_switchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
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
        self.enterRule(localctx, 44, self.RULE_exprSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(TwoDimParser.SWITCH)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 240
                self.simpleStmt()
                self.state = 241
                self.match(TwoDimParser.SEMI)


            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (TwoDimParser.NIL_LIT - 10)) | (1 << (TwoDimParser.IDENTIFIER - 10)) | (1 << (TwoDimParser.L_PAREN - 10)) | (1 << (TwoDimParser.DECIMAL_LIT - 10)) | (1 << (TwoDimParser.FLOAT_LIT - 10)) | (1 << (TwoDimParser.RUNE_LIT - 10)) | (1 << (TwoDimParser.RAW_STRING_LIT - 10)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 10)))) != 0):
                self.state = 245
                self.expression()


            self.state = 248
            self.match(TwoDimParser.L_CURLY)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.CASE or _la==TwoDimParser.DEFAULT:
                self.state = 249
                self.exprCaseClause()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
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
        self.enterRule(localctx, 46, self.RULE_exprCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.exprSwitchCase()
            self.state = 258
            self.match(TwoDimParser.COLON)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 2)) & ~0x3f) == 0 and ((1 << (_la - 2)) & ((1 << (TwoDimParser.SWITCH - 2)) | (1 << (TwoDimParser.IF - 2)) | (1 << (TwoDimParser.NIL_LIT - 2)) | (1 << (TwoDimParser.IDENTIFIER - 2)) | (1 << (TwoDimParser.SQUARE - 2)) | (1 << (TwoDimParser.RECT - 2)) | (1 << (TwoDimParser.CIRCLE - 2)) | (1 << (TwoDimParser.TRIANGLE - 2)) | (1 << (TwoDimParser.SHAPE - 2)) | (1 << (TwoDimParser.DRAW - 2)) | (1 << (TwoDimParser.L_PAREN - 2)) | (1 << (TwoDimParser.L_CURLY - 2)) | (1 << (TwoDimParser.DECIMAL_LIT - 2)) | (1 << (TwoDimParser.FLOAT_LIT - 2)) | (1 << (TwoDimParser.RUNE_LIT - 2)) | (1 << (TwoDimParser.RAW_STRING_LIT - 2)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 2)))) != 0):
                self.state = 259
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
        self.enterRule(localctx, 48, self.RULE_exprSwitchCase)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(TwoDimParser.CASE)
                self.state = 263
                self.expression()
                pass
            elif token in [TwoDimParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 50, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
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
        self.enterRule(localctx, 52, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.primaryExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.primaryExpr()
                self.state = 271
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.LEFT) | (1 << TwoDimParser.RIGHT) | (1 << TwoDimParser.TOP) | (1 << TwoDimParser.BOT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.OUTER or _la==TwoDimParser.INNER:
                    self.state = 272
                    _la = self._input.LA(1)
                    if not(_la==TwoDimParser.OUTER or _la==TwoDimParser.INNER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 275
                self.primaryExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.primaryExpr()
                self.state = 278
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.ON) | (1 << TwoDimParser.UNDER) | (1 << TwoDimParser.IN))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.primaryExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.primaryExpr()
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==TwoDimParser.PLUS or _la==TwoDimParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
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
        self.enterRule(localctx, 54, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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


        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

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
        self.enterRule(localctx, 56, self.RULE_operand)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.NIL_LIT, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.literal()
                pass
            elif token in [TwoDimParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.operandName()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.match(TwoDimParser.L_PAREN)
                self.state = 292
                self.expression()
                self.state = 293
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicLit(self):
            return self.getTypedRuleContext(TwoDimParser.BasicLitContext,0)


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
        self.enterRule(localctx, 58, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.basicLit()
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
        self.enterRule(localctx, 60, self.RULE_basicLit)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(TwoDimParser.NIL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.integer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.string_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 302
                self.match(TwoDimParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 303
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
        self.enterRule(localctx, 62, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
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
        self.enterRule(localctx, 64, self.RULE_operandName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(TwoDimParser.IDENTIFIER)
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
        self.enterRule(localctx, 66, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
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

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionListContext,0)


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
        self.enterRule(localctx, 68, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(TwoDimParser.L_PAREN)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (TwoDimParser.NIL_LIT - 10)) | (1 << (TwoDimParser.IDENTIFIER - 10)) | (1 << (TwoDimParser.L_PAREN - 10)) | (1 << (TwoDimParser.DECIMAL_LIT - 10)) | (1 << (TwoDimParser.FLOAT_LIT - 10)) | (1 << (TwoDimParser.RUNE_LIT - 10)) | (1 << (TwoDimParser.RAW_STRING_LIT - 10)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 10)))) != 0):
                self.state = 313
                self.expressionList()


            self.state = 316
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
        self.enterRule(localctx, 70, self.RULE_eos)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(TwoDimParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(TwoDimParser.SEMI)
                self.state = 320
                self.match(TwoDimParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                if not self.lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                if not self.checkPreviousTokenText("}"):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.checkPreviousTokenText(\"}\")")
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
        self._predicates[6] = self.signature_sempred
        self._predicates[35] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def signature_sempred(self, localctx:SignatureContext, predIndex:int):
            if predIndex == 0:
                return self.noTerminatorAfterParams(1)
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 1:
                return self.lineTerminatorAhead()
         

            if predIndex == 2:
                return self.checkPreviousTokenText("}")
         




