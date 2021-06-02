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
        buf.write("\u0194\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\5\2X\n\2\3\2\3\2")
        buf.write("\5\2\\\n\2\3\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\5\2f\n")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\7\5u\n\5\f\5\16\5x\13\5\3\6\3\6\3\6\7\6}\n\6\f\6\16\6")
        buf.write("\u0080\13\6\3\7\3\7\3\7\3\7\5\7\u0086\n\7\3\b\3\b\3\b")
        buf.write("\5\b\u008b\n\b\3\t\3\t\3\t\3\t\7\t\u0091\n\t\f\t\16\t")
        buf.write("\u0094\13\t\5\t\u0096\n\t\3\t\3\t\3\n\3\n\5\n\u009c\n")
        buf.write("\n\3\13\3\13\5\13\u00a0\n\13\3\13\3\13\5\13\u00a4\n\13")
        buf.write("\3\13\5\13\u00a7\n\13\3\13\3\13\5\13\u00ab\n\13\3\13\7")
        buf.write("\13\u00ae\n\13\f\13\16\13\u00b1\13\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u00bd\n\16\3\16\3\16")
        buf.write("\3\16\5\16\u00c2\n\16\3\16\3\16\7\16\u00c6\n\16\f\16\16")
        buf.write("\16\u00c9\13\16\3\17\3\17\5\17\u00cd\n\17\3\17\5\17\u00d0")
        buf.write("\n\17\3\17\3\17\3\20\3\20\3\20\6\20\u00d7\n\20\r\20\16")
        buf.write("\20\u00d8\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00e2")
        buf.write("\n\21\3\22\3\22\3\22\5\22\u00e7\n\22\3\23\3\23\3\24\5")
        buf.write("\24\u00ec\n\24\3\24\5\24\u00ef\n\24\3\24\3\24\5\24\u00f3")
        buf.write("\n\24\3\24\3\24\3\24\5\24\u00f8\n\24\3\24\5\24\u00fb\n")
        buf.write("\24\3\24\5\24\u00fe\n\24\3\24\5\24\u0101\n\24\3\25\3\25")
        buf.write("\3\25\5\25\u0106\n\25\3\25\3\25\5\25\u010a\n\25\3\25\3")
        buf.write("\25\5\25\u010e\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\5\30\u011c\n\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0123\n\30\5\30\u0125\n\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u012d\n\32\3\32\5\32\u0130\n")
        buf.write("\32\3\32\3\32\7\32\u0134\n\32\f\32\16\32\u0137\13\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\5\33\u013e\n\33\3\34\3\34\3\34")
        buf.write("\5\34\u0143\n\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\5!\u0150\n!\3!\3!\3!\3!\3!\3!\5!\u0158\n!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0161\n\"\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\3$\5$\u016b\n$\3%\3%\3&\3&\3&\3&\3&\5&\u0174\n")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\7*\u017e\n*\f*\16*\u0181\13")
        buf.write("*\3*\5*\u0184\n*\3*\7*\u0187\n*\f*\16*\u018a\13*\3*\3")
        buf.write("*\3+\3+\3+\3+\5+\u0192\n+\3+\2\2,\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("T\2\t\3\2\16\22\3\2\31\32\3\2\25\30\3\2\33\35\3\2:;\4")
        buf.write("\2??AA\3\2BC\2\u01a9\2W\3\2\2\2\4j\3\2\2\2\6o\3\2\2\2")
        buf.write("\bq\3\2\2\2\ny\3\2\2\2\f\u0081\3\2\2\2\16\u008a\3\2\2")
        buf.write("\2\20\u008c\3\2\2\2\22\u0099\3\2\2\2\24\u009d\3\2\2\2")
        buf.write("\26\u00b4\3\2\2\2\30\u00b7\3\2\2\2\32\u00b9\3\2\2\2\34")
        buf.write("\u00ca\3\2\2\2\36\u00d6\3\2\2\2 \u00e1\3\2\2\2\"\u00e6")
        buf.write("\3\2\2\2$\u00e8\3\2\2\2&\u00eb\3\2\2\2(\u0102\3\2\2\2")
        buf.write("*\u0111\3\2\2\2,\u0115\3\2\2\2.\u0117\3\2\2\2\60\u0126")
        buf.write("\3\2\2\2\62\u0128\3\2\2\2\64\u013a\3\2\2\2\66\u0142\3")
        buf.write("\2\2\28\u0144\3\2\2\2:\u0146\3\2\2\2<\u0148\3\2\2\2>\u014a")
        buf.write("\3\2\2\2@\u0157\3\2\2\2B\u0160\3\2\2\2D\u0162\3\2\2\2")
        buf.write("F\u016a\3\2\2\2H\u016c\3\2\2\2J\u0173\3\2\2\2L\u0175\3")
        buf.write("\2\2\2N\u0177\3\2\2\2P\u0179\3\2\2\2R\u017b\3\2\2\2T\u0191")
        buf.write("\3\2\2\2VX\5\4\3\2WV\3\2\2\2WX\3\2\2\2Xa\3\2\2\2Y\\\5")
        buf.write("\f\7\2Z\\\5\6\4\2[Y\3\2\2\2[Z\3\2\2\2\\]\3\2\2\2]^\5T")
        buf.write("+\2^`\3\2\2\2_[\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2")
        buf.write("be\3\2\2\2ca\3\2\2\2df\5\36\20\2ed\3\2\2\2ef\3\2\2\2f")
        buf.write("g\3\2\2\2gh\5\26\f\2hi\5T+\2i\3\3\2\2\2jk\7\24\2\2kl\7")
        buf.write("?\2\2lm\7?\2\2mn\5T+\2n\5\3\2\2\2op\5\30\r\2p\7\3\2\2")
        buf.write("\2qv\7\r\2\2rs\7%\2\2su\7\r\2\2tr\3\2\2\2ux\3\2\2\2vt")
        buf.write("\3\2\2\2vw\3\2\2\2w\t\3\2\2\2xv\3\2\2\2y~\5B\"\2z{\7%")
        buf.write("\2\2{}\5B\"\2|z\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177")
        buf.write("\3\2\2\2\177\13\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7\3")
        buf.write("\2\2\u0082\u0083\7\r\2\2\u0083\u0085\5\16\b\2\u0084\u0086")
        buf.write("\5\34\17\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\r\3\2\2\2\u0087\u0088\6\b\2\2\u0088\u008b\5\20\t\2\u0089")
        buf.write("\u008b\5\20\t\2\u008a\u0087\3\2\2\2\u008a\u0089\3\2\2")
        buf.write("\2\u008b\17\3\2\2\2\u008c\u0095\7\36\2\2\u008d\u0092\5")
        buf.write("\22\n\2\u008e\u008f\7%\2\2\u008f\u0091\5\22\n\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3")
        buf.write("\2\2\2\u0095\u008d\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0098\7\37\2\2\u0098\21\3\2\2\2\u0099\u009b")
        buf.write("\58\35\2\u009a\u009c\5\b\5\2\u009b\u009a\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\23\3\2\2\2\u009d\u009f\7\r\2\2\u009e")
        buf.write("\u00a0\7E\2\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a3\7\36\2\2\u00a2\u00a4")
        buf.write("\7E\2\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a6\3\2\2\2\u00a5\u00a7\5N(\2\u00a6\u00a5\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00af\3\2\2\2\u00a8\u00aa\7%\2\2")
        buf.write("\u00a9\u00ab\7E\2\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab\3")
        buf.write("\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\5N(\2\u00ad\u00a8")
        buf.write("\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b3\7\37\2\2\u00b3\25\3\2\2\2\u00b4\u00b5\7\23")
        buf.write("\2\2\u00b5\u00b6\7\r\2\2\u00b6\27\3\2\2\2\u00b7\u00b8")
        buf.write("\5\32\16\2\u00b8\31\3\2\2\2\u00b9\u00ba\58\35\2\u00ba")
        buf.write("\u00bc\7\r\2\2\u00bb\u00bd\7E\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c7\5")
        buf.write("&\24\2\u00bf\u00c1\7%\2\2\u00c0\u00c2\7E\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c4\7\r\2\2\u00c4\u00c6\5&\24\2\u00c5\u00bf\3\2\2\2")
        buf.write("\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8\33\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cc")
        buf.write("\7 \2\2\u00cb\u00cd\7G\2\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00d0\5\36\20\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d2\7!\2\2\u00d2\35\3\2\2\2\u00d3\u00d4\5 \21")
        buf.write("\2\u00d4\u00d5\5T+\2\u00d5\u00d7\3\2\2\2\u00d6\u00d3\3")
        buf.write("\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\37\3\2\2\2\u00da\u00e2\5\6\4\2\u00db\u00e2")
        buf.write("\5\f\7\2\u00dc\u00e2\5\24\13\2\u00dd\u00e2\5\"\22\2\u00de")
        buf.write("\u00e2\5.\30\2\u00df\u00e2\5\60\31\2\u00e0\u00e2\5(\25")
        buf.write("\2\u00e1\u00da\3\2\2\2\u00e1\u00db\3\2\2\2\u00e1\u00dc")
        buf.write("\3\2\2\2\u00e1\u00dd\3\2\2\2\u00e1\u00de\3\2\2\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2!\3\2\2\2\u00e3")
        buf.write("\u00e7\5$\23\2\u00e4\u00e7\5*\26\2\u00e5\u00e7\5\26\f")
        buf.write("\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7#\3\2\2\2\u00e8\u00e9\5B\"\2\u00e9%\3\2")
        buf.write("\2\2\u00ea\u00ec\5R*\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00ef\7E\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u0100\3\2\2\2")
        buf.write("\u00f0\u00f2\7\"\2\2\u00f1\u00f3\7E\2\2\u00f2\u00f1\3")
        buf.write("\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00fa")
        buf.write("\7D\2\2\u00f5\u00f7\7%\2\2\u00f6\u00f8\7E\2\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fb\7D\2\2\u00fa\u00f5\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fd\3\2\2\2\u00fc\u00fe\7E\2\2\u00fd\u00fc\3")
        buf.write("\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101")
        buf.write("\7#\2\2\u0100\u00f0\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\'\3\2\2\2\u0102\u0103\7\22\2\2\u0103\u0105\7\r\2\2\u0104")
        buf.write("\u0106\7E\2\2\u0105\u0104\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\u0109\5&\24\2\u0108\u010a\7")
        buf.write("E\2\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u010d\5,\27\2\u010c\u010e\7E\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\5\24\13\2\u0110)\3\2\2\2\u0111\u0112\7\r")
        buf.write("\2\2\u0112\u0113\5,\27\2\u0113\u0114\5B\"\2\u0114+\3\2")
        buf.write("\2\2\u0115\u0116\7$\2\2\u0116-\3\2\2\2\u0117\u011b\7\7")
        buf.write("\2\2\u0118\u0119\5\"\22\2\u0119\u011a\7&\2\2\u011a\u011c")
        buf.write("\3\2\2\2\u011b\u0118\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u011e\5B\"\2\u011e\u0124\5\34\17")
        buf.write("\2\u011f\u0122\7\b\2\2\u0120\u0123\5.\30\2\u0121\u0123")
        buf.write("\5\34\17\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0125\3\2\2\2\u0124\u011f\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125/\3\2\2\2\u0126\u0127\5\62\32\2\u0127\61\3\2\2\2")
        buf.write("\u0128\u012c\7\4\2\2\u0129\u012a\5\"\22\2\u012a\u012b")
        buf.write("\7&\2\2\u012b\u012d\3\2\2\2\u012c\u0129\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u0130\5B\"\2")
        buf.write("\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3")
        buf.write("\2\2\2\u0131\u0135\7 \2\2\u0132\u0134\5\64\33\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3")
        buf.write("\2\2\2\u0138\u0139\7!\2\2\u0139\63\3\2\2\2\u013a\u013b")
        buf.write("\5\66\34\2\u013b\u013d\7\'\2\2\u013c\u013e\5\36\20\2\u013d")
        buf.write("\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\65\3\2\2\2\u013f")
        buf.write("\u0140\7\5\2\2\u0140\u0143\5B\"\2\u0141\u0143\7\6\2\2")
        buf.write("\u0142\u013f\3\2\2\2\u0142\u0141\3\2\2\2\u0143\67\3\2")
        buf.write("\2\2\u0144\u0145\t\2\2\2\u01459\3\2\2\2\u0146\u0147\t")
        buf.write("\3\2\2\u0147;\3\2\2\2\u0148\u0149\t\4\2\2\u0149=\3\2\2")
        buf.write("\2\u014a\u014b\t\5\2\2\u014b?\3\2\2\2\u014c\u014d\5D#")
        buf.write("\2\u014d\u014f\5<\37\2\u014e\u0150\5:\36\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\5D#\2\u0152\u0158\3\2\2\2\u0153\u0154\5D#\2\u0154")
        buf.write("\u0155\5> \2\u0155\u0156\5D#\2\u0156\u0158\3\2\2\2\u0157")
        buf.write("\u014c\3\2\2\2\u0157\u0153\3\2\2\2\u0158A\3\2\2\2\u0159")
        buf.write("\u0161\5D#\2\u015a\u0161\5@!\2\u015b\u015c\5D#\2\u015c")
        buf.write("\u015d\t\6\2\2\u015d\u015e\5D#\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u0161\5\24\13\2\u0160\u0159\3\2\2\2\u0160\u015a\3\2\2")
        buf.write("\2\u0160\u015b\3\2\2\2\u0160\u015f\3\2\2\2\u0161C\3\2")
        buf.write("\2\2\u0162\u0163\5F$\2\u0163E\3\2\2\2\u0164\u016b\5H%")
        buf.write("\2\u0165\u016b\5N(\2\u0166\u0167\7\36\2\2\u0167\u0168")
        buf.write("\5B\"\2\u0168\u0169\7\37\2\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u0164\3\2\2\2\u016a\u0165\3\2\2\2\u016a\u0166\3\2\2\2")
        buf.write("\u016bG\3\2\2\2\u016c\u016d\5J&\2\u016dI\3\2\2\2\u016e")
        buf.write("\u0174\7\f\2\2\u016f\u0174\5L\'\2\u0170\u0174\5P)\2\u0171")
        buf.write("\u0174\7@\2\2\u0172\u0174\7A\2\2\u0173\u016e\3\2\2\2\u0173")
        buf.write("\u016f\3\2\2\2\u0173\u0170\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0172\3\2\2\2\u0174K\3\2\2\2\u0175\u0176\t\7\2")
        buf.write("\2\u0176M\3\2\2\2\u0177\u0178\7\r\2\2\u0178O\3\2\2\2\u0179")
        buf.write("\u017a\t\b\2\2\u017aQ\3\2\2\2\u017b\u017f\7 \2\2\u017c")
        buf.write("\u017e\7E\2\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2")
        buf.write("\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0183\3")
        buf.write("\2\2\2\u0181\u017f\3\2\2\2\u0182\u0184\5\n\6\2\u0183\u0182")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0188\3\2\2\2\u0185")
        buf.write("\u0187\7E\2\2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3")
        buf.write("\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c\7!\2\2\u018cS\3")
        buf.write("\2\2\2\u018d\u0192\7&\2\2\u018e\u018f\7&\2\2\u018f\u0192")
        buf.write("\7\2\2\3\u0190\u0192\6+\3\2\u0191\u018d\3\2\2\2\u0191")
        buf.write("\u018e\3\2\2\2\u0191\u0190\3\2\2\2\u0192U\3\2\2\2\65W")
        buf.write("[aev~\u0085\u008a\u0092\u0095\u009b\u009f\u00a3\u00a6")
        buf.write("\u00aa\u00af\u00bc\u00c1\u00c7\u00cc\u00cf\u00d8\u00e1")
        buf.write("\u00e6\u00eb\u00ee\u00f2\u00f7\u00fa\u00fd\u0100\u0105")
        buf.write("\u0109\u010d\u011b\u0122\u0124\u012c\u012f\u0135\u013d")
        buf.write("\u0142\u014f\u0157\u0160\u016a\u0173\u017f\u0183\u0188")
        buf.write("\u0191")
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
    RULE_functionCall = 9
    RULE_drawClause = 10
    RULE_shapeDecl = 11
    RULE_shapeSpec = 12
    RULE_block = 13
    RULE_statementList = 14
    RULE_statement = 15
    RULE_simpleStmt = 16
    RULE_expressionStmt = 17
    RULE_shapeArguments = 18
    RULE_assignmentDeclarationStmt = 19
    RULE_assignment = 20
    RULE_assign_op = 21
    RULE_ifStmt = 22
    RULE_switchStmt = 23
    RULE_exprSwitchStmt = 24
    RULE_exprCaseClause = 25
    RULE_exprSwitchCase = 26
    RULE_typeName = 27
    RULE_relationDetailOp = 28
    RULE_singleLevelRelationOp = 29
    RULE_multiLevelRelationOp = 30
    RULE_relationExpr = 31
    RULE_expression = 32
    RULE_primaryExpr = 33
    RULE_operand = 34
    RULE_literal = 35
    RULE_basicLit = 36
    RULE_integer = 37
    RULE_operandName = 38
    RULE_string_ = 39
    RULE_arguments = 40
    RULE_eos = 41

    ruleNames =  [ "sourceFile", "viewportClause", "declaration", "identifierList", 
                   "expressionList", "functionDecl", "signature", "parameters", 
                   "parameterDecl", "functionCall", "drawClause", "shapeDecl", 
                   "shapeSpec", "block", "statementList", "statement", "simpleStmt", 
                   "expressionStmt", "shapeArguments", "assignmentDeclarationStmt", 
                   "assignment", "assign_op", "ifStmt", "switchStmt", "exprSwitchStmt", 
                   "exprCaseClause", "exprSwitchCase", "typeName", "relationDetailOp", 
                   "singleLevelRelationOp", "multiLevelRelationOp", "relationExpr", 
                   "expression", "primaryExpr", "operand", "literal", "basicLit", 
                   "integer", "operandName", "string_", "arguments", "eos" ]

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceFile" ):
                return visitor.visitSourceFile(self)
            else:
                return visitor.visitChildren(self)




    def sourceFile(self):

        localctx = TwoDimParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.VIEWPORT:
                self.state = 84
                self.viewportClause()


            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [TwoDimParser.FUNC]:
                        self.state = 87
                        self.functionDecl()
                        pass
                    elif token in [TwoDimParser.SQUARE, TwoDimParser.RECT, TwoDimParser.CIRCLE, TwoDimParser.TRIANGLE, TwoDimParser.SHAPE]:
                        self.state = 88
                        self.declaration()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 91
                    self.eos() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 98
                self.statementList()


            self.state = 101
            self.drawClause()
            self.state = 102
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitViewportClause" ):
                return visitor.visitViewportClause(self)
            else:
                return visitor.visitChildren(self)




    def viewportClause(self):

        localctx = TwoDimParser.ViewportClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_viewportClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(TwoDimParser.VIEWPORT)
            self.state = 105
            self.match(TwoDimParser.DECIMAL_LIT)
            self.state = 106
            self.match(TwoDimParser.DECIMAL_LIT)
            self.state = 107
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = TwoDimParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = TwoDimParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifierList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 112
                    self.match(TwoDimParser.COMMA)
                    self.state = 113
                    self.match(TwoDimParser.IDENTIFIER) 
                self.state = 118
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = TwoDimParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.expression()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.COMMA:
                self.state = 120
                self.match(TwoDimParser.COMMA)
                self.state = 121
                self.expression()
                self.state = 126
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = TwoDimParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(TwoDimParser.FUNC)
            self.state = 128
            self.match(TwoDimParser.IDENTIFIER)

            self.state = 129
            self.signature()
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 130
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignature" ):
                return visitor.visitSignature(self)
            else:
                return visitor.visitChildren(self)




    def signature(self):

        localctx = TwoDimParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_signature)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                if not self.noTerminatorAfterParams(1):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.noTerminatorAfterParams(1)")
                self.state = 134
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = TwoDimParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(TwoDimParser.L_PAREN)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE))) != 0):
                self.state = 139
                self.parameterDecl()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TwoDimParser.COMMA:
                    self.state = 140
                    self.match(TwoDimParser.COMMA)
                    self.state = 141
                    self.parameterDecl()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 149
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterDecl" ):
                return visitor.visitParameterDecl(self)
            else:
                return visitor.visitChildren(self)




    def parameterDecl(self):

        localctx = TwoDimParser.ParameterDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.typeName()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.IDENTIFIER:
                self.state = 152
                self.identifierList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.WS)
            else:
                return self.getToken(TwoDimParser.WS, i)

        def operandName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.OperandNameContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.OperandNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = TwoDimParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.WS:
                self.state = 156
                self.match(TwoDimParser.WS)


            self.state = 159
            self.match(TwoDimParser.L_PAREN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.WS:
                self.state = 160
                self.match(TwoDimParser.WS)


            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.IDENTIFIER:
                self.state = 163
                self.operandName()


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.COMMA:
                self.state = 166
                self.match(TwoDimParser.COMMA)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.WS:
                    self.state = 167
                    self.match(TwoDimParser.WS)


                self.state = 170
                self.operandName()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(TwoDimParser.R_PAREN)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawClause" ):
                return visitor.visitDrawClause(self)
            else:
                return visitor.visitChildren(self)




    def drawClause(self):

        localctx = TwoDimParser.DrawClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_drawClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(TwoDimParser.DRAW)
            self.state = 179
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShapeDecl" ):
                return visitor.visitShapeDecl(self)
            else:
                return visitor.visitChildren(self)




    def shapeDecl(self):

        localctx = TwoDimParser.ShapeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_shapeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShapeSpec" ):
                return visitor.visitShapeSpec(self)
            else:
                return visitor.visitChildren(self)




    def shapeSpec(self):

        localctx = TwoDimParser.ShapeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_shapeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.typeName()
            self.state = 184
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 185
                self.match(TwoDimParser.WS)


            self.state = 188
            self.shapeArguments()
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 189
                    self.match(TwoDimParser.COMMA)
                    self.state = 191
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==TwoDimParser.WS:
                        self.state = 190
                        self.match(TwoDimParser.WS)


                    self.state = 193
                    self.match(TwoDimParser.IDENTIFIER)
                    self.state = 194
                    self.shapeArguments() 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def TERMINATOR(self):
            return self.getToken(TwoDimParser.TERMINATOR, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = TwoDimParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(TwoDimParser.L_CURLY)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.TERMINATOR:
                self.state = 201
                self.match(TwoDimParser.TERMINATOR)


            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.SWITCH) | (1 << TwoDimParser.IF) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE) | (1 << TwoDimParser.DRAW) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT))) != 0) or _la==TwoDimParser.RAW_STRING_LIT or _la==TwoDimParser.INTERPRETED_STRING_LIT:
                self.state = 204
                self.statementList()


            self.state = 207
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = TwoDimParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 209
                    self.statement()
                    self.state = 210
                    self.eos()

                else:
                    raise NoViableAltException(self)
                self.state = 214 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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


        def functionDecl(self):
            return self.getTypedRuleContext(TwoDimParser.FunctionDeclContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(TwoDimParser.FunctionCallContext,0)


        def simpleStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SimpleStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(TwoDimParser.IfStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SwitchStmtContext,0)


        def assignmentDeclarationStmt(self):
            return self.getTypedRuleContext(TwoDimParser.AssignmentDeclarationStmtContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TwoDimParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.functionDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.simpleStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 221
                self.switchStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 222
                self.assignmentDeclarationStmt()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStmt" ):
                return visitor.visitSimpleStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleStmt(self):

        localctx = TwoDimParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_simpleStmt)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.expressionStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStmt" ):
                return visitor.visitExpressionStmt(self)
            else:
                return visitor.visitChildren(self)




    def expressionStmt(self):

        localctx = TwoDimParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShapeArguments" ):
                return visitor.visitShapeArguments(self)
            else:
                return visitor.visitChildren(self)




    def shapeArguments(self):

        localctx = TwoDimParser.ShapeArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_shapeArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 232
                self.arguments()


            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 235
                self.match(TwoDimParser.WS)


            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(TwoDimParser.L_BRACKET)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.WS:
                    self.state = 239
                    self.match(TwoDimParser.WS)


                self.state = 242
                self.match(TwoDimParser.SIZE_LIT)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.COMMA:
                    self.state = 243
                    self.match(TwoDimParser.COMMA)
                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==TwoDimParser.WS:
                        self.state = 244
                        self.match(TwoDimParser.WS)


                    self.state = 247
                    self.match(TwoDimParser.SIZE_LIT)


                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.WS:
                    self.state = 250
                    self.match(TwoDimParser.WS)


                self.state = 253
                self.match(TwoDimParser.R_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentDeclarationStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHAPE(self):
            return self.getToken(TwoDimParser.SHAPE, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def shapeArguments(self):
            return self.getTypedRuleContext(TwoDimParser.ShapeArgumentsContext,0)


        def assign_op(self):
            return self.getTypedRuleContext(TwoDimParser.Assign_opContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(TwoDimParser.FunctionCallContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.WS)
            else:
                return self.getToken(TwoDimParser.WS, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_assignmentDeclarationStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentDeclarationStmt" ):
                listener.enterAssignmentDeclarationStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentDeclarationStmt" ):
                listener.exitAssignmentDeclarationStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentDeclarationStmt" ):
                return visitor.visitAssignmentDeclarationStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignmentDeclarationStmt(self):

        localctx = TwoDimParser.AssignmentDeclarationStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignmentDeclarationStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(TwoDimParser.SHAPE)
            self.state = 257
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(TwoDimParser.WS)


            self.state = 261
            self.shapeArguments()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.WS:
                self.state = 262
                self.match(TwoDimParser.WS)


            self.state = 265
            self.assign_op()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.WS:
                self.state = 266
                self.match(TwoDimParser.WS)


            self.state = 269
            self.functionCall()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = TwoDimParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 272
            self.assign_op()
            self.state = 273
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_op" ):
                return visitor.visitAssign_op(self)
            else:
                return visitor.visitChildren(self)




    def assign_op(self):

        localctx = TwoDimParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = TwoDimParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(TwoDimParser.IF)
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 278
                self.simpleStmt()
                self.state = 279
                self.match(TwoDimParser.SEMI)


            self.state = 283
            self.expression()
            self.state = 284
            self.block()
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 285
                self.match(TwoDimParser.ELSE)
                self.state = 288
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TwoDimParser.IF]:
                    self.state = 286
                    self.ifStmt()
                    pass
                elif token in [TwoDimParser.L_CURLY]:
                    self.state = 287
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStmt" ):
                return visitor.visitSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def switchStmt(self):

        localctx = TwoDimParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_switchStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSwitchStmt" ):
                return visitor.visitExprSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprSwitchStmt(self):

        localctx = TwoDimParser.ExprSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exprSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(TwoDimParser.SWITCH)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 295
                self.simpleStmt()
                self.state = 296
                self.match(TwoDimParser.SEMI)


            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (TwoDimParser.NIL_LIT - 10)) | (1 << (TwoDimParser.IDENTIFIER - 10)) | (1 << (TwoDimParser.L_PAREN - 10)) | (1 << (TwoDimParser.DECIMAL_LIT - 10)) | (1 << (TwoDimParser.FLOAT_LIT - 10)) | (1 << (TwoDimParser.RUNE_LIT - 10)) | (1 << (TwoDimParser.RAW_STRING_LIT - 10)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 10)))) != 0):
                self.state = 300
                self.expression()


            self.state = 303
            self.match(TwoDimParser.L_CURLY)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.CASE or _la==TwoDimParser.DEFAULT:
                self.state = 304
                self.exprCaseClause()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprCaseClause" ):
                return visitor.visitExprCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def exprCaseClause(self):

        localctx = TwoDimParser.ExprCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.exprSwitchCase()
            self.state = 313
            self.match(TwoDimParser.COLON)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.SWITCH) | (1 << TwoDimParser.IF) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.SQUARE) | (1 << TwoDimParser.RECT) | (1 << TwoDimParser.CIRCLE) | (1 << TwoDimParser.TRIANGLE) | (1 << TwoDimParser.SHAPE) | (1 << TwoDimParser.DRAW) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT))) != 0) or _la==TwoDimParser.RAW_STRING_LIT or _la==TwoDimParser.INTERPRETED_STRING_LIT:
                self.state = 314
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSwitchCase" ):
                return visitor.visitExprSwitchCase(self)
            else:
                return visitor.visitChildren(self)




    def exprSwitchCase(self):

        localctx = TwoDimParser.ExprSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exprSwitchCase)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(TwoDimParser.CASE)
                self.state = 318
                self.expression()
                pass
            elif token in [TwoDimParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = TwoDimParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
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


    class RelationDetailOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INNER(self):
            return self.getToken(TwoDimParser.INNER, 0)

        def OUTER(self):
            return self.getToken(TwoDimParser.OUTER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_relationDetailOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationDetailOp" ):
                listener.enterRelationDetailOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationDetailOp" ):
                listener.exitRelationDetailOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationDetailOp" ):
                return visitor.visitRelationDetailOp(self)
            else:
                return visitor.visitChildren(self)




    def relationDetailOp(self):

        localctx = TwoDimParser.RelationDetailOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_relationDetailOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            _la = self._input.LA(1)
            if not(_la==TwoDimParser.OUTER or _la==TwoDimParser.INNER):
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


    class SingleLevelRelationOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(TwoDimParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(TwoDimParser.RIGHT, 0)

        def TOP(self):
            return self.getToken(TwoDimParser.TOP, 0)

        def BOT(self):
            return self.getToken(TwoDimParser.BOT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_singleLevelRelationOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleLevelRelationOp" ):
                listener.enterSingleLevelRelationOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleLevelRelationOp" ):
                listener.exitSingleLevelRelationOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleLevelRelationOp" ):
                return visitor.visitSingleLevelRelationOp(self)
            else:
                return visitor.visitChildren(self)




    def singleLevelRelationOp(self):

        localctx = TwoDimParser.SingleLevelRelationOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_singleLevelRelationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.LEFT) | (1 << TwoDimParser.RIGHT) | (1 << TwoDimParser.TOP) | (1 << TwoDimParser.BOT))) != 0)):
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


    class MultiLevelRelationOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(TwoDimParser.IN, 0)

        def ON(self):
            return self.getToken(TwoDimParser.ON, 0)

        def UNDER(self):
            return self.getToken(TwoDimParser.UNDER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_multiLevelRelationOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiLevelRelationOp" ):
                listener.enterMultiLevelRelationOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiLevelRelationOp" ):
                listener.exitMultiLevelRelationOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiLevelRelationOp" ):
                return visitor.visitMultiLevelRelationOp(self)
            else:
                return visitor.visitChildren(self)




    def multiLevelRelationOp(self):

        localctx = TwoDimParser.MultiLevelRelationOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_multiLevelRelationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.ON) | (1 << TwoDimParser.UNDER) | (1 << TwoDimParser.IN))) != 0)):
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


    class RelationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.PrimaryExprContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.PrimaryExprContext,i)


        def singleLevelRelationOp(self):
            return self.getTypedRuleContext(TwoDimParser.SingleLevelRelationOpContext,0)


        def relationDetailOp(self):
            return self.getTypedRuleContext(TwoDimParser.RelationDetailOpContext,0)


        def multiLevelRelationOp(self):
            return self.getTypedRuleContext(TwoDimParser.MultiLevelRelationOpContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_relationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationExpr" ):
                listener.enterRelationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationExpr" ):
                listener.exitRelationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationExpr" ):
                return visitor.visitRelationExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationExpr(self):

        localctx = TwoDimParser.RelationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_relationExpr)
        self._la = 0 # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.primaryExpr()
                self.state = 331
                self.singleLevelRelationOp()
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.OUTER or _la==TwoDimParser.INNER:
                    self.state = 332
                    self.relationDetailOp()


                self.state = 335
                self.primaryExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.primaryExpr()
                self.state = 338
                self.multiLevelRelationOp()
                self.state = 339
                self.primaryExpr()
                pass


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


        def relationExpr(self):
            return self.getTypedRuleContext(TwoDimParser.RelationExprContext,0)


        def PLUS(self):
            return self.getToken(TwoDimParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(TwoDimParser.MINUS, 0)

        def functionCall(self):
            return self.getTypedRuleContext(TwoDimParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = TwoDimParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.primaryExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.relationExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.primaryExpr()
                self.state = 346
                _la = self._input.LA(1)
                if not(_la==TwoDimParser.PLUS or _la==TwoDimParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 347
                self.primaryExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.functionCall()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = TwoDimParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = TwoDimParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operand)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.NIL_LIT, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.literal()
                pass
            elif token in [TwoDimParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.operandName()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.match(TwoDimParser.L_PAREN)
                self.state = 357
                self.expression()
                self.state = 358
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = TwoDimParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicLit" ):
                return visitor.visitBasicLit(self)
            else:
                return visitor.visitChildren(self)




    def basicLit(self):

        localctx = TwoDimParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_basicLit)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(TwoDimParser.NIL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.integer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 366
                self.string_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 367
                self.match(TwoDimParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 368
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = TwoDimParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandName" ):
                return visitor.visitOperandName(self)
            else:
                return visitor.visitChildren(self)




    def operandName(self):

        localctx = TwoDimParser.OperandNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_operandName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_" ):
                return visitor.visitString_(self)
            else:
                return visitor.visitChildren(self)




    def string_(self):

        localctx = TwoDimParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
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

        def L_CURLY(self):
            return self.getToken(TwoDimParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(TwoDimParser.R_CURLY, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.WS)
            else:
                return self.getToken(TwoDimParser.WS, i)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = TwoDimParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(TwoDimParser.L_CURLY)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 378
                    self.match(TwoDimParser.WS) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (TwoDimParser.NIL_LIT - 10)) | (1 << (TwoDimParser.IDENTIFIER - 10)) | (1 << (TwoDimParser.L_PAREN - 10)) | (1 << (TwoDimParser.DECIMAL_LIT - 10)) | (1 << (TwoDimParser.FLOAT_LIT - 10)) | (1 << (TwoDimParser.RUNE_LIT - 10)) | (1 << (TwoDimParser.RAW_STRING_LIT - 10)) | (1 << (TwoDimParser.INTERPRETED_STRING_LIT - 10)))) != 0):
                self.state = 384
                self.expressionList()


            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.WS:
                self.state = 387
                self.match(TwoDimParser.WS)
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 393
            self.match(TwoDimParser.R_CURLY)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = TwoDimParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_eos)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(TwoDimParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.match(TwoDimParser.SEMI)
                self.state = 397
                self.match(TwoDimParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
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
        self._predicates[41] = self.eos_sempred
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
                return self.checkPreviousTokenText("}")
         




