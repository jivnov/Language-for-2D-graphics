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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u02a0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\3\2\3\2\5\2")
        buf.write("\u00a2\n\2\3\2\3\2\7\2\u00a6\n\2\f\2\16\2\u00a9\13\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00b4\n\4\f\4\16")
        buf.write("\4\u00b7\13\4\3\4\5\4\u00ba\n\4\3\5\5\5\u00bd\n\5\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\5\7\u00c5\n\7\3\b\3\b\3\b\7\b\u00ca")
        buf.write("\n\b\f\b\16\b\u00cd\13\b\3\t\3\t\3\t\7\t\u00d2\n\t\f\t")
        buf.write("\16\t\u00d5\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00dd\n\n")
        buf.write("\f\n\16\n\u00e0\13\n\3\n\5\n\u00e3\n\n\3\13\3\13\5\13")
        buf.write("\u00e7\n\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00ef\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00f6\n\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u00ff\n\17\f\17\16\17\u0102\13\17\3")
        buf.write("\17\5\17\u0105\n\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\5\21\u010e\n\21\3\21\3\21\3\22\3\22\3\22\6\22\u0115\n")
        buf.write("\22\r\22\16\22\u0116\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u011f\n\23\3\24\3\24\3\24\3\24\5\24\u0125\n\24\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\5\30\u0131")
        buf.write("\n\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u013f\n\33\3\33\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0146\n\33\5\33\u0148\n\33\3\34\3\34\5\34\u014c\n")
        buf.write("\34\3\35\3\35\3\35\3\35\5\35\u0152\n\35\3\35\5\35\u0155")
        buf.write("\n\35\3\35\3\35\7\35\u0159\n\35\f\35\16\35\u015c\13\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\5\36\u0163\n\36\3\37\3\37\3")
        buf.write("\37\5\37\u0168\n\37\3 \3 \3 \3 \5 \u016e\n \3 \3 \3 \7")
        buf.write(" \u0173\n \f \16 \u0176\13 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\5\"\u0183\n\"\3#\3#\3#\5#\u0188\n#\3$\3$\5")
        buf.write("$\u018c\n$\3$\3$\3$\5$\u0191\n$\7$\u0193\n$\f$\16$\u0196")
        buf.write("\13$\3%\3%\3%\5%\u019b\n%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u01a5")
        buf.write("\n&\3\'\3\'\5\'\u01a9\n\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\5*\u01b7\n*\3+\3+\3+\3,\3,\3,\3,\3,\5,\u01c1\n")
        buf.write(",\3-\3-\5-\u01c5\n-\3.\3.\3.\3.\7.\u01cb\n.\f.\16.\u01ce")
        buf.write("\13.\3.\5.\u01d1\n.\5.\u01d3\n.\3.\3.\3/\5/\u01d8\n/\3")
        buf.write("/\3/\3\60\3\60\3\60\5\60\u01df\n\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\7\60\u01f0\n\60\f\60\16\60\u01f3\13\60\3\61\3\61\3\61")
        buf.write("\5\61\u01f8\n\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0200")
        buf.write("\n\61\7\61\u0202\n\61\f\61\16\61\u0205\13\61\3\62\3\62")
        buf.write("\3\62\5\62\u020a\n\62\3\63\3\63\3\63\3\63\5\63\u0210\n")
        buf.write("\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u021b\n\64\3\65\3\65\3\65\5\65\u0220\n\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\5\66\u0227\n\66\3\67\3\67\38\38\58\u022d")
        buf.write("\n8\39\39\39\39\3:\3:\3:\3;\3;\3;\3;\5;\u023a\n;\3<\3")
        buf.write("<\3<\5<\u023f\n<\5<\u0241\n<\3<\3<\3=\3=\3=\7=\u0248\n")
        buf.write("=\f=\16=\u024b\13=\3>\3>\3>\5>\u0250\n>\3>\3>\3?\3?\3")
        buf.write("?\5?\u0257\n?\3@\3@\5@\u025b\n@\3A\3A\3A\3A\3A\5A\u0262")
        buf.write("\nA\3A\5A\u0265\nA\3B\3B\3C\5C\u026a\nC\3C\3C\3D\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\5G\u0280")
        buf.write("\nG\5G\u0282\nG\3G\5G\u0285\nG\5G\u0287\nG\3G\3G\3H\3")
        buf.write("H\3H\3H\3I\3I\3I\3I\3I\5I\u0294\nI\3I\3I\5I\u0298\nI\3")
        buf.write("J\3J\3J\3J\5J\u029e\nJ\3J\2\4^`K\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\2\13\4\2\r\r\"\"\3\2#$")
        buf.write("\3\2\64\65\4\2.\62\678\4\2--\64\66\3\2\',\3\2\638\4\2")
        buf.write("99;;\3\2<=\2\u02b9\2\u0094\3\2\2\2\4\u00aa\3\2\2\2\6\u00ad")
        buf.write("\3\2\2\2\b\u00bc\3\2\2\2\n\u00c0\3\2\2\2\f\u00c4\3\2\2")
        buf.write("\2\16\u00c6\3\2\2\2\20\u00ce\3\2\2\2\22\u00d6\3\2\2\2")
        buf.write("\24\u00e4\3\2\2\2\26\u00ea\3\2\2\2\30\u00f0\3\2\2\2\32")
        buf.write("\u00f7\3\2\2\2\34\u0104\3\2\2\2\36\u0106\3\2\2\2 \u010b")
        buf.write("\3\2\2\2\"\u0114\3\2\2\2$\u011e\3\2\2\2&\u0124\3\2\2\2")
        buf.write("(\u0126\3\2\2\2*\u0128\3\2\2\2,\u012b\3\2\2\2.\u0130\3")
        buf.write("\2\2\2\60\u0134\3\2\2\2\62\u0136\3\2\2\2\64\u013a\3\2")
        buf.write("\2\2\66\u014b\3\2\2\28\u014d\3\2\2\2:\u015f\3\2\2\2<\u0167")
        buf.write("\3\2\2\2>\u0169\3\2\2\2@\u0179\3\2\2\2B\u017f\3\2\2\2")
        buf.write("D\u0187\3\2\2\2F\u018b\3\2\2\2H\u019a\3\2\2\2J\u01a4\3")
        buf.write("\2\2\2L\u01a8\3\2\2\2N\u01aa\3\2\2\2P\u01ac\3\2\2\2R\u01b6")
        buf.write("\3\2\2\2T\u01b8\3\2\2\2V\u01c0\3\2\2\2X\u01c4\3\2\2\2")
        buf.write("Z\u01c6\3\2\2\2\\\u01d7\3\2\2\2^\u01de\3\2\2\2`\u01f7")
        buf.write("\3\2\2\2b\u0209\3\2\2\2d\u020b\3\2\2\2f\u021a\3\2\2\2")
        buf.write("h\u021f\3\2\2\2j\u0226\3\2\2\2l\u0228\3\2\2\2n\u022c\3")
        buf.write("\2\2\2p\u022e\3\2\2\2r\u0232\3\2\2\2t\u0239\3\2\2\2v\u023b")
        buf.write("\3\2\2\2x\u0244\3\2\2\2z\u024f\3\2\2\2|\u0256\3\2\2\2")
        buf.write("~\u025a\3\2\2\2\u0080\u0261\3\2\2\2\u0082\u0266\3\2\2")
        buf.write("\2\u0084\u0269\3\2\2\2\u0086\u026d\3\2\2\2\u0088\u0271")
        buf.write("\3\2\2\2\u008a\u0275\3\2\2\2\u008c\u027a\3\2\2\2\u008e")
        buf.write("\u028a\3\2\2\2\u0090\u0297\3\2\2\2\u0092\u029d\3\2\2\2")
        buf.write("\u0094\u0095\5\4\3\2\u0095\u009b\5\u0092J\2\u0096\u0097")
        buf.write("\5\6\4\2\u0097\u0098\5\u0092J\2\u0098\u009a\3\2\2\2\u0099")
        buf.write("\u0096\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u00a7\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u00a2\5\26\f\2\u009f\u00a2\5\30\r\2\u00a0")
        buf.write("\u00a2\5\f\7\2\u00a1\u009e\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\5")
        buf.write("\u0092J\2\u00a4\u00a6\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a6")
        buf.write("\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2")
        buf.write("\u00a8\3\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7\n\2")
        buf.write("\2\u00ab\u00ac\7\r\2\2\u00ac\5\3\2\2\2\u00ad\u00b9\7\13")
        buf.write("\2\2\u00ae\u00ba\5\b\5\2\u00af\u00b5\7\30\2\2\u00b0\u00b1")
        buf.write("\5\b\5\2\u00b1\u00b2\5\u0092J\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00b0\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3")
        buf.write("\2\2\2\u00b8\u00ba\7\31\2\2\u00b9\u00ae\3\2\2\2\u00b9")
        buf.write("\u00af\3\2\2\2\u00ba\7\3\2\2\2\u00bb\u00bd\t\2\2\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\5\n\6\2\u00bf\t\3\2\2\2\u00c0\u00c1\5\u0082")
        buf.write("B\2\u00c1\13\3\2\2\2\u00c2\u00c5\5\22\n\2\u00c3\u00c5")
        buf.write("\5\34\17\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\r\3\2\2\2\u00c6\u00cb\7\r\2\2\u00c7\u00c8\7\37\2\2\u00c8")
        buf.write("\u00ca\7\r\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cd\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\17\3\2")
        buf.write("\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d3\5^\60\2\u00cf\u00d0")
        buf.write("\7\37\2\2\u00d0\u00d2\5^\60\2\u00d1\u00cf\3\2\2\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\21\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00e2\7\t")
        buf.write("\2\2\u00d7\u00e3\5\24\13\2\u00d8\u00de\7\30\2\2\u00d9")
        buf.write("\u00da\5\24\13\2\u00da\u00db\5\u0092J\2\u00db\u00dd\3")
        buf.write("\2\2\2\u00dc\u00d9\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e1\u00e3\7\31\2\2\u00e2\u00d7\3\2\2")
        buf.write("\2\u00e2\u00d8\3\2\2\2\u00e3\23\3\2\2\2\u00e4\u00e6\7")
        buf.write("\r\2\2\u00e5\u00e7\7\36\2\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\5J&\2\u00e9")
        buf.write("\25\3\2\2\2\u00ea\u00eb\7\3\2\2\u00eb\u00ec\7\r\2\2\u00ec")
        buf.write("\u00ee\5V,\2\u00ed\u00ef\5 \21\2\u00ee\u00ed\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\27\3\2\2\2\u00f0\u00f1\7\3\2\2\u00f1")
        buf.write("\u00f2\5\32\16\2\u00f2\u00f3\7\r\2\2\u00f3\u00f5\5V,\2")
        buf.write("\u00f4\u00f6\5 \21\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\31\3\2\2\2\u00f7\u00f8\5Z.\2\u00f8\33\3\2")
        buf.write("\2\2\u00f9\u0105\5\36\20\2\u00fa\u0100\7\30\2\2\u00fb")
        buf.write("\u00fc\5\36\20\2\u00fc\u00fd\5\u0092J\2\u00fd\u00ff\3")
        buf.write("\2\2\2\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0103\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u0105\7\31\2\2\u0104\u00f9\3\2\2")
        buf.write("\2\u0104\u00fa\3\2\2\2\u0105\35\3\2\2\2\u0106\u0107\5")
        buf.write("J&\2\u0107\u0108\5\16\b\2\u0108\u0109\7\36\2\2\u0109\u010a")
        buf.write("\5\20\t\2\u010a\37\3\2\2\2\u010b\u010d\7\32\2\2\u010c")
        buf.write("\u010e\5\"\22\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2")
        buf.write("\2\u010e\u010f\3\2\2\2\u010f\u0110\7\33\2\2\u0110!\3\2")
        buf.write("\2\2\u0111\u0112\5$\23\2\u0112\u0113\5\u0092J\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0111\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117#\3\2\2")
        buf.write("\2\u0118\u011f\5\f\7\2\u0119\u011f\5\62\32\2\u011a\u011f")
        buf.write("\5&\24\2\u011b\u011f\5 \21\2\u011c\u011f\5\64\33\2\u011d")
        buf.write("\u011f\5\66\34\2\u011e\u0118\3\2\2\2\u011e\u0119\3\2\2")
        buf.write("\2\u011e\u011a\3\2\2\2\u011e\u011b\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011e\u011d\3\2\2\2\u011f%\3\2\2\2\u0120\u0125")
        buf.write("\5(\25\2\u0121\u0125\5*\26\2\u0122\u0125\5,\27\2\u0123")
        buf.write("\u0125\5\60\31\2\u0124\u0120\3\2\2\2\u0124\u0121\3\2\2")
        buf.write("\2\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\'\3\2")
        buf.write("\2\2\u0126\u0127\5^\60\2\u0127)\3\2\2\2\u0128\u0129\5")
        buf.write("^\60\2\u0129\u012a\t\3\2\2\u012a+\3\2\2\2\u012b\u012c")
        buf.write("\5\20\t\2\u012c\u012d\5.\30\2\u012d\u012e\5\20\t\2\u012e")
        buf.write("-\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u012f\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\7\36\2")
        buf.write("\2\u0133/\3\2\2\2\u0134\u0135\7 \2\2\u0135\61\3\2\2\2")
        buf.write("\u0136\u0137\7\r\2\2\u0137\u0138\7!\2\2\u0138\u0139\5")
        buf.write("$\23\2\u0139\63\3\2\2\2\u013a\u013e\7\7\2\2\u013b\u013c")
        buf.write("\5&\24\2\u013c\u013d\7 \2\2\u013d\u013f\3\2\2\2\u013e")
        buf.write("\u013b\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0141\5^\60\2\u0141\u0147\5 \21\2\u0142\u0145\7")
        buf.write("\b\2\2\u0143\u0146\5\64\33\2\u0144\u0146\5 \21\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146\u0148\3\2\2\2")
        buf.write("\u0147\u0142\3\2\2\2\u0147\u0148\3\2\2\2\u0148\65\3\2")
        buf.write("\2\2\u0149\u014c\58\35\2\u014a\u014c\5> \2\u014b\u0149")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c\67\3\2\2\2\u014d\u0151")
        buf.write("\7\4\2\2\u014e\u014f\5&\24\2\u014f\u0150\7 \2\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014e\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0154\3\2\2\2\u0153\u0155\5^\60\2\u0154\u0153\3")
        buf.write("\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u015a")
        buf.write("\7\32\2\2\u0157\u0159\5:\36\2\u0158\u0157\3\2\2\2\u0159")
        buf.write("\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7")
        buf.write("\33\2\2\u015e9\3\2\2\2\u015f\u0160\5<\37\2\u0160\u0162")
        buf.write("\7!\2\2\u0161\u0163\5\"\22\2\u0162\u0161\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163;\3\2\2\2\u0164\u0165\7\5\2\2\u0165")
        buf.write("\u0168\5\20\t\2\u0166\u0168\7\6\2\2\u0167\u0164\3\2\2")
        buf.write("\2\u0167\u0166\3\2\2\2\u0168=\3\2\2\2\u0169\u016d\7\4")
        buf.write("\2\2\u016a\u016b\5&\24\2\u016b\u016c\7 \2\2\u016c\u016e")
        buf.write("\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\5@!\2\u0170\u0174\7\32\2\2")
        buf.write("\u0171\u0173\5B\"\2\u0172\u0171\3\2\2\2\u0173\u0176\3")
        buf.write("\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7\33\2\2\u0178")
        buf.write("?\3\2\2\2\u0179\u017a\5`\61\2\u017a\u017b\7\"\2\2\u017b")
        buf.write("\u017c\7\30\2\2\u017c\u017d\7\t\2\2\u017d\u017e\7\31\2")
        buf.write("\2\u017eA\3\2\2\2\u017f\u0180\5D#\2\u0180\u0182\7!\2\2")
        buf.write("\u0181\u0183\5\"\22\2\u0182\u0181\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183C\3\2\2\2\u0184\u0185\7\5\2\2\u0185\u0188")
        buf.write("\5F$\2\u0186\u0188\7\6\2\2\u0187\u0184\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188E\3\2\2\2\u0189\u018c\5J&\2\u018a\u018c")
        buf.write("\7\f\2\2\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("\u0194\3\2\2\2\u018d\u0190\7\37\2\2\u018e\u0191\5J&\2")
        buf.write("\u018f\u0191\7\f\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3")
        buf.write("\2\2\2\u0191\u0193\3\2\2\2\u0192\u018d\3\2\2\2\u0193\u0196")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("G\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0198\5\20\t\2\u0198")
        buf.write("\u0199\7\36\2\2\u0199\u019b\3\2\2\2\u019a\u0197\3\2\2")
        buf.write("\2\u019a\u019b\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d")
        buf.write("\5^\60\2\u019dI\3\2\2\2\u019e\u01a5\5L\'\2\u019f\u01a5")
        buf.write("\5N(\2\u01a0\u01a1\7\30\2\2\u01a1\u01a2\5J&\2\u01a2\u01a3")
        buf.write("\7\31\2\2\u01a3\u01a5\3\2\2\2\u01a4\u019e\3\2\2\2\u01a4")
        buf.write("\u019f\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a5K\3\2\2\2\u01a6")
        buf.write("\u01a9\7\r\2\2\u01a7\u01a9\5p9\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9M\3\2\2\2\u01aa\u01ab\5T+\2\u01ab")
        buf.write("O\3\2\2\2\u01ac\u01ad\5J&\2\u01adQ\3\2\2\2\u01ae\u01af")
        buf.write("\6*\2\2\u01af\u01b0\7\r\2\2\u01b0\u01b1\5Z.\2\u01b1\u01b2")
        buf.write("\5X-\2\u01b2\u01b7\3\2\2\2\u01b3\u01b7\5L\'\2\u01b4\u01b5")
        buf.write("\7\r\2\2\u01b5\u01b7\5Z.\2\u01b6\u01ae\3\2\2\2\u01b6\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7S\3\2\2\2\u01b8\u01b9")
        buf.write("\7\3\2\2\u01b9\u01ba\5V,\2\u01baU\3\2\2\2\u01bb\u01bc")
        buf.write("\6,\3\2\u01bc\u01bd\5Z.\2\u01bd\u01be\5X-\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01c1\5Z.\2\u01c0\u01bb\3\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1W\3\2\2\2\u01c2\u01c5\5Z.\2\u01c3\u01c5")
        buf.write("\5J&\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5Y")
        buf.write("\3\2\2\2\u01c6\u01d2\7\30\2\2\u01c7\u01cc\5\\/\2\u01c8")
        buf.write("\u01c9\7\37\2\2\u01c9\u01cb\5\\/\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d1")
        buf.write("\7\37\2\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d3\3\2\2\2\u01d2\u01c7\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d3\u01d4\3\2\2\2\u01d4\u01d5\7\31\2\2\u01d5[\3\2\2")
        buf.write("\2\u01d6\u01d8\5\16\b\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\5J&\2\u01da]")
        buf.write("\3\2\2\2\u01db\u01dc\b\60\1\2\u01dc\u01df\5`\61\2\u01dd")
        buf.write("\u01df\5b\62\2\u01de\u01db\3\2\2\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01df\u01f1\3\2\2\2\u01e0\u01e1\f\7\2\2\u01e1\u01e2\t")
        buf.write("\5\2\2\u01e2\u01f0\5^\60\b\u01e3\u01e4\f\6\2\2\u01e4\u01e5")
        buf.write("\t\6\2\2\u01e5\u01f0\5^\60\7\u01e6\u01e7\f\5\2\2\u01e7")
        buf.write("\u01e8\t\7\2\2\u01e8\u01f0\5^\60\6\u01e9\u01ea\f\4\2\2")
        buf.write("\u01ea\u01eb\7&\2\2\u01eb\u01f0\5^\60\5\u01ec\u01ed\f")
        buf.write("\3\2\2\u01ed\u01ee\7%\2\2\u01ee\u01f0\5^\60\4\u01ef\u01e0")
        buf.write("\3\2\2\2\u01ef\u01e3\3\2\2\2\u01ef\u01e6\3\2\2\2\u01ef")
        buf.write("\u01e9\3\2\2\2\u01ef\u01ec\3\2\2\2\u01f0\u01f3\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2_\3\2\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\b\61\1\2\u01f5\u01f8")
        buf.write("\5f\64\2\u01f6\u01f8\5d\63\2\u01f7\u01f4\3\2\2\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8\u0203\3\2\2\2\u01f9\u01ff\f\3\2\2")
        buf.write("\u01fa\u01fb\7\"\2\2\u01fb\u0200\7\r\2\2\u01fc\u0200\5")
        buf.write("\u0088E\2\u01fd\u0200\5\u008aF\2\u01fe\u0200\5\u008cG")
        buf.write("\2\u01ff\u01fa\3\2\2\2\u01ff\u01fc\3\2\2\2\u01ff\u01fd")
        buf.write("\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200\u0202\3\2\2\2\u0201")
        buf.write("\u01f9\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204a\3\2\2\2\u0205\u0203\3\2\2")
        buf.write("\2\u0206\u020a\5`\61\2\u0207\u0208\t\b\2\2\u0208\u020a")
        buf.write("\5^\60\2\u0209\u0206\3\2\2\2\u0209\u0207\3\2\2\2\u020a")
        buf.write("c\3\2\2\2\u020b\u020c\5J&\2\u020c\u020d\7\30\2\2\u020d")
        buf.write("\u020f\5^\60\2\u020e\u0210\7\37\2\2\u020f\u020e\3\2\2")
        buf.write("\2\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212")
        buf.write("\7\31\2\2\u0212e\3\2\2\2\u0213\u021b\5h\65\2\u0214\u021b")
        buf.write("\5n8\2\u0215\u021b\5\u008eH\2\u0216\u0217\7\30\2\2\u0217")
        buf.write("\u0218\5^\60\2\u0218\u0219\7\31\2\2\u0219\u021b\3\2\2")
        buf.write("\2\u021a\u0213\3\2\2\2\u021a\u0214\3\2\2\2\u021a\u0215")
        buf.write("\3\2\2\2\u021a\u0216\3\2\2\2\u021bg\3\2\2\2\u021c\u0220")
        buf.write("\5j\66\2\u021d\u0220\5r:\2\u021e\u0220\5\u0086D\2\u021f")
        buf.write("\u021c\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u021e\3\2\2\2")
        buf.write("\u0220i\3\2\2\2\u0221\u0227\7\f\2\2\u0222\u0227\5l\67")
        buf.write("\2\u0223\u0227\5\u0082B\2\u0224\u0227\7:\2\2\u0225\u0227")
        buf.write("\7;\2\2\u0226\u0221\3\2\2\2\u0226\u0222\3\2\2\2\u0226")
        buf.write("\u0223\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0225\3\2\2\2")
        buf.write("\u0227k\3\2\2\2\u0228\u0229\t\t\2\2\u0229m\3\2\2\2\u022a")
        buf.write("\u022d\7\r\2\2\u022b\u022d\5p9\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022b\3\2\2\2\u022do\3\2\2\2\u022e\u022f\7\r\2\2\u022f")
        buf.write("\u0230\7\"\2\2\u0230\u0231\7\r\2\2\u0231q\3\2\2\2\u0232")
        buf.write("\u0233\5t;\2\u0233\u0234\5v<\2\u0234s\3\2\2\2\u0235\u0236")
        buf.write("\7\34\2\2\u0236\u0237\7\35\2\2\u0237\u023a\5P)\2\u0238")
        buf.write("\u023a\5L\'\2\u0239\u0235\3\2\2\2\u0239\u0238\3\2\2\2")
        buf.write("\u023au\3\2\2\2\u023b\u0240\7\32\2\2\u023c\u023e\5x=\2")
        buf.write("\u023d\u023f\7\37\2\2\u023e\u023d\3\2\2\2\u023e\u023f")
        buf.write("\3\2\2\2\u023f\u0241\3\2\2\2\u0240\u023c\3\2\2\2\u0240")
        buf.write("\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243\7\33\2")
        buf.write("\2\u0243w\3\2\2\2\u0244\u0249\5z>\2\u0245\u0246\7\37\2")
        buf.write("\2\u0246\u0248\5z>\2\u0247\u0245\3\2\2\2\u0248\u024b\3")
        buf.write("\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024ay")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\5|?\2\u024d\u024e")
        buf.write("\7!\2\2\u024e\u0250\3\2\2\2\u024f\u024c\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252\5~@\2\u0252")
        buf.write("{\3\2\2\2\u0253\u0257\7\r\2\2\u0254\u0257\5^\60\2\u0255")
        buf.write("\u0257\5v<\2\u0256\u0253\3\2\2\2\u0256\u0254\3\2\2\2\u0256")
        buf.write("\u0255\3\2\2\2\u0257}\3\2\2\2\u0258\u025b\5^\60\2\u0259")
        buf.write("\u025b\5v<\2\u025a\u0258\3\2\2\2\u025a\u0259\3\2\2\2\u025b")
        buf.write("\177\3\2\2\2\u025c\u025d\6A\n\2\u025d\u025e\5\16\b\2\u025e")
        buf.write("\u025f\5J&\2\u025f\u0262\3\2\2\2\u0260\u0262\5\u0084C")
        buf.write("\2\u0261\u025c\3\2\2\2\u0261\u0260\3\2\2\2\u0262\u0264")
        buf.write("\3\2\2\2\u0263\u0265\5\u0082B\2\u0264\u0263\3\2\2\2\u0264")
        buf.write("\u0265\3\2\2\2\u0265\u0081\3\2\2\2\u0266\u0267\t\n\2\2")
        buf.write("\u0267\u0083\3\2\2\2\u0268\u026a\7\67\2\2\u0269\u0268")
        buf.write("\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026b\3\2\2\2\u026b")
        buf.write("\u026c\5L\'\2\u026c\u0085\3\2\2\2\u026d\u026e\7\3\2\2")
        buf.write("\u026e\u026f\5V,\2\u026f\u0270\5 \21\2\u0270\u0087\3\2")
        buf.write("\2\2\u0271\u0272\7\34\2\2\u0272\u0273\5^\60\2\u0273\u0274")
        buf.write("\7\35\2\2\u0274\u0089\3\2\2\2\u0275\u0276\7\"\2\2\u0276")
        buf.write("\u0277\7\30\2\2\u0277\u0278\5J&\2\u0278\u0279\7\31\2\2")
        buf.write("\u0279\u008b\3\2\2\2\u027a\u0286\7\30\2\2\u027b\u0282")
        buf.write("\5\20\t\2\u027c\u027f\5J&\2\u027d\u027e\7\37\2\2\u027e")
        buf.write("\u0280\5\20\t\2\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2")
        buf.write("\2\u0280\u0282\3\2\2\2\u0281\u027b\3\2\2\2\u0281\u027c")
        buf.write("\3\2\2\2\u0282\u0284\3\2\2\2\u0283\u0285\7\37\2\2\u0284")
        buf.write("\u0283\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0287\3\2\2\2")
        buf.write("\u0286\u0281\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\3")
        buf.write("\2\2\2\u0288\u0289\7\31\2\2\u0289\u008d\3\2\2\2\u028a")
        buf.write("\u028b\5\u0090I\2\u028b\u028c\7\"\2\2\u028c\u028d\7\r")
        buf.write("\2\2\u028d\u008f\3\2\2\2\u028e\u0298\5L\'\2\u028f\u0293")
        buf.write("\7\30\2\2\u0290\u0291\7\67\2\2\u0291\u0294\5L\'\2\u0292")
        buf.write("\u0294\5\u0090I\2\u0293\u0290\3\2\2\2\u0293\u0292\3\2")
        buf.write("\2\2\u0294\u0295\3\2\2\2\u0295\u0296\7\31\2\2\u0296\u0298")
        buf.write("\3\2\2\2\u0297\u028e\3\2\2\2\u0297\u028f\3\2\2\2\u0298")
        buf.write("\u0091\3\2\2\2\u0299\u029e\7 \2\2\u029a\u029e\7\2\2\3")
        buf.write("\u029b\u029e\6J\13\2\u029c\u029e\6J\f\2\u029d\u0299\3")
        buf.write("\2\2\2\u029d\u029a\3\2\2\2\u029d\u029b\3\2\2\2\u029d\u029c")
        buf.write("\3\2\2\2\u029e\u0093\3\2\2\2N\u009b\u00a1\u00a7\u00b5")
        buf.write("\u00b9\u00bc\u00c4\u00cb\u00d3\u00de\u00e2\u00e6\u00ee")
        buf.write("\u00f5\u0100\u0104\u010d\u0116\u011e\u0124\u0130\u013e")
        buf.write("\u0145\u0147\u014b\u0151\u0154\u015a\u0162\u0167\u016d")
        buf.write("\u0174\u0182\u0187\u018b\u0190\u0194\u019a\u01a4\u01a8")
        buf.write("\u01b6\u01c0\u01c4\u01cc\u01d0\u01d2\u01d7\u01de\u01ef")
        buf.write("\u01f1\u01f7\u01ff\u0203\u0209\u020f\u021a\u021f\u0226")
        buf.write("\u022c\u0239\u023e\u0240\u0249\u024f\u0256\u025a\u0261")
        buf.write("\u0264\u0269\u027f\u0281\u0284\u0286\u0293\u0297\u029d")
        return buf.getvalue()


class TwoDimParser ( TwoDimParserBase ):

    grammarFileName = "TwoDimParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'switch'", "'case'", "'default'", 
                     "'if'", "'else'", "'type'", "'package'", "'import'", 
                     "'nil'", "<INVALID>", "'draw'", "'left'", "'right'", 
                     "'top'", "'bot'", "'outer'", "'inner'", "'on'", "'under'", 
                     "'in'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'='", 
                     "','", "';'", "':'", "'.'", "'++'", "'--'", "'or'", 
                     "'and'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'|'", "'/'", "'%'", "'<<'", "'>>'", "'&^'", "'!'", 
                     "'+'", "'-'", "'^'", "'*'", "'&'" ]

    symbolicNames = [ "<INVALID>", "FUNC", "SWITCH", "CASE", "DEFAULT", 
                      "IF", "ELSE", "TYPE", "PACKAGE", "IMPORT", "NIL_LIT", 
                      "IDENTIFIER", "DRAW", "LEFT", "RIGHT", "TOP", "BOT", 
                      "OUTER", "INNER", "ON", "UNDER", "IN", "L_PAREN", 
                      "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", 
                      "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", "PLUS_PLUS", 
                      "MINUS_MINUS", "LOGICAL_OR", "LOGICAL_AND", "EQUALS", 
                      "NOT_EQUALS", "LESS", "LESS_OR_EQUALS", "GREATER", 
                      "GREATER_OR_EQUALS", "OR", "DIV", "MOD", "LSHIFT", 
                      "RSHIFT", "BIT_CLEAR", "EXCLAMATION", "PLUS", "MINUS", 
                      "CARET", "STAR", "AMPERSAND", "DECIMAL_LIT", "FLOAT_LIT", 
                      "RUNE_LIT", "RAW_STRING_LIT", "INTERPRETED_STRING_LIT", 
                      "WS", "COMMENT", "TERMINATOR", "LINE_COMMENT" ]

    RULE_sourceFile = 0
    RULE_packageClause = 1
    RULE_importDecl = 2
    RULE_importSpec = 3
    RULE_importPath = 4
    RULE_declaration = 5
    RULE_identifierList = 6
    RULE_expressionList = 7
    RULE_typeDecl = 8
    RULE_typeSpec = 9
    RULE_functionDecl = 10
    RULE_methodDecl = 11
    RULE_receiver = 12
    RULE_varDecl = 13
    RULE_varSpec = 14
    RULE_block = 15
    RULE_statementList = 16
    RULE_statement = 17
    RULE_simpleStmt = 18
    RULE_expressionStmt = 19
    RULE_incDecStmt = 20
    RULE_assignment = 21
    RULE_assign_op = 22
    RULE_emptyStmt = 23
    RULE_labeledStmt = 24
    RULE_ifStmt = 25
    RULE_switchStmt = 26
    RULE_exprSwitchStmt = 27
    RULE_exprCaseClause = 28
    RULE_exprSwitchCase = 29
    RULE_typeSwitchStmt = 30
    RULE_typeSwitchGuard = 31
    RULE_typeCaseClause = 32
    RULE_typeSwitchCase = 33
    RULE_typeList = 34
    RULE_recvStmt = 35
    RULE_type_ = 36
    RULE_typeName = 37
    RULE_typeLit = 38
    RULE_elementType = 39
    RULE_methodSpec = 40
    RULE_functionType = 41
    RULE_signature = 42
    RULE_result = 43
    RULE_parameters = 44
    RULE_parameterDecl = 45
    RULE_expression = 46
    RULE_primaryExpr = 47
    RULE_unaryExpr = 48
    RULE_conversion = 49
    RULE_operand = 50
    RULE_literal = 51
    RULE_basicLit = 52
    RULE_integer = 53
    RULE_operandName = 54
    RULE_qualifiedIdent = 55
    RULE_compositeLit = 56
    RULE_literalType = 57
    RULE_literalValue = 58
    RULE_elementList = 59
    RULE_keyedElement = 60
    RULE_key = 61
    RULE_element = 62
    RULE_fieldDecl = 63
    RULE_string_ = 64
    RULE_anonymousField = 65
    RULE_functionLit = 66
    RULE_index = 67
    RULE_typeAssertion = 68
    RULE_arguments = 69
    RULE_methodExpr = 70
    RULE_receiverType = 71
    RULE_eos = 72

    ruleNames =  [ "sourceFile", "packageClause", "importDecl", "importSpec", 
                   "importPath", "declaration", "identifierList", "expressionList", 
                   "typeDecl", "typeSpec", "functionDecl", "methodDecl", 
                   "receiver", "varDecl", "varSpec", "block", "statementList", 
                   "statement", "simpleStmt", "expressionStmt", "incDecStmt", 
                   "assignment", "assign_op", "emptyStmt", "labeledStmt", 
                   "ifStmt", "switchStmt", "exprSwitchStmt", "exprCaseClause", 
                   "exprSwitchCase", "typeSwitchStmt", "typeSwitchGuard", 
                   "typeCaseClause", "typeSwitchCase", "typeList", "recvStmt", 
                   "type_", "typeName", "typeLit", "elementType", "methodSpec", 
                   "functionType", "signature", "result", "parameters", 
                   "parameterDecl", "expression", "primaryExpr", "unaryExpr", 
                   "conversion", "operand", "literal", "basicLit", "integer", 
                   "operandName", "qualifiedIdent", "compositeLit", "literalType", 
                   "literalValue", "elementList", "keyedElement", "key", 
                   "element", "fieldDecl", "string_", "anonymousField", 
                   "functionLit", "index", "typeAssertion", "arguments", 
                   "methodExpr", "receiverType", "eos" ]

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
    DRAW=12
    LEFT=13
    RIGHT=14
    TOP=15
    BOT=16
    OUTER=17
    INNER=18
    ON=19
    UNDER=20
    IN=21
    L_PAREN=22
    R_PAREN=23
    L_CURLY=24
    R_CURLY=25
    L_BRACKET=26
    R_BRACKET=27
    ASSIGN=28
    COMMA=29
    SEMI=30
    COLON=31
    DOT=32
    PLUS_PLUS=33
    MINUS_MINUS=34
    LOGICAL_OR=35
    LOGICAL_AND=36
    EQUALS=37
    NOT_EQUALS=38
    LESS=39
    LESS_OR_EQUALS=40
    GREATER=41
    GREATER_OR_EQUALS=42
    OR=43
    DIV=44
    MOD=45
    LSHIFT=46
    RSHIFT=47
    BIT_CLEAR=48
    EXCLAMATION=49
    PLUS=50
    MINUS=51
    CARET=52
    STAR=53
    AMPERSAND=54
    DECIMAL_LIT=55
    FLOAT_LIT=56
    RUNE_LIT=57
    RAW_STRING_LIT=58
    INTERPRETED_STRING_LIT=59
    WS=60
    COMMENT=61
    TERMINATOR=62
    LINE_COMMENT=63

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

        def packageClause(self):
            return self.getTypedRuleContext(TwoDimParser.PackageClauseContext,0)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.EosContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.EosContext,i)


        def importDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ImportDeclContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ImportDeclContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.FunctionDeclContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.MethodDeclContext,i)


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
            self.state = 146
            self.packageClause()
            self.state = 147
            self.eos()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.IMPORT:
                self.state = 148
                self.importDecl()
                self.state = 149
                self.eos()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.TYPE) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN))) != 0):
                self.state = 159
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 156
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 157
                    self.methodDecl()
                    pass

                elif la_ == 3:
                    self.state = 158
                    self.declaration()
                    pass


                self.state = 161
                self.eos()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(TwoDimParser.PACKAGE, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_packageClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageClause" ):
                listener.enterPackageClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageClause" ):
                listener.exitPackageClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageClause" ):
                return visitor.visitPackageClause(self)
            else:
                return visitor.visitChildren(self)




    def packageClause(self):

        localctx = TwoDimParser.PackageClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_packageClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(TwoDimParser.PACKAGE)
            self.state = 169
            self.match(TwoDimParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(TwoDimParser.IMPORT, 0)

        def importSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ImportSpecContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ImportSpecContext,i)


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
            return TwoDimParser.RULE_importDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDecl" ):
                listener.enterImportDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDecl" ):
                listener.exitImportDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDecl" ):
                return visitor.visitImportDecl(self)
            else:
                return visitor.visitChildren(self)




    def importDecl(self):

        localctx = TwoDimParser.ImportDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(TwoDimParser.IMPORT)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.IDENTIFIER, TwoDimParser.DOT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.state = 172
                self.importSpec()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.state = 173
                self.match(TwoDimParser.L_PAREN)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.DOT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                    self.state = 174
                    self.importSpec()
                    self.state = 175
                    self.eos()
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 182
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


    class ImportSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importPath(self):
            return self.getTypedRuleContext(TwoDimParser.ImportPathContext,0)


        def DOT(self):
            return self.getToken(TwoDimParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_importSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportSpec" ):
                listener.enterImportSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportSpec" ):
                listener.exitImportSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportSpec" ):
                return visitor.visitImportSpec(self)
            else:
                return visitor.visitChildren(self)




    def importSpec(self):

        localctx = TwoDimParser.ImportSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.IDENTIFIER or _la==TwoDimParser.DOT:
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==TwoDimParser.IDENTIFIER or _la==TwoDimParser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 188
            self.importPath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_(self):
            return self.getTypedRuleContext(TwoDimParser.String_Context,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_importPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportPath" ):
                listener.enterImportPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportPath" ):
                listener.exitImportPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportPath" ):
                return visitor.visitImportPath(self)
            else:
                return visitor.visitChildren(self)




    def importPath(self):

        localctx = TwoDimParser.ImportPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_importPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.string_()
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

        def typeDecl(self):
            return self.getTypedRuleContext(TwoDimParser.TypeDeclContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = TwoDimParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.typeDecl()
                pass
            elif token in [TwoDimParser.FUNC, TwoDimParser.IDENTIFIER, TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.varDecl()
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
        self.enterRule(localctx, 12, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.COMMA:
                self.state = 197
                self.match(TwoDimParser.COMMA)
                self.state = 198
                self.match(TwoDimParser.IDENTIFIER)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 14, self.RULE_expressionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expression(0)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.match(TwoDimParser.COMMA)
                    self.state = 206
                    self.expression(0) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(TwoDimParser.TYPE, 0)

        def typeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.TypeSpecContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.TypeSpecContext,i)


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
            return TwoDimParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = TwoDimParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(TwoDimParser.TYPE)
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.IDENTIFIER]:
                self.state = 213
                self.typeSpec()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.state = 214
                self.match(TwoDimParser.L_PAREN)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TwoDimParser.IDENTIFIER:
                    self.state = 215
                    self.typeSpec()
                    self.state = 216
                    self.eos()
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 223
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


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(TwoDimParser.ASSIGN, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = TwoDimParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.ASSIGN:
                self.state = 227
                self.match(TwoDimParser.ASSIGN)


            self.state = 230
            self.type_()
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
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(TwoDimParser.FUNC)
            self.state = 233
            self.match(TwoDimParser.IDENTIFIER)

            self.state = 234
            self.signature()
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 235
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TwoDimParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(TwoDimParser.ReceiverContext,0)


        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(TwoDimParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(TwoDimParser.BlockContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = TwoDimParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(TwoDimParser.FUNC)
            self.state = 239
            self.receiver()
            self.state = 240
            self.match(TwoDimParser.IDENTIFIER)

            self.state = 241
            self.signature()
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 242
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(TwoDimParser.ParametersContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_receiver

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiver" ):
                listener.enterReceiver(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiver" ):
                listener.exitReceiver(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = TwoDimParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.parameters()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = TwoDimParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 247
                self.varSpec()
                pass

            elif la_ == 2:
                self.state = 248
                self.match(TwoDimParser.L_PAREN)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN))) != 0):
                    self.state = 249
                    self.varSpec()
                    self.state = 250
                    self.eos()
                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 257
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

        def expressionList(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_varSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarSpec" ):
                listener.enterVarSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarSpec" ):
                listener.exitVarSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarSpec" ):
                return visitor.visitVarSpec(self)
            else:
                return visitor.visitChildren(self)




    def varSpec(self):

        localctx = TwoDimParser.VarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_varSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.type_()
            self.state = 261
            self.identifierList()
            self.state = 262
            self.match(TwoDimParser.ASSIGN)
            self.state = 263
            self.expressionList()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = TwoDimParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(TwoDimParser.L_CURLY)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.SWITCH) | (1 << TwoDimParser.IF) | (1 << TwoDimParser.TYPE) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_CURLY) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.SEMI) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                self.state = 266
                self.statementList()


            self.state = 269
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
        self.enterRule(localctx, 32, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.statement()
                self.state = 272
                self.eos()
                self.state = 276 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.SWITCH) | (1 << TwoDimParser.IF) | (1 << TwoDimParser.TYPE) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_CURLY) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.SEMI) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0)):
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


        def labeledStmt(self):
            return self.getTypedRuleContext(TwoDimParser.LabeledStmtContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TwoDimParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.labeledStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.simpleStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 282
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 283
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


        def incDecStmt(self):
            return self.getTypedRuleContext(TwoDimParser.IncDecStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(TwoDimParser.AssignmentContext,0)


        def emptyStmt(self):
            return self.getTypedRuleContext(TwoDimParser.EmptyStmtContext,0)


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
        self.enterRule(localctx, 36, self.RULE_simpleStmt)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expressionStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.incDecStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 289
                self.emptyStmt()
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
        self.enterRule(localctx, 38, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def PLUS_PLUS(self):
            return self.getToken(TwoDimParser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(TwoDimParser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncDecStmt" ):
                return visitor.visitIncDecStmt(self)
            else:
                return visitor.visitChildren(self)




    def incDecStmt(self):

        localctx = TwoDimParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_incDecStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.expression(0)
            self.state = 295
            _la = self._input.LA(1)
            if not(_la==TwoDimParser.PLUS_PLUS or _la==TwoDimParser.MINUS_MINUS):
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ExpressionListContext,i)


        def assign_op(self):
            return self.getTypedRuleContext(TwoDimParser.Assign_opContext,0)


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
        self.enterRule(localctx, 42, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expressionList()
            self.state = 298
            self.assign_op()
            self.state = 299
            self.expressionList()
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

        def PLUS(self):
            return self.getToken(TwoDimParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(TwoDimParser.MINUS, 0)

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
        self.enterRule(localctx, 44, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.PLUS or _la==TwoDimParser.MINUS:
                self.state = 301
                _la = self._input.LA(1)
                if not(_la==TwoDimParser.PLUS or _la==TwoDimParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 304
            self.match(TwoDimParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(TwoDimParser.SEMI, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_emptyStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStmt" ):
                return visitor.visitEmptyStmt(self)
            else:
                return visitor.visitChildren(self)




    def emptyStmt(self):

        localctx = TwoDimParser.EmptyStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_emptyStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(TwoDimParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(TwoDimParser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(TwoDimParser.StatementContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_labeledStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStmt" ):
                listener.enterLabeledStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStmt" ):
                listener.exitLabeledStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledStmt" ):
                return visitor.visitLabeledStmt(self)
            else:
                return visitor.visitChildren(self)




    def labeledStmt(self):

        localctx = TwoDimParser.LabeledStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_labeledStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 309
            self.match(TwoDimParser.COLON)
            self.state = 310
            self.statement()
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
        self.enterRule(localctx, 50, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(TwoDimParser.IF)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 313
                self.simpleStmt()
                self.state = 314
                self.match(TwoDimParser.SEMI)


            self.state = 318
            self.expression(0)
            self.state = 319
            self.block()
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 320
                self.match(TwoDimParser.ELSE)
                self.state = 323
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TwoDimParser.IF]:
                    self.state = 321
                    self.ifStmt()
                    pass
                elif token in [TwoDimParser.L_CURLY]:
                    self.state = 322
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


        def typeSwitchStmt(self):
            return self.getTypedRuleContext(TwoDimParser.TypeSwitchStmtContext,0)


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
        self.enterRule(localctx, 52, self.RULE_switchStmt)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.exprSwitchStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.typeSwitchStmt()
                pass


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
        self.enterRule(localctx, 54, self.RULE_exprSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(TwoDimParser.SWITCH)
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 332
                self.simpleStmt()
                self.state = 333
                self.match(TwoDimParser.SEMI)


            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                self.state = 337
                self.expression(0)


            self.state = 340
            self.match(TwoDimParser.L_CURLY)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.CASE or _la==TwoDimParser.DEFAULT:
                self.state = 341
                self.exprCaseClause()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 347
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
        self.enterRule(localctx, 56, self.RULE_exprCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.exprSwitchCase()
            self.state = 350
            self.match(TwoDimParser.COLON)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.SWITCH) | (1 << TwoDimParser.IF) | (1 << TwoDimParser.TYPE) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_CURLY) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.SEMI) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                self.state = 351
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

        def expressionList(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionListContext,0)


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
        self.enterRule(localctx, 58, self.RULE_exprSwitchCase)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(TwoDimParser.CASE)
                self.state = 355
                self.expressionList()
                pass
            elif token in [TwoDimParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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


    class TypeSwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TwoDimParser.SWITCH, 0)

        def typeSwitchGuard(self):
            return self.getTypedRuleContext(TwoDimParser.TypeSwitchGuardContext,0)


        def L_CURLY(self):
            return self.getToken(TwoDimParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(TwoDimParser.R_CURLY, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(TwoDimParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(TwoDimParser.SEMI, 0)

        def typeCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.TypeCaseClauseContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.TypeCaseClauseContext,i)


        def getRuleIndex(self):
            return TwoDimParser.RULE_typeSwitchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchStmt" ):
                listener.enterTypeSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchStmt" ):
                listener.exitTypeSwitchStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSwitchStmt" ):
                return visitor.visitTypeSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def typeSwitchStmt(self):

        localctx = TwoDimParser.TypeSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_typeSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(TwoDimParser.SWITCH)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 360
                self.simpleStmt()
                self.state = 361
                self.match(TwoDimParser.SEMI)


            self.state = 365
            self.typeSwitchGuard()
            self.state = 366
            self.match(TwoDimParser.L_CURLY)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.CASE or _la==TwoDimParser.DEFAULT:
                self.state = 367
                self.typeCaseClause()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 373
            self.match(TwoDimParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSwitchGuardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(TwoDimParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(TwoDimParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def TYPE(self):
            return self.getToken(TwoDimParser.TYPE, 0)

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_typeSwitchGuard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchGuard" ):
                listener.enterTypeSwitchGuard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchGuard" ):
                listener.exitTypeSwitchGuard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSwitchGuard" ):
                return visitor.visitTypeSwitchGuard(self)
            else:
                return visitor.visitChildren(self)




    def typeSwitchGuard(self):

        localctx = TwoDimParser.TypeSwitchGuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_typeSwitchGuard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.primaryExpr(0)
            self.state = 376
            self.match(TwoDimParser.DOT)
            self.state = 377
            self.match(TwoDimParser.L_PAREN)
            self.state = 378
            self.match(TwoDimParser.TYPE)
            self.state = 379
            self.match(TwoDimParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeCaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSwitchCase(self):
            return self.getTypedRuleContext(TwoDimParser.TypeSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(TwoDimParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(TwoDimParser.StatementListContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_typeCaseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCaseClause" ):
                listener.enterTypeCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCaseClause" ):
                listener.exitTypeCaseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCaseClause" ):
                return visitor.visitTypeCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def typeCaseClause(self):

        localctx = TwoDimParser.TypeCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_typeCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.typeSwitchCase()
            self.state = 382
            self.match(TwoDimParser.COLON)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.SWITCH) | (1 << TwoDimParser.IF) | (1 << TwoDimParser.TYPE) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_CURLY) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.SEMI) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                self.state = 383
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TwoDimParser.CASE, 0)

        def typeList(self):
            return self.getTypedRuleContext(TwoDimParser.TypeListContext,0)


        def DEFAULT(self):
            return self.getToken(TwoDimParser.DEFAULT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_typeSwitchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchCase" ):
                listener.enterTypeSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchCase" ):
                listener.exitTypeSwitchCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSwitchCase" ):
                return visitor.visitTypeSwitchCase(self)
            else:
                return visitor.visitChildren(self)




    def typeSwitchCase(self):

        localctx = TwoDimParser.TypeSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_typeSwitchCase)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(TwoDimParser.CASE)
                self.state = 387
                self.typeList()
                pass
            elif token in [TwoDimParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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


    class TypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.Type_Context)
            else:
                return self.getTypedRuleContext(TwoDimParser.Type_Context,i)


        def NIL_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.NIL_LIT)
            else:
                return self.getToken(TwoDimParser.NIL_LIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeList" ):
                return visitor.visitTypeList(self)
            else:
                return visitor.visitChildren(self)




    def typeList(self):

        localctx = TwoDimParser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.FUNC, TwoDimParser.IDENTIFIER, TwoDimParser.L_PAREN]:
                self.state = 391
                self.type_()
                pass
            elif token in [TwoDimParser.NIL_LIT]:
                self.state = 392
                self.match(TwoDimParser.NIL_LIT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TwoDimParser.COMMA:
                self.state = 395
                self.match(TwoDimParser.COMMA)
                self.state = 398
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TwoDimParser.FUNC, TwoDimParser.IDENTIFIER, TwoDimParser.L_PAREN]:
                    self.state = 396
                    self.type_()
                    pass
                elif token in [TwoDimParser.NIL_LIT]:
                    self.state = 397
                    self.match(TwoDimParser.NIL_LIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecvStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionListContext,0)


        def ASSIGN(self):
            return self.getToken(TwoDimParser.ASSIGN, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_recvStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecvStmt" ):
                listener.enterRecvStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecvStmt" ):
                listener.exitRecvStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecvStmt" ):
                return visitor.visitRecvStmt(self)
            else:
                return visitor.visitChildren(self)




    def recvStmt(self):

        localctx = TwoDimParser.RecvStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_recvStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 405
                self.expressionList()
                self.state = 406
                self.match(TwoDimParser.ASSIGN)


            self.state = 410
            self.expression(0)
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


        def typeLit(self):
            return self.getTypedRuleContext(TwoDimParser.TypeLitContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = TwoDimParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_type_)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.typeName()
                pass
            elif token in [TwoDimParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.typeLit()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.match(TwoDimParser.L_PAREN)
                self.state = 415
                self.type_()
                self.state = 416
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

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def qualifiedIdent(self):
            return self.getTypedRuleContext(TwoDimParser.QualifiedIdentContext,0)


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
        self.enterRule(localctx, 74, self.RULE_typeName)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(TwoDimParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.qualifiedIdent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionType(self):
            return self.getTypedRuleContext(TwoDimParser.FunctionTypeContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_typeLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLit" ):
                listener.enterTypeLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLit" ):
                listener.exitTypeLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeLit" ):
                return visitor.visitTypeLit(self)
            else:
                return visitor.visitChildren(self)




    def typeLit(self):

        localctx = TwoDimParser.TypeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_typeLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.functionType()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementType" ):
                return visitor.visitElementType(self)
            else:
                return visitor.visitChildren(self)




    def elementType(self):

        localctx = TwoDimParser.ElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elementType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def parameters(self):
            return self.getTypedRuleContext(TwoDimParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(TwoDimParser.ResultContext,0)


        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_methodSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodSpec" ):
                listener.enterMethodSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodSpec" ):
                listener.exitMethodSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSpec" ):
                return visitor.visitMethodSpec(self)
            else:
                return visitor.visitChildren(self)




    def methodSpec(self):

        localctx = TwoDimParser.MethodSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_methodSpec)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                if not noTerminatorAfterParams(2):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorAfterParams(2)")
                self.state = 429
                self.match(TwoDimParser.IDENTIFIER)
                self.state = 430
                self.parameters()
                self.state = 431
                self.result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.typeName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
                self.match(TwoDimParser.IDENTIFIER)
                self.state = 435
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TwoDimParser.FUNC, 0)

        def signature(self):
            return self.getTypedRuleContext(TwoDimParser.SignatureContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_functionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionType" ):
                listener.enterFunctionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionType" ):
                listener.exitFunctionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionType" ):
                return visitor.visitFunctionType(self)
            else:
                return visitor.visitChildren(self)




    def functionType(self):

        localctx = TwoDimParser.FunctionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_functionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(TwoDimParser.FUNC)
            self.state = 439
            self.signature()
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


        def result(self):
            return self.getTypedRuleContext(TwoDimParser.ResultContext,0)


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
        self.enterRule(localctx, 84, self.RULE_signature)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                if not noTerminatorAfterParams(1):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorAfterParams(1)")
                self.state = 442
                self.parameters()
                self.state = 443
                self.result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(TwoDimParser.ParametersContext,0)


        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult" ):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = TwoDimParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_result)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.type_()
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
        self.enterRule(localctx, 88, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(TwoDimParser.L_PAREN)
            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN))) != 0):
                self.state = 453
                self.parameterDecl()
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 454
                        self.match(TwoDimParser.COMMA)
                        self.state = 455
                        self.parameterDecl() 
                    self.state = 460
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.COMMA:
                    self.state = 461
                    self.match(TwoDimParser.COMMA)




            self.state = 466
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

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


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
        self.enterRule(localctx, 90, self.RULE_parameterDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 468
                self.identifierList()


            self.state = 471
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

        def primaryExpr(self):
            return self.getTypedRuleContext(TwoDimParser.PrimaryExprContext,0)


        def unaryExpr(self):
            return self.getTypedRuleContext(TwoDimParser.UnaryExprContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.ExpressionContext,i)


        def STAR(self):
            return self.getToken(TwoDimParser.STAR, 0)

        def DIV(self):
            return self.getToken(TwoDimParser.DIV, 0)

        def MOD(self):
            return self.getToken(TwoDimParser.MOD, 0)

        def LSHIFT(self):
            return self.getToken(TwoDimParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(TwoDimParser.RSHIFT, 0)

        def AMPERSAND(self):
            return self.getToken(TwoDimParser.AMPERSAND, 0)

        def BIT_CLEAR(self):
            return self.getToken(TwoDimParser.BIT_CLEAR, 0)

        def PLUS(self):
            return self.getToken(TwoDimParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(TwoDimParser.MINUS, 0)

        def OR(self):
            return self.getToken(TwoDimParser.OR, 0)

        def CARET(self):
            return self.getToken(TwoDimParser.CARET, 0)

        def EQUALS(self):
            return self.getToken(TwoDimParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(TwoDimParser.NOT_EQUALS, 0)

        def LESS(self):
            return self.getToken(TwoDimParser.LESS, 0)

        def LESS_OR_EQUALS(self):
            return self.getToken(TwoDimParser.LESS_OR_EQUALS, 0)

        def GREATER(self):
            return self.getToken(TwoDimParser.GREATER, 0)

        def GREATER_OR_EQUALS(self):
            return self.getToken(TwoDimParser.GREATER_OR_EQUALS, 0)

        def LOGICAL_AND(self):
            return self.getToken(TwoDimParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(TwoDimParser.LOGICAL_OR, 0)

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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TwoDimParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 474
                self.primaryExpr(0)
                pass

            elif la_ == 2:
                self.state = 475
                self.unaryExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 493
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        localctx = TwoDimParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 478
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 479
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.DIV) | (1 << TwoDimParser.MOD) | (1 << TwoDimParser.LSHIFT) | (1 << TwoDimParser.RSHIFT) | (1 << TwoDimParser.BIT_CLEAR) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 480
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = TwoDimParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 481
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 482
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.OR) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 483
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = TwoDimParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 484
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 485
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.EQUALS) | (1 << TwoDimParser.NOT_EQUALS) | (1 << TwoDimParser.LESS) | (1 << TwoDimParser.LESS_OR_EQUALS) | (1 << TwoDimParser.GREATER) | (1 << TwoDimParser.GREATER_OR_EQUALS))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 486
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = TwoDimParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 487
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 488
                        self.match(TwoDimParser.LOGICAL_AND)
                        self.state = 489
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = TwoDimParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 490
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 491
                        self.match(TwoDimParser.LOGICAL_OR)
                        self.state = 492
                        self.expression(2)
                        pass

             
                self.state = 497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TwoDimParser.OperandContext,0)


        def conversion(self):
            return self.getTypedRuleContext(TwoDimParser.ConversionContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(TwoDimParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(TwoDimParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def index(self):
            return self.getTypedRuleContext(TwoDimParser.IndexContext,0)


        def typeAssertion(self):
            return self.getTypedRuleContext(TwoDimParser.TypeAssertionContext,0)


        def arguments(self):
            return self.getTypedRuleContext(TwoDimParser.ArgumentsContext,0)


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



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TwoDimParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_primaryExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 499
                self.operand()
                pass

            elif la_ == 2:
                self.state = 500
                self.conversion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 513
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TwoDimParser.PrimaryExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                    self.state = 503
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 509
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        self.state = 504
                        self.match(TwoDimParser.DOT)
                        self.state = 505
                        self.match(TwoDimParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        self.state = 506
                        self.index()
                        pass

                    elif la_ == 3:
                        self.state = 507
                        self.typeAssertion()
                        pass

                    elif la_ == 4:
                        self.state = 508
                        self.arguments()
                        pass

             
                self.state = 515
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(TwoDimParser.PrimaryExprContext,0)


        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(TwoDimParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(TwoDimParser.MINUS, 0)

        def EXCLAMATION(self):
            return self.getToken(TwoDimParser.EXCLAMATION, 0)

        def CARET(self):
            return self.getToken(TwoDimParser.CARET, 0)

        def STAR(self):
            return self.getToken(TwoDimParser.STAR, 0)

        def AMPERSAND(self):
            return self.getToken(TwoDimParser.AMPERSAND, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = TwoDimParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.FUNC, TwoDimParser.NIL_LIT, TwoDimParser.IDENTIFIER, TwoDimParser.L_PAREN, TwoDimParser.L_BRACKET, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.primaryExpr(0)
                pass
            elif token in [TwoDimParser.EXCLAMATION, TwoDimParser.PLUS, TwoDimParser.MINUS, TwoDimParser.CARET, TwoDimParser.STAR, TwoDimParser.AMPERSAND]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 518
                self.expression(0)
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


    class ConversionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def COMMA(self):
            return self.getToken(TwoDimParser.COMMA, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_conversion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversion" ):
                listener.enterConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversion" ):
                listener.exitConversion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversion" ):
                return visitor.visitConversion(self)
            else:
                return visitor.visitChildren(self)




    def conversion(self):

        localctx = TwoDimParser.ConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_conversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.type_()
            self.state = 522
            self.match(TwoDimParser.L_PAREN)
            self.state = 523
            self.expression(0)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.COMMA:
                self.state = 524
                self.match(TwoDimParser.COMMA)


            self.state = 527
            self.match(TwoDimParser.R_PAREN)
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


        def methodExpr(self):
            return self.getTypedRuleContext(TwoDimParser.MethodExprContext,0)


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
        self.enterRule(localctx, 100, self.RULE_operand)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.operandName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 531
                self.methodExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 532
                self.match(TwoDimParser.L_PAREN)
                self.state = 533
                self.expression(0)
                self.state = 534
                self.match(TwoDimParser.R_PAREN)
                pass


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


        def functionLit(self):
            return self.getTypedRuleContext(TwoDimParser.FunctionLitContext,0)


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
        self.enterRule(localctx, 102, self.RULE_literal)
        try:
            self.state = 541
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.NIL_LIT, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.basicLit()
                pass
            elif token in [TwoDimParser.IDENTIFIER, TwoDimParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.compositeLit()
                pass
            elif token in [TwoDimParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.functionLit()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicLit" ):
                return visitor.visitBasicLit(self)
            else:
                return visitor.visitChildren(self)




    def basicLit(self):

        localctx = TwoDimParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_basicLit)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.match(TwoDimParser.NIL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.integer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 545
                self.string_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                self.match(TwoDimParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 547
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
        self.enterRule(localctx, 106, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
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

        def qualifiedIdent(self):
            return self.getTypedRuleContext(TwoDimParser.QualifiedIdentContext,0)


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
        self.enterRule(localctx, 108, self.RULE_operandName)
        try:
            self.state = 554
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.match(TwoDimParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.qualifiedIdent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedIdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.IDENTIFIER)
            else:
                return self.getToken(TwoDimParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(TwoDimParser.DOT, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_qualifiedIdent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedIdent" ):
                listener.enterQualifiedIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedIdent" ):
                listener.exitQualifiedIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedIdent" ):
                return visitor.visitQualifiedIdent(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedIdent(self):

        localctx = TwoDimParser.QualifiedIdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_qualifiedIdent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(TwoDimParser.IDENTIFIER)
            self.state = 557
            self.match(TwoDimParser.DOT)
            self.state = 558
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeLit" ):
                return visitor.visitCompositeLit(self)
            else:
                return visitor.visitChildren(self)




    def compositeLit(self):

        localctx = TwoDimParser.CompositeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_compositeLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.literalType()
            self.state = 561
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

        def L_BRACKET(self):
            return self.getToken(TwoDimParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(TwoDimParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(TwoDimParser.ElementTypeContext,0)


        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_literalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralType" ):
                listener.enterLiteralType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralType" ):
                listener.exitLiteralType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralType" ):
                return visitor.visitLiteralType(self)
            else:
                return visitor.visitChildren(self)




    def literalType(self):

        localctx = TwoDimParser.LiteralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_literalType)
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.match(TwoDimParser.L_BRACKET)
                self.state = 564
                self.match(TwoDimParser.R_BRACKET)
                self.state = 565
                self.elementType()
                pass
            elif token in [TwoDimParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.typeName()
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


    class LiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(TwoDimParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(TwoDimParser.R_CURLY, 0)

        def elementList(self):
            return self.getTypedRuleContext(TwoDimParser.ElementListContext,0)


        def COMMA(self):
            return self.getToken(TwoDimParser.COMMA, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralValue" ):
                return visitor.visitLiteralValue(self)
            else:
                return visitor.visitChildren(self)




    def literalValue(self):

        localctx = TwoDimParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(TwoDimParser.L_CURLY)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_CURLY) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                self.state = 570
                self.elementList()
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.COMMA:
                    self.state = 571
                    self.match(TwoDimParser.COMMA)




            self.state = 576
            self.match(TwoDimParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TwoDimParser.KeyedElementContext)
            else:
                return self.getTypedRuleContext(TwoDimParser.KeyedElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

        def getRuleIndex(self):
            return TwoDimParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementList" ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementList" ):
                listener.exitElementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementList" ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = TwoDimParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_elementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.keyedElement()
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 579
                    self.match(TwoDimParser.COMMA)
                    self.state = 580
                    self.keyedElement() 
                self.state = 585
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyedElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(TwoDimParser.ElementContext,0)


        def key(self):
            return self.getTypedRuleContext(TwoDimParser.KeyContext,0)


        def COLON(self):
            return self.getToken(TwoDimParser.COLON, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_keyedElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyedElement" ):
                listener.enterKeyedElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyedElement" ):
                listener.exitKeyedElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyedElement" ):
                return visitor.visitKeyedElement(self)
            else:
                return visitor.visitChildren(self)




    def keyedElement(self):

        localctx = TwoDimParser.KeyedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_keyedElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 586
                self.key()
                self.state = 587
                self.match(TwoDimParser.COLON)


            self.state = 591
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(TwoDimParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = TwoDimParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_key)
        try:
            self.state = 596
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.match(TwoDimParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 594
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 595
                self.literalValue()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = TwoDimParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_element)
        try:
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.FUNC, TwoDimParser.NIL_LIT, TwoDimParser.IDENTIFIER, TwoDimParser.L_PAREN, TwoDimParser.L_BRACKET, TwoDimParser.EXCLAMATION, TwoDimParser.PLUS, TwoDimParser.MINUS, TwoDimParser.CARET, TwoDimParser.STAR, TwoDimParser.AMPERSAND, TwoDimParser.DECIMAL_LIT, TwoDimParser.FLOAT_LIT, TwoDimParser.RUNE_LIT, TwoDimParser.RAW_STRING_LIT, TwoDimParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.expression(0)
                pass
            elif token in [TwoDimParser.L_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
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


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(TwoDimParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def anonymousField(self):
            return self.getTypedRuleContext(TwoDimParser.AnonymousFieldContext,0)


        def string_(self):
            return self.getTypedRuleContext(TwoDimParser.String_Context,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_fieldDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDecl" ):
                listener.enterFieldDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDecl" ):
                listener.exitFieldDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = TwoDimParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_fieldDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 602
                if not noTerminatorBetween(2):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorBetween(2)")
                self.state = 603
                self.identifierList()
                self.state = 604
                self.type_()
                pass

            elif la_ == 2:
                self.state = 606
                self.anonymousField()
                pass


            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.RAW_STRING_LIT or _la==TwoDimParser.INTERPRETED_STRING_LIT:
                self.state = 609
                self.string_()


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
        self.enterRule(localctx, 128, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
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


    class AnonymousFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def STAR(self):
            return self.getToken(TwoDimParser.STAR, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_anonymousField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonymousField" ):
                listener.enterAnonymousField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonymousField" ):
                listener.exitAnonymousField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnonymousField" ):
                return visitor.visitAnonymousField(self)
            else:
                return visitor.visitChildren(self)




    def anonymousField(self):

        localctx = TwoDimParser.AnonymousFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_anonymousField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TwoDimParser.STAR:
                self.state = 614
                self.match(TwoDimParser.STAR)


            self.state = 617
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TwoDimParser.FUNC, 0)

        def signature(self):
            return self.getTypedRuleContext(TwoDimParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(TwoDimParser.BlockContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_functionLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionLit" ):
                listener.enterFunctionLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionLit" ):
                listener.exitFunctionLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionLit" ):
                return visitor.visitFunctionLit(self)
            else:
                return visitor.visitChildren(self)




    def functionLit(self):

        localctx = TwoDimParser.FunctionLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_functionLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(TwoDimParser.FUNC)
            self.state = 620
            self.signature()
            self.state = 621
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(TwoDimParser.L_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(TwoDimParser.ExpressionContext,0)


        def R_BRACKET(self):
            return self.getToken(TwoDimParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = TwoDimParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(TwoDimParser.L_BRACKET)
            self.state = 624
            self.expression(0)
            self.state = 625
            self.match(TwoDimParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(TwoDimParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_typeAssertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAssertion" ):
                listener.enterTypeAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAssertion" ):
                listener.exitTypeAssertion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAssertion" ):
                return visitor.visitTypeAssertion(self)
            else:
                return visitor.visitChildren(self)




    def typeAssertion(self):

        localctx = TwoDimParser.TypeAssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_typeAssertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(TwoDimParser.DOT)
            self.state = 628
            self.match(TwoDimParser.L_PAREN)
            self.state = 629
            self.type_()
            self.state = 630
            self.match(TwoDimParser.R_PAREN)
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


        def type_(self):
            return self.getTypedRuleContext(TwoDimParser.Type_Context,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TwoDimParser.COMMA)
            else:
                return self.getToken(TwoDimParser.COMMA, i)

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
        self.enterRule(localctx, 138, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(TwoDimParser.L_PAREN)
            self.state = 644
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TwoDimParser.FUNC) | (1 << TwoDimParser.NIL_LIT) | (1 << TwoDimParser.IDENTIFIER) | (1 << TwoDimParser.L_PAREN) | (1 << TwoDimParser.L_BRACKET) | (1 << TwoDimParser.EXCLAMATION) | (1 << TwoDimParser.PLUS) | (1 << TwoDimParser.MINUS) | (1 << TwoDimParser.CARET) | (1 << TwoDimParser.STAR) | (1 << TwoDimParser.AMPERSAND) | (1 << TwoDimParser.DECIMAL_LIT) | (1 << TwoDimParser.FLOAT_LIT) | (1 << TwoDimParser.RUNE_LIT) | (1 << TwoDimParser.RAW_STRING_LIT) | (1 << TwoDimParser.INTERPRETED_STRING_LIT))) != 0):
                self.state = 639
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                if la_ == 1:
                    self.state = 633
                    self.expressionList()
                    pass

                elif la_ == 2:
                    self.state = 634
                    self.type_()
                    self.state = 637
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        self.state = 635
                        self.match(TwoDimParser.COMMA)
                        self.state = 636
                        self.expressionList()


                    pass


                self.state = 642
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TwoDimParser.COMMA:
                    self.state = 641
                    self.match(TwoDimParser.COMMA)




            self.state = 646
            self.match(TwoDimParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def receiverType(self):
            return self.getTypedRuleContext(TwoDimParser.ReceiverTypeContext,0)


        def DOT(self):
            return self.getToken(TwoDimParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(TwoDimParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TwoDimParser.RULE_methodExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodExpr" ):
                listener.enterMethodExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodExpr" ):
                listener.exitMethodExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodExpr" ):
                return visitor.visitMethodExpr(self)
            else:
                return visitor.visitChildren(self)




    def methodExpr(self):

        localctx = TwoDimParser.MethodExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_methodExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self.receiverType()
            self.state = 649
            self.match(TwoDimParser.DOT)
            self.state = 650
            self.match(TwoDimParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(TwoDimParser.TypeNameContext,0)


        def L_PAREN(self):
            return self.getToken(TwoDimParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(TwoDimParser.R_PAREN, 0)

        def STAR(self):
            return self.getToken(TwoDimParser.STAR, 0)

        def receiverType(self):
            return self.getTypedRuleContext(TwoDimParser.ReceiverTypeContext,0)


        def getRuleIndex(self):
            return TwoDimParser.RULE_receiverType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiverType" ):
                listener.enterReceiverType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiverType" ):
                listener.exitReceiverType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiverType" ):
                return visitor.visitReceiverType(self)
            else:
                return visitor.visitChildren(self)




    def receiverType(self):

        localctx = TwoDimParser.ReceiverTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_receiverType)
        try:
            self.state = 661
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TwoDimParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.typeName()
                pass
            elif token in [TwoDimParser.L_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 653
                self.match(TwoDimParser.L_PAREN)
                self.state = 657
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [TwoDimParser.STAR]:
                    self.state = 654
                    self.match(TwoDimParser.STAR)
                    self.state = 655
                    self.typeName()
                    pass
                elif token in [TwoDimParser.IDENTIFIER, TwoDimParser.L_PAREN]:
                    self.state = 656
                    self.receiverType()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 659
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
        self.enterRule(localctx, 144, self.RULE_eos)
        try:
            self.state = 667
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.match(TwoDimParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.match(TwoDimParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 665
                if not lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 666
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
        self._predicates[40] = self.methodSpec_sempred
        self._predicates[42] = self.signature_sempred
        self._predicates[46] = self.expression_sempred
        self._predicates[47] = self.primaryExpr_sempred
        self._predicates[63] = self.fieldDecl_sempred
        self._predicates[72] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def methodSpec_sempred(self, localctx:MethodSpecContext, predIndex:int):
            if predIndex == 0:
                return noTerminatorAfterParams(2)
         

    def signature_sempred(self, localctx:SignatureContext, predIndex:int):
            if predIndex == 1:
                return noTerminatorAfterParams(1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def fieldDecl_sempred(self, localctx:FieldDeclContext, predIndex:int):
            if predIndex == 8:
                return noTerminatorBetween(2)
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 9:
                return lineTerminatorAhead()
         

            if predIndex == 10:
                return checkPreviousTokenText("}")
         




