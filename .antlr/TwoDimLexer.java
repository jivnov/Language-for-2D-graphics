// Generated from /home/liza/TKK/projekt/Language-for-2D-graphics/TwoDimLexer.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TwoDimLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		FUNC=1, SWITCH=2, CASE=3, DEFAULT=4, IF=5, ELSE=6, TYPE=7, PACKAGE=8, 
		IMPORT=9, NIL_LIT=10, IDENTIFIER=11, SQUARE=12, RECT=13, CIRCLE=14, TRIANGLE=15, 
		SHAPE=16, DRAW=17, VIEWPORT=18, LEFT=19, RIGHT=20, TOP=21, BOT=22, OUTER=23, 
		INNER=24, ON=25, UNDER=26, IN=27, L_PAREN=28, R_PAREN=29, L_CURLY=30, 
		R_CURLY=31, L_BRACKET=32, R_BRACKET=33, ASSIGN=34, COMMA=35, SEMI=36, 
		COLON=37, DOT=38, PLUS_PLUS=39, MINUS_MINUS=40, LOGICAL_OR=41, LOGICAL_AND=42, 
		EQUALS=43, NOT_EQUALS=44, LESS=45, LESS_OR_EQUALS=46, GREATER=47, GREATER_OR_EQUALS=48, 
		OR=49, DIV=50, MOD=51, LSHIFT=52, RSHIFT=53, BIT_CLEAR=54, EXCLAMATION=55, 
		PLUS=56, MINUS=57, CARET=58, STAR=59, AMPERSAND=60, DECIMAL_LIT=61, FLOAT_LIT=62, 
		RUNE_LIT=63, RAW_STRING_LIT=64, INTERPRETED_STRING_LIT=65, SIZE_LIT=66, 
		WS=67, COMMENT=68, TERMINATOR=69, LINE_COMMENT=70;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"FUNC", "SWITCH", "CASE", "DEFAULT", "IF", "ELSE", "TYPE", "PACKAGE", 
			"IMPORT", "NIL_LIT", "IDENTIFIER", "SQUARE", "RECT", "CIRCLE", "TRIANGLE", 
			"SHAPE", "DRAW", "VIEWPORT", "LEFT", "RIGHT", "TOP", "BOT", "OUTER", 
			"INNER", "ON", "UNDER", "IN", "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", 
			"L_BRACKET", "R_BRACKET", "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", 
			"PLUS_PLUS", "MINUS_MINUS", "LOGICAL_OR", "LOGICAL_AND", "EQUALS", "NOT_EQUALS", 
			"LESS", "LESS_OR_EQUALS", "GREATER", "GREATER_OR_EQUALS", "OR", "DIV", 
			"MOD", "LSHIFT", "RSHIFT", "BIT_CLEAR", "EXCLAMATION", "PLUS", "MINUS", 
			"CARET", "STAR", "AMPERSAND", "DECIMAL_LIT", "FLOAT_LIT", "RUNE_LIT", 
			"RAW_STRING_LIT", "INTERPRETED_STRING_LIT", "SIZE_LIT", "WS", "COMMENT", 
			"TERMINATOR", "LINE_COMMENT", "ESCAPED_VALUE", "SIZE", "DECIMALS", "EXPONENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'func'", "'switch'", "'case'", "'default'", "'if'", "'else'", 
			"'type'", "'package'", "'import'", "'nil'", null, "'square'", "'rect'", 
			"'circle'", "'triangle'", "'shape'", "'draw'", "'#viewport'", "'left'", 
			"'right'", "'top'", "'bot'", "'outer'", "'inner'", "'on'", "'under'", 
			"'in'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'='", "','", "';'", 
			"':'", "'.'", "'++'", "'--'", "'or'", "'and'", "'=='", "'!='", "'<'", 
			"'<='", "'>'", "'>='", "'|'", "'/'", "'%'", "'<<'", "'>>'", "'&^'", "'!'", 
			"'+'", "'-'", "'^'", "'*'", "'&'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FUNC", "SWITCH", "CASE", "DEFAULT", "IF", "ELSE", "TYPE", "PACKAGE", 
			"IMPORT", "NIL_LIT", "IDENTIFIER", "SQUARE", "RECT", "CIRCLE", "TRIANGLE", 
			"SHAPE", "DRAW", "VIEWPORT", "LEFT", "RIGHT", "TOP", "BOT", "OUTER", 
			"INNER", "ON", "UNDER", "IN", "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", 
			"L_BRACKET", "R_BRACKET", "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", 
			"PLUS_PLUS", "MINUS_MINUS", "LOGICAL_OR", "LOGICAL_AND", "EQUALS", "NOT_EQUALS", 
			"LESS", "LESS_OR_EQUALS", "GREATER", "GREATER_OR_EQUALS", "OR", "DIV", 
			"MOD", "LSHIFT", "RSHIFT", "BIT_CLEAR", "EXCLAMATION", "PLUS", "MINUS", 
			"CARET", "STAR", "AMPERSAND", "DECIMAL_LIT", "FLOAT_LIT", "RUNE_LIT", 
			"RAW_STRING_LIT", "INTERPRETED_STRING_LIT", "SIZE_LIT", "WS", "COMMENT", 
			"TERMINATOR", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public TwoDimLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "TwoDimLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H\u01ee\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7"+
		"\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\7\f\u00d3\n\f\f\f\16\f"+
		"\u00d6\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37"+
		"\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)"+
		"\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60"+
		"\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66"+
		"\3\66\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\7>\u0184"+
		"\n>\f>\16>\u0187\13>\3?\3?\3?\5?\u018c\n?\3?\5?\u018f\n?\3?\5?\u0192\n"+
		"?\3?\3?\3?\5?\u0197\n?\5?\u0199\n?\3@\3@\3@\5@\u019e\n@\3@\3@\3A\3A\7"+
		"A\u01a4\nA\fA\16A\u01a7\13A\3A\3A\3B\3B\3B\7B\u01ae\nB\fB\16B\u01b1\13"+
		"B\3B\3B\3C\3C\3D\6D\u01b8\nD\rD\16D\u01b9\3D\3D\3E\3E\3E\3E\7E\u01c2\n"+
		"E\fE\16E\u01c5\13E\3E\3E\3E\3E\3E\3F\6F\u01cd\nF\rF\16F\u01ce\3F\3F\3"+
		"G\3G\3G\3G\7G\u01d7\nG\fG\16G\u01da\13G\3G\3G\3H\3H\3H\3I\3I\3I\3J\6J"+
		"\u01e5\nJ\rJ\16J\u01e6\3K\3K\5K\u01eb\nK\3K\3K\3\u01c3\2L\3\3\5\4\7\5"+
		"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{"+
		"?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008f\2\u0091"+
		"\2\u0093\2\u0095\2\3\2\f\3\2\63;\3\2\62;\4\2\f\f^^\3\2bb\4\2$$^^\3\2\""+
		"\"\4\2\f\f\17\17\13\2$$))^^cdhhppttvvxx\4\2GGgg\4\2--//\4\u0275\2C\2\\"+
		"\2\u00c2\2\u00d8\2\u00da\2\u00e0\2\u0102\2\u0102\2\u0104\2\u0104\2\u0106"+
		"\2\u0106\2\u0108\2\u0108\2\u010a\2\u010a\2\u010c\2\u010c\2\u010e\2\u010e"+
		"\2\u0110\2\u0110\2\u0112\2\u0112\2\u0114\2\u0114\2\u0116\2\u0116\2\u0118"+
		"\2\u0118\2\u011a\2\u011a\2\u011c\2\u011c\2\u011e\2\u011e\2\u0120\2\u0120"+
		"\2\u0122\2\u0122\2\u0124\2\u0124\2\u0126\2\u0126\2\u0128\2\u0128\2\u012a"+
		"\2\u012a\2\u012c\2\u012c\2\u012e\2\u012e\2\u0130\2\u0130\2\u0132\2\u0132"+
		"\2\u0134\2\u0134\2\u0136\2\u0136\2\u0138\2\u0138\2\u013b\2\u013b\2\u013d"+
		"\2\u013d\2\u013f\2\u013f\2\u0141\2\u0141\2\u0143\2\u0143\2\u0145\2\u0145"+
		"\2\u0147\2\u0147\2\u0149\2\u0149\2\u014c\2\u014c\2\u014e\2\u014e\2\u0150"+
		"\2\u0150\2\u0152\2\u0152\2\u0154\2\u0154\2\u0156\2\u0156\2\u0158\2\u0158"+
		"\2\u015a\2\u015a\2\u015c\2\u015c\2\u015e\2\u015e\2\u0160\2\u0160\2\u0162"+
		"\2\u0162\2\u0164\2\u0164\2\u0166\2\u0166\2\u0168\2\u0168\2\u016a\2\u016a"+
		"\2\u016c\2\u016c\2\u016e\2\u016e\2\u0170\2\u0170\2\u0172\2\u0172\2\u0174"+
		"\2\u0174\2\u0176\2\u0176\2\u0178\2\u0178\2\u017a\2\u017b\2\u017d\2\u017d"+
		"\2\u017f\2\u017f\2\u0183\2\u0184\2\u0186\2\u0186\2\u0188\2\u0189\2\u018b"+
		"\2\u018d\2\u0190\2\u0193\2\u0195\2\u0196\2\u0198\2\u019a\2\u019e\2\u019f"+
		"\2\u01a1\2\u01a2\2\u01a4\2\u01a4\2\u01a6\2\u01a6\2\u01a8\2\u01a9\2\u01ab"+
		"\2\u01ab\2\u01ae\2\u01ae\2\u01b0\2\u01b1\2\u01b3\2\u01b5\2\u01b7\2\u01b7"+
		"\2\u01b9\2\u01ba\2\u01be\2\u01be\2\u01c6\2\u01c6\2\u01c9\2\u01c9\2\u01cc"+
		"\2\u01cc\2\u01cf\2\u01cf\2\u01d1\2\u01d1\2\u01d3\2\u01d3\2\u01d5\2\u01d5"+
		"\2\u01d7\2\u01d7\2\u01d9\2\u01d9\2\u01db\2\u01db\2\u01dd\2\u01dd\2\u01e0"+
		"\2\u01e0\2\u01e2\2\u01e2\2\u01e4\2\u01e4\2\u01e6\2\u01e6\2\u01e8\2\u01e8"+
		"\2\u01ea\2\u01ea\2\u01ec\2\u01ec\2\u01ee\2\u01ee\2\u01f0\2\u01f0\2\u01f3"+
		"\2\u01f3\2\u01f6\2\u01f6\2\u01f8\2\u01fa\2\u01fc\2\u01fc\2\u01fe\2\u01fe"+
		"\2\u0200\2\u0200\2\u0202\2\u0202\2\u0204\2\u0204\2\u0206\2\u0206\2\u0208"+
		"\2\u0208\2\u020a\2\u020a\2\u020c\2\u020c\2\u020e\2\u020e\2\u0210\2\u0210"+
		"\2\u0212\2\u0212\2\u0214\2\u0214\2\u0216\2\u0216\2\u0218\2\u0218\2\u021a"+
		"\2\u021a\2\u021c\2\u021c\2\u021e\2\u021e\2\u0220\2\u0220\2\u0222\2\u0222"+
		"\2\u0224\2\u0224\2\u0226\2\u0226\2\u0228\2\u0228\2\u022a\2\u022a\2\u022c"+
		"\2\u022c\2\u022e\2\u022e\2\u0230\2\u0230\2\u0232\2\u0232\2\u0234\2\u0234"+
		"\2\u023c\2\u023d\2\u023f\2\u0240\2\u0243\2\u0243\2\u0245\2\u0248\2\u024a"+
		"\2\u024a\2\u024c\2\u024c\2\u024e\2\u024e\2\u0250\2\u0250\2\u0372\2\u0372"+
		"\2\u0374\2\u0374\2\u0378\2\u0378\2\u0381\2\u0381\2\u0388\2\u0388\2\u038a"+
		"\2\u038c\2\u038e\2\u038e\2\u0390\2\u0391\2\u0393\2\u03a3\2\u03a5\2\u03ad"+
		"\2\u03d1\2\u03d1\2\u03d4\2\u03d6\2\u03da\2\u03da\2\u03dc\2\u03dc\2\u03de"+
		"\2\u03de\2\u03e0\2\u03e0\2\u03e2\2\u03e2\2\u03e4\2\u03e4\2\u03e6\2\u03e6"+
		"\2\u03e8\2\u03e8\2\u03ea\2\u03ea\2\u03ec\2\u03ec\2\u03ee\2\u03ee\2\u03f0"+
		"\2\u03f0\2\u03f6\2\u03f6\2\u03f9\2\u03f9\2\u03fb\2\u03fc\2\u03ff\2\u0431"+
		"\2\u0462\2\u0462\2\u0464\2\u0464\2\u0466\2\u0466\2\u0468\2\u0468\2\u046a"+
		"\2\u046a\2\u046c\2\u046c\2\u046e\2\u046e\2\u0470\2\u0470\2\u0472\2\u0472"+
		"\2\u0474\2\u0474\2\u0476\2\u0476\2\u0478\2\u0478\2\u047a\2\u047a\2\u047c"+
		"\2\u047c\2\u047e\2\u047e\2\u0480\2\u0480\2\u0482\2\u0482\2\u048c\2\u048c"+
		"\2\u048e\2\u048e\2\u0490\2\u0490\2\u0492\2\u0492\2\u0494\2\u0494\2\u0496"+
		"\2\u0496\2\u0498\2\u0498\2\u049a\2\u049a\2\u049c\2\u049c\2\u049e\2\u049e"+
		"\2\u04a0\2\u04a0\2\u04a2\2\u04a2\2\u04a4\2\u04a4\2\u04a6\2\u04a6\2\u04a8"+
		"\2\u04a8\2\u04aa\2\u04aa\2\u04ac\2\u04ac\2\u04ae\2\u04ae\2\u04b0\2\u04b0"+
		"\2\u04b2\2\u04b2\2\u04b4\2\u04b4\2\u04b6\2\u04b6\2\u04b8\2\u04b8\2\u04ba"+
		"\2\u04ba\2\u04bc\2\u04bc\2\u04be\2\u04be\2\u04c0\2\u04c0\2\u04c2\2\u04c3"+
		"\2\u04c5\2\u04c5\2\u04c7\2\u04c7\2\u04c9\2\u04c9\2\u04cb\2\u04cb\2\u04cd"+
		"\2\u04cd\2\u04cf\2\u04cf\2\u04d2\2\u04d2\2\u04d4\2\u04d4\2\u04d6\2\u04d6"+
		"\2\u04d8\2\u04d8\2\u04da\2\u04da\2\u04dc\2\u04dc\2\u04de\2\u04de\2\u04e0"+
		"\2\u04e0\2\u04e2\2\u04e2\2\u04e4\2\u04e4\2\u04e6\2\u04e6\2\u04e8\2\u04e8"+
		"\2\u04ea\2\u04ea\2\u04ec\2\u04ec\2\u04ee\2\u04ee\2\u04f0\2\u04f0\2\u04f2"+
		"\2\u04f2\2\u04f4\2\u04f4\2\u04f6\2\u04f6\2\u04f8\2\u04f8\2\u04fa\2\u04fa"+
		"\2\u04fc\2\u04fc\2\u04fe\2\u04fe\2\u0500\2\u0500\2\u0502\2\u0502\2\u0504"+
		"\2\u0504\2\u0506\2\u0506\2\u0508\2\u0508\2\u050a\2\u050a\2\u050c\2\u050c"+
		"\2\u050e\2\u050e\2\u0510\2\u0510\2\u0512\2\u0512\2\u0514\2\u0514\2\u0516"+
		"\2\u0516\2\u0518\2\u0518\2\u051a\2\u051a\2\u051c\2\u051c\2\u051e\2\u051e"+
		"\2\u0520\2\u0520\2\u0522\2\u0522\2\u0524\2\u0524\2\u0526\2\u0526\2\u0528"+
		"\2\u0528\2\u052a\2\u052a\2\u052c\2\u052c\2\u052e\2\u052e\2\u0530\2\u0530"+
		"\2\u0533\2\u0558\2\u10a2\2\u10c7\2\u10c9\2\u10c9\2\u10cf\2\u10cf\2\u13a2"+
		"\2\u13f7\2\u1e02\2\u1e02\2\u1e04\2\u1e04\2\u1e06\2\u1e06\2\u1e08\2\u1e08"+
		"\2\u1e0a\2\u1e0a\2\u1e0c\2\u1e0c\2\u1e0e\2\u1e0e\2\u1e10\2\u1e10\2\u1e12"+
		"\2\u1e12\2\u1e14\2\u1e14\2\u1e16\2\u1e16\2\u1e18\2\u1e18\2\u1e1a\2\u1e1a"+
		"\2\u1e1c\2\u1e1c\2\u1e1e\2\u1e1e\2\u1e20\2\u1e20\2\u1e22\2\u1e22\2\u1e24"+
		"\2\u1e24\2\u1e26\2\u1e26\2\u1e28\2\u1e28\2\u1e2a\2\u1e2a\2\u1e2c\2\u1e2c"+
		"\2\u1e2e\2\u1e2e\2\u1e30\2\u1e30\2\u1e32\2\u1e32\2\u1e34\2\u1e34\2\u1e36"+
		"\2\u1e36\2\u1e38\2\u1e38\2\u1e3a\2\u1e3a\2\u1e3c\2\u1e3c\2\u1e3e\2\u1e3e"+
		"\2\u1e40\2\u1e40\2\u1e42\2\u1e42\2\u1e44\2\u1e44\2\u1e46\2\u1e46\2\u1e48"+
		"\2\u1e48\2\u1e4a\2\u1e4a\2\u1e4c\2\u1e4c\2\u1e4e\2\u1e4e\2\u1e50\2\u1e50"+
		"\2\u1e52\2\u1e52\2\u1e54\2\u1e54\2\u1e56\2\u1e56\2\u1e58\2\u1e58\2\u1e5a"+
		"\2\u1e5a\2\u1e5c\2\u1e5c\2\u1e5e\2\u1e5e\2\u1e60\2\u1e60\2\u1e62\2\u1e62"+
		"\2\u1e64\2\u1e64\2\u1e66\2\u1e66\2\u1e68\2\u1e68\2\u1e6a\2\u1e6a\2\u1e6c"+
		"\2\u1e6c\2\u1e6e\2\u1e6e\2\u1e70\2\u1e70\2\u1e72\2\u1e72\2\u1e74\2\u1e74"+
		"\2\u1e76\2\u1e76\2\u1e78\2\u1e78\2\u1e7a\2\u1e7a\2\u1e7c\2\u1e7c\2\u1e7e"+
		"\2\u1e7e\2\u1e80\2\u1e80\2\u1e82\2\u1e82\2\u1e84\2\u1e84\2\u1e86\2\u1e86"+
		"\2\u1e88\2\u1e88\2\u1e8a\2\u1e8a\2\u1e8c\2\u1e8c\2\u1e8e\2\u1e8e\2\u1e90"+
		"\2\u1e90\2\u1e92\2\u1e92\2\u1e94\2\u1e94\2\u1e96\2\u1e96\2\u1ea0\2\u1ea0"+
		"\2\u1ea2\2\u1ea2\2\u1ea4\2\u1ea4\2\u1ea6\2\u1ea6\2\u1ea8\2\u1ea8\2\u1eaa"+
		"\2\u1eaa\2\u1eac\2\u1eac\2\u1eae\2\u1eae\2\u1eb0\2\u1eb0\2\u1eb2\2\u1eb2"+
		"\2\u1eb4\2\u1eb4\2\u1eb6\2\u1eb6\2\u1eb8\2\u1eb8\2\u1eba\2\u1eba\2\u1ebc"+
		"\2\u1ebc\2\u1ebe\2\u1ebe\2\u1ec0\2\u1ec0\2\u1ec2\2\u1ec2\2\u1ec4\2\u1ec4"+
		"\2\u1ec6\2\u1ec6\2\u1ec8\2\u1ec8\2\u1eca\2\u1eca\2\u1ecc\2\u1ecc\2\u1ece"+
		"\2\u1ece\2\u1ed0\2\u1ed0\2\u1ed2\2\u1ed2\2\u1ed4\2\u1ed4\2\u1ed6\2\u1ed6"+
		"\2\u1ed8\2\u1ed8\2\u1eda\2\u1eda\2\u1edc\2\u1edc\2\u1ede\2\u1ede\2\u1ee0"+
		"\2\u1ee0\2\u1ee2\2\u1ee2\2\u1ee4\2\u1ee4\2\u1ee6\2\u1ee6\2\u1ee8\2\u1ee8"+
		"\2\u1eea\2\u1eea\2\u1eec\2\u1eec\2\u1eee\2\u1eee\2\u1ef0\2\u1ef0\2\u1ef2"+
		"\2\u1ef2\2\u1ef4\2\u1ef4\2\u1ef6\2\u1ef6\2\u1ef8\2\u1ef8\2\u1efa\2\u1efa"+
		"\2\u1efc\2\u1efc\2\u1efe\2\u1efe\2\u1f00\2\u1f00\2\u1f0a\2\u1f11\2\u1f1a"+
		"\2\u1f1f\2\u1f2a\2\u1f31\2\u1f3a\2\u1f41\2\u1f4a\2\u1f4f\2\u1f5b\2\u1f5b"+
		"\2\u1f5d\2\u1f5d\2\u1f5f\2\u1f5f\2\u1f61\2\u1f61\2\u1f6a\2\u1f71\2\u1fba"+
		"\2\u1fbd\2\u1fca\2\u1fcd\2\u1fda\2\u1fdd\2\u1fea\2\u1fee\2\u1ffa\2\u1ffd"+
		"\2\u2104\2\u2104\2\u2109\2\u2109\2\u210d\2\u210f\2\u2112\2\u2114\2\u2117"+
		"\2\u2117\2\u211b\2\u211f\2\u2126\2\u2126\2\u2128\2\u2128\2\u212a\2\u212a"+
		"\2\u212c\2\u212f\2\u2132\2\u2135\2\u2140\2\u2141\2\u2147\2\u2147\2\u2185"+
		"\2\u2185\2\u2c02\2\u2c30\2\u2c62\2\u2c62\2\u2c64\2\u2c66\2\u2c69\2\u2c69"+
		"\2\u2c6b\2\u2c6b\2\u2c6d\2\u2c6d\2\u2c6f\2\u2c72\2\u2c74\2\u2c74\2\u2c77"+
		"\2\u2c77\2\u2c80\2\u2c82\2\u2c84\2\u2c84\2\u2c86\2\u2c86\2\u2c88\2\u2c88"+
		"\2\u2c8a\2\u2c8a\2\u2c8c\2\u2c8c\2\u2c8e\2\u2c8e\2\u2c90\2\u2c90\2\u2c92"+
		"\2\u2c92\2\u2c94\2\u2c94\2\u2c96\2\u2c96\2\u2c98\2\u2c98\2\u2c9a\2\u2c9a"+
		"\2\u2c9c\2\u2c9c\2\u2c9e\2\u2c9e\2\u2ca0\2\u2ca0\2\u2ca2\2\u2ca2\2\u2ca4"+
		"\2\u2ca4\2\u2ca6\2\u2ca6\2\u2ca8\2\u2ca8\2\u2caa\2\u2caa\2\u2cac\2\u2cac"+
		"\2\u2cae\2\u2cae\2\u2cb0\2\u2cb0\2\u2cb2\2\u2cb2\2\u2cb4\2\u2cb4\2\u2cb6"+
		"\2\u2cb6\2\u2cb8\2\u2cb8\2\u2cba\2\u2cba\2\u2cbc\2\u2cbc\2\u2cbe\2\u2cbe"+
		"\2\u2cc0\2\u2cc0\2\u2cc2\2\u2cc2\2\u2cc4\2\u2cc4\2\u2cc6\2\u2cc6\2\u2cc8"+
		"\2\u2cc8\2\u2cca\2\u2cca\2\u2ccc\2\u2ccc\2\u2cce\2\u2cce\2\u2cd0\2\u2cd0"+
		"\2\u2cd2\2\u2cd2\2\u2cd4\2\u2cd4\2\u2cd6\2\u2cd6\2\u2cd8\2\u2cd8\2\u2cda"+
		"\2\u2cda\2\u2cdc\2\u2cdc\2\u2cde\2\u2cde\2\u2ce0\2\u2ce0\2\u2ce2\2\u2ce2"+
		"\2\u2ce4\2\u2ce4\2\u2ced\2\u2ced\2\u2cef\2\u2cef\2\u2cf4\2\u2cf4\2\ua642"+
		"\2\ua642\2\ua644\2\ua644\2\ua646\2\ua646\2\ua648\2\ua648\2\ua64a\2\ua64a"+
		"\2\ua64c\2\ua64c\2\ua64e\2\ua64e\2\ua650\2\ua650\2\ua652\2\ua652\2\ua654"+
		"\2\ua654\2\ua656\2\ua656\2\ua658\2\ua658\2\ua65a\2\ua65a\2\ua65c\2\ua65c"+
		"\2\ua65e\2\ua65e\2\ua660\2\ua660\2\ua662\2\ua662\2\ua664\2\ua664\2\ua666"+
		"\2\ua666\2\ua668\2\ua668\2\ua66a\2\ua66a\2\ua66c\2\ua66c\2\ua66e\2\ua66e"+
		"\2\ua682\2\ua682\2\ua684\2\ua684\2\ua686\2\ua686\2\ua688\2\ua688\2\ua68a"+
		"\2\ua68a\2\ua68c\2\ua68c\2\ua68e\2\ua68e\2\ua690\2\ua690\2\ua692\2\ua692"+
		"\2\ua694\2\ua694\2\ua696\2\ua696\2\ua698\2\ua698\2\ua69a\2\ua69a\2\ua69c"+
		"\2\ua69c\2\ua724\2\ua724\2\ua726\2\ua726\2\ua728\2\ua728\2\ua72a\2\ua72a"+
		"\2\ua72c\2\ua72c\2\ua72e\2\ua72e\2\ua730\2\ua730\2\ua734\2\ua734\2\ua736"+
		"\2\ua736\2\ua738\2\ua738\2\ua73a\2\ua73a\2\ua73c\2\ua73c\2\ua73e\2\ua73e"+
		"\2\ua740\2\ua740\2\ua742\2\ua742\2\ua744\2\ua744\2\ua746\2\ua746\2\ua748"+
		"\2\ua748\2\ua74a\2\ua74a\2\ua74c\2\ua74c\2\ua74e\2\ua74e\2\ua750\2\ua750"+
		"\2\ua752\2\ua752\2\ua754\2\ua754\2\ua756\2\ua756\2\ua758\2\ua758\2\ua75a"+
		"\2\ua75a\2\ua75c\2\ua75c\2\ua75e\2\ua75e\2\ua760\2\ua760\2\ua762\2\ua762"+
		"\2\ua764\2\ua764\2\ua766\2\ua766\2\ua768\2\ua768\2\ua76a\2\ua76a\2\ua76c"+
		"\2\ua76c\2\ua76e\2\ua76e\2\ua770\2\ua770\2\ua77b\2\ua77b\2\ua77d\2\ua77d"+
		"\2\ua77f\2\ua780\2\ua782\2\ua782\2\ua784\2\ua784\2\ua786\2\ua786\2\ua788"+
		"\2\ua788\2\ua78d\2\ua78d\2\ua78f\2\ua78f\2\ua792\2\ua792\2\ua794\2\ua794"+
		"\2\ua798\2\ua798\2\ua79a\2\ua79a\2\ua79c\2\ua79c\2\ua79e\2\ua79e\2\ua7a0"+
		"\2\ua7a0\2\ua7a2\2\ua7a2\2\ua7a4\2\ua7a4\2\ua7a6\2\ua7a6\2\ua7a8\2\ua7a8"+
		"\2\ua7aa\2\ua7aa\2\ua7ac\2\ua7b0\2\ua7b2\2\ua7b6\2\ua7b8\2\ua7b8\2\uff23"+
		"\2\uff3c\2\u0402\3\u0429\3\u04b2\3\u04d5\3\u0c82\3\u0cb4\3\u18a2\3\u18c1"+
		"\3\ud402\3\ud41b\3\ud436\3\ud44f\3\ud46a\3\ud483\3\ud49e\3\ud49e\3\ud4a0"+
		"\3\ud4a1\3\ud4a4\3\ud4a4\3\ud4a7\3\ud4a8\3\ud4ab\3\ud4ae\3\ud4b0\3\ud4b7"+
		"\3\ud4d2\3\ud4eb\3\ud506\3\ud507\3\ud509\3\ud50c\3\ud50f\3\ud516\3\ud518"+
		"\3\ud51e\3\ud53a\3\ud53b\3\ud53d\3\ud540\3\ud542\3\ud546\3\ud548\3\ud548"+
		"\3\ud54c\3\ud552\3\ud56e\3\ud587\3\ud5a2\3\ud5bb\3\ud5d6\3\ud5ef\3\ud60a"+
		"\3\ud623\3\ud63e\3\ud657\3\ud672\3\ud68b\3\ud6aa\3\ud6c2\3\ud6e4\3\ud6fc"+
		"\3\ud71e\3\ud736\3\ud758\3\ud770\3\ud792\3\ud7aa\3\ud7cc\3\ud7cc\3\ue902"+
		"\3\ue923\3\u0271\2\62\2;\2C\2\\\2a\2a\2c\2|\2\u00ac\2\u00ac\2\u00b7\2"+
		"\u00b7\2\u00bc\2\u00bc\2\u00c2\2\u00d8\2\u00da\2\u00f8\2\u00fa\2\u02c3"+
		"\2\u02c8\2\u02d3\2\u02e2\2\u02e6\2\u02ee\2\u02ee\2\u02f0\2\u02f0\2\u0372"+
		"\2\u0376\2\u0378\2\u0379\2\u037c\2\u037f\2\u0381\2\u0381\2\u0388\2\u0388"+
		"\2\u038a\2\u038c\2\u038e\2\u038e\2\u0390\2\u03a3\2\u03a5\2\u03f7\2\u03f9"+
		"\2\u0483\2\u048c\2\u0531\2\u0533\2\u0558\2\u055b\2\u055b\2\u0563\2\u0589"+
		"\2\u05d2\2\u05ec\2\u05f2\2\u05f4\2\u0622\2\u064c\2\u0662\2\u066b\2\u0670"+
		"\2\u0671\2\u0673\2\u06d5\2\u06d7\2\u06d7\2\u06e7\2\u06e8\2\u06f0\2\u06fe"+
		"\2\u0701\2\u0701\2\u0712\2\u0712\2\u0714\2\u0731\2\u074f\2\u07a7\2\u07b3"+
		"\2\u07b3\2\u07c2\2\u07ec\2\u07f6\2\u07f7\2\u07fc\2\u07fc\2\u0802\2\u0817"+
		"\2\u081c\2\u081c\2\u0826\2\u0826\2\u082a\2\u082a\2\u0842\2\u085a\2\u0862"+
		"\2\u086c\2\u08a2\2\u08b6\2\u08b8\2\u08bf\2\u0906\2\u093b\2\u093f\2\u093f"+
		"\2\u0952\2\u0952\2\u095a\2\u0963\2\u0968\2\u0971\2\u0973\2\u0982\2\u0987"+
		"\2\u098e\2\u0991\2\u0992\2\u0995\2\u09aa\2\u09ac\2\u09b2\2\u09b4\2\u09b4"+
		"\2\u09b8\2\u09bb\2\u09bf\2\u09bf\2\u09d0\2\u09d0\2\u09de\2\u09df\2\u09e1"+
		"\2\u09e3\2\u09e8\2\u09f3\2\u09fe\2\u09fe\2\u0a07\2\u0a0c\2\u0a11\2\u0a12"+
		"\2\u0a15\2\u0a2a\2\u0a2c\2\u0a32\2\u0a34\2\u0a35\2\u0a37\2\u0a38\2\u0a3a"+
		"\2\u0a3b\2\u0a5b\2\u0a5e\2\u0a60\2\u0a60\2\u0a68\2\u0a71\2\u0a74\2\u0a76"+
		"\2\u0a87\2\u0a8f\2\u0a91\2\u0a93\2\u0a95\2\u0aaa\2\u0aac\2\u0ab2\2\u0ab4"+
		"\2\u0ab5\2\u0ab7\2\u0abb\2\u0abf\2\u0abf\2\u0ad2\2\u0ad2\2\u0ae2\2\u0ae3"+
		"\2\u0ae8\2\u0af1\2\u0afb\2\u0afb\2\u0b07\2\u0b0e\2\u0b11\2\u0b12\2\u0b15"+
		"\2\u0b2a\2\u0b2c\2\u0b32\2\u0b34\2\u0b35\2\u0b37\2\u0b3b\2\u0b3f\2\u0b3f"+
		"\2\u0b5e\2\u0b5f\2\u0b61\2\u0b63\2\u0b68\2\u0b71\2\u0b73\2\u0b73\2\u0b85"+
		"\2\u0b85\2\u0b87\2\u0b8c\2\u0b90\2\u0b92\2\u0b94\2\u0b97\2\u0b9b\2\u0b9c"+
		"\2\u0b9e\2\u0b9e\2\u0ba0\2\u0ba1\2\u0ba5\2\u0ba6\2\u0baa\2\u0bac\2\u0bb0"+
		"\2\u0bbb\2\u0bd2\2\u0bd2\2\u0be8\2\u0bf1\2\u0c07\2\u0c0e\2\u0c10\2\u0c12"+
		"\2\u0c14\2\u0c2a\2\u0c2c\2\u0c3b\2\u0c3f\2\u0c3f\2\u0c5a\2\u0c5c\2\u0c62"+
		"\2\u0c63\2\u0c68\2\u0c71\2\u0c82\2\u0c82\2\u0c87\2\u0c8e\2\u0c90\2\u0c92"+
		"\2\u0c94\2\u0caa\2\u0cac\2\u0cb5\2\u0cb7\2\u0cbb\2\u0cbf\2\u0cbf\2\u0ce0"+
		"\2\u0ce0\2\u0ce2\2\u0ce3\2\u0ce8\2\u0cf1\2\u0cf3\2\u0cf4\2\u0d07\2\u0d0e"+
		"\2\u0d10\2\u0d12\2\u0d14\2\u0d3c\2\u0d3f\2\u0d3f\2\u0d50\2\u0d50\2\u0d56"+
		"\2\u0d58\2\u0d61\2\u0d63\2\u0d68\2\u0d71\2\u0d7c\2\u0d81\2\u0d87\2\u0d98"+
		"\2\u0d9c\2\u0db3\2\u0db5\2\u0dbd\2\u0dbf\2\u0dbf\2\u0dc2\2\u0dc8\2\u0de8"+
		"\2\u0df1\2\u0e03\2\u0e32\2\u0e34\2\u0e35\2\u0e42\2\u0e48\2\u0e52\2\u0e5b"+
		"\2\u0e83\2\u0e84\2\u0e86\2\u0e86\2\u0e89\2\u0e8a\2\u0e8c\2\u0e8c\2\u0e8f"+
		"\2\u0e8f\2\u0e96\2\u0e99\2\u0e9b\2\u0ea1\2\u0ea3\2\u0ea5\2\u0ea7\2\u0ea7"+
		"\2\u0ea9\2\u0ea9\2\u0eac\2\u0ead\2\u0eaf\2\u0eb2\2\u0eb4\2\u0eb5\2\u0ebf"+
		"\2\u0ebf\2\u0ec2\2\u0ec6\2\u0ec8\2\u0ec8\2\u0ed2\2\u0edb\2\u0ede\2\u0ee1"+
		"\2\u0f02\2\u0f02\2\u0f22\2\u0f2b\2\u0f42\2\u0f49\2\u0f4b\2\u0f6e\2\u0f8a"+
		"\2\u0f8e\2\u1002\2\u102c\2\u1041\2\u104b\2\u1052\2\u1057\2\u105c\2\u105f"+
		"\2\u1063\2\u1063\2\u1067\2\u1068\2\u1070\2\u1072\2\u1077\2\u1083\2\u1090"+
		"\2\u1090\2\u1092\2\u109b\2\u10a2\2\u10c7\2\u10c9\2\u10c9\2\u10cf\2\u10cf"+
		"\2\u10d2\2\u10fc\2\u10fe\2\u124a\2\u124c\2\u124f\2\u1252\2\u1258\2\u125a"+
		"\2\u125a\2\u125c\2\u125f\2\u1262\2\u128a\2\u128c\2\u128f\2\u1292\2\u12b2"+
		"\2\u12b4\2\u12b7\2\u12ba\2\u12c0\2\u12c2\2\u12c2\2\u12c4\2\u12c7\2\u12ca"+
		"\2\u12d8\2\u12da\2\u1312\2\u1314\2\u1317\2\u131a\2\u135c\2\u1382\2\u1391"+
		"\2\u13a2\2\u13f7\2\u13fa\2\u13ff\2\u1403\2\u166e\2\u1671\2\u1681\2\u1683"+
		"\2\u169c\2\u16a2\2\u16ec\2\u16f3\2\u16fa\2\u1702\2\u170e\2\u1710\2\u1713"+
		"\2\u1722\2\u1733\2\u1742\2\u1753\2\u1762\2\u176e\2\u1770\2\u1772\2\u1782"+
		"\2\u17b5\2\u17d9\2\u17d9\2\u17de\2\u17de\2\u17e2\2\u17eb\2\u1812\2\u181b"+
		"\2\u1822\2\u1879\2\u1882\2\u1886\2\u1889\2\u18aa\2\u18ac\2\u18ac\2\u18b2"+
		"\2\u18f7\2\u1902\2\u1920\2\u1948\2\u196f\2\u1972\2\u1976\2\u1982\2\u19ad"+
		"\2\u19b2\2\u19cb\2\u19d2\2\u19db\2\u1a02\2\u1a18\2\u1a22\2\u1a56\2\u1a82"+
		"\2\u1a8b\2\u1a92\2\u1a9b\2\u1aa9\2\u1aa9\2\u1b07\2\u1b35\2\u1b47\2\u1b4d"+
		"\2\u1b52\2\u1b5b\2\u1b85\2\u1ba2\2\u1bb0\2\u1be7\2\u1c02\2\u1c25\2\u1c42"+
		"\2\u1c4b\2\u1c4f\2\u1c7f\2\u1c82\2\u1c8a\2\u1ceb\2\u1cee\2\u1cf0\2\u1cf3"+
		"\2\u1cf7\2\u1cf8\2\u1d02\2\u1dc1\2\u1e02\2\u1f17\2\u1f1a\2\u1f1f\2\u1f22"+
		"\2\u1f47\2\u1f4a\2\u1f4f\2\u1f52\2\u1f59\2\u1f5b\2\u1f5b\2\u1f5d\2\u1f5d"+
		"\2\u1f5f\2\u1f5f\2\u1f61\2\u1f7f\2\u1f82\2\u1fb6\2\u1fb8\2\u1fbe\2\u1fc0"+
		"\2\u1fc0\2\u1fc4\2\u1fc6\2\u1fc8\2\u1fce\2\u1fd2\2\u1fd5\2\u1fd8\2\u1fdd"+
		"\2\u1fe2\2\u1fee\2\u1ff4\2\u1ff6\2\u1ff8\2\u1ffe\2\u2073\2\u2073\2\u2081"+
		"\2\u2081\2\u2092\2\u209e\2\u2104\2\u2104\2\u2109\2\u2109\2\u210c\2\u2115"+
		"\2\u2117\2\u2117\2\u211b\2\u211f\2\u2126\2\u2126\2\u2128\2\u2128\2\u212a"+
		"\2\u212a\2\u212c\2\u212f\2\u2131\2\u213b\2\u213e\2\u2141\2\u2147\2\u214b"+
		"\2\u2150\2\u2150\2\u2185\2\u2186\2\u2c02\2\u2c30\2\u2c32\2\u2c60\2\u2c62"+
		"\2\u2ce6\2\u2ced\2\u2cf0\2\u2cf4\2\u2cf5\2\u2d02\2\u2d27\2\u2d29\2\u2d29"+
		"\2\u2d2f\2\u2d2f\2\u2d32\2\u2d69\2\u2d71\2\u2d71\2\u2d82\2\u2d98\2\u2da2"+
		"\2\u2da8\2\u2daa\2\u2db0\2\u2db2\2\u2db8\2\u2dba\2\u2dc0\2\u2dc2\2\u2dc8"+
		"\2\u2dca\2\u2dd0\2\u2dd2\2\u2dd8\2\u2dda\2\u2de0\2\u2e31\2\u2e31\2\u3007"+
		"\2\u3008\2\u3033\2\u3037\2\u303d\2\u303e\2\u3043\2\u3098\2\u309f\2\u30a1"+
		"\2\u30a3\2\u30fc\2\u30fe\2\u3101\2\u3107\2\u3130\2\u3133\2\u3190\2\u31a2"+
		"\2\u31bc\2\u31f2\2\u3201\2\u3402\2\u4db7\2\u4e02\2\u9fec\2\ua002\2\ua48e"+
		"\2\ua4d2\2\ua4ff\2\ua502\2\ua60e\2\ua612\2\ua62d\2\ua642\2\ua670\2\ua681"+
		"\2\ua69f\2\ua6a2\2\ua6e7\2\ua719\2\ua721\2\ua724\2\ua78a\2\ua78d\2\ua7b0"+
		"\2\ua7b2\2\ua7b9\2\ua7f9\2\ua803\2\ua805\2\ua807\2\ua809\2\ua80c\2\ua80e"+
		"\2\ua824\2\ua842\2\ua875\2\ua884\2\ua8b5\2\ua8d2\2\ua8db\2\ua8f4\2\ua8f9"+
		"\2\ua8fd\2\ua8fd\2\ua8ff\2\ua8ff\2\ua902\2\ua927\2\ua932\2\ua948\2\ua962"+
		"\2\ua97e\2\ua986\2\ua9b4\2\ua9d1\2\ua9db\2\ua9e2\2\ua9e6\2\ua9e8\2\uaa00"+
		"\2\uaa02\2\uaa2a\2\uaa42\2\uaa44\2\uaa46\2\uaa4d\2\uaa52\2\uaa5b\2\uaa62"+
		"\2\uaa78\2\uaa7c\2\uaa7c\2\uaa80\2\uaab1\2\uaab3\2\uaab3\2\uaab7\2\uaab8"+
		"\2\uaabb\2\uaabf\2\uaac2\2\uaac2\2\uaac4\2\uaac4\2\uaadd\2\uaadf\2\uaae2"+
		"\2\uaaec\2\uaaf4\2\uaaf6\2\uab03\2\uab08\2\uab0b\2\uab10\2\uab13\2\uab18"+
		"\2\uab22\2\uab28\2\uab2a\2\uab30\2\uab32\2\uab5c\2\uab5e\2\uab67\2\uab72"+
		"\2\uabe4\2\uabf2\2\uabfb\2\uac02\2\ud7a5\2\ud7b2\2\ud7c8\2\ud7cd\2\ud7fd"+
		"\2\uf902\2\ufa6f\2\ufa72\2\ufadb\2\ufb02\2\ufb08\2\ufb15\2\ufb19\2\ufb1f"+
		"\2\ufb1f\2\ufb21\2\ufb2a\2\ufb2c\2\ufb38\2\ufb3a\2\ufb3e\2\ufb40\2\ufb40"+
		"\2\ufb42\2\ufb43\2\ufb45\2\ufb46\2\ufb48\2\ufbb3\2\ufbd5\2\ufd3f\2\ufd52"+
		"\2\ufd91\2\ufd94\2\ufdc9\2\ufdf2\2\ufdfd\2\ufe72\2\ufe76\2\ufe78\2\ufefe"+
		"\2\uff12\2\uff1b\2\uff23\2\uff3c\2\uff43\2\uff5c\2\uff68\2\uffc0\2\uffc4"+
		"\2\uffc9\2\uffcc\2\uffd1\2\uffd4\2\uffd9\2\uffdc\2\uffde\2\2\3\r\3\17"+
		"\3(\3*\3<\3>\3?\3A\3O\3R\3_\3\u0082\3\u00fc\3\u0282\3\u029e\3\u02a2\3"+
		"\u02d2\3\u0302\3\u0321\3\u032f\3\u0342\3\u0344\3\u034b\3\u0352\3\u0377"+
		"\3\u0382\3\u039f\3\u03a2\3\u03c5\3\u03ca\3\u03d1\3\u0402\3\u049f\3\u04a2"+
		"\3\u04ab\3\u04b2\3\u04d5\3\u04da\3\u04fd\3\u0502\3\u0529\3\u0532\3\u0565"+
		"\3\u0602\3\u0738\3\u0742\3\u0757\3\u0762\3\u0769\3\u0802\3\u0807\3\u080a"+
		"\3\u080a\3\u080c\3\u0837\3\u0839\3\u083a\3\u083e\3\u083e\3\u0841\3\u0857"+
		"\3\u0862\3\u0878\3\u0882\3\u08a0\3\u08e2\3\u08f4\3\u08f6\3\u08f7\3\u0902"+
		"\3\u0917\3\u0922\3\u093b\3\u0982\3\u09b9\3\u09c0\3\u09c1\3\u0a02\3\u0a02"+
		"\3\u0a12\3\u0a15\3\u0a17\3\u0a19\3\u0a1b\3\u0a35\3\u0a62\3\u0a7e\3\u0a82"+
		"\3\u0a9e\3\u0ac2\3\u0ac9\3\u0acb\3\u0ae6\3\u0b02\3\u0b37\3\u0b42\3\u0b57"+
		"\3\u0b62\3\u0b74\3\u0b82\3\u0b93\3\u0c02\3\u0c4a\3\u0c82\3\u0cb4\3\u0cc2"+
		"\3\u0cf4\3\u1005\3\u1039\3\u1068\3\u1071\3\u1085\3\u10b1\3\u10d2\3\u10ea"+
		"\3\u10f2\3\u10fb\3\u1105\3\u1128\3\u1138\3\u1141\3\u1152\3\u1174\3\u1178"+
		"\3\u1178\3\u1185\3\u11b4\3\u11c3\3\u11c6\3\u11d2\3\u11dc\3\u11de\3\u11de"+
		"\3\u1202\3\u1213\3\u1215\3\u122d\3\u1282\3\u1288\3\u128a\3\u128a\3\u128c"+
		"\3\u128f\3\u1291\3\u129f\3\u12a1\3\u12aa\3\u12b2\3\u12e0\3\u12f2\3\u12fb"+
		"\3\u1307\3\u130e\3\u1311\3\u1312\3\u1315\3\u132a\3\u132c\3\u1332\3\u1334"+
		"\3\u1335\3\u1337\3\u133b\3\u133f\3\u133f\3\u1352\3\u1352\3\u135f\3\u1363"+
		"\3\u1402\3\u1436\3\u1449\3\u144c\3\u1452\3\u145b\3\u1482\3\u14b1\3\u14c6"+
		"\3\u14c7\3\u14c9\3\u14c9\3\u14d2\3\u14db\3\u1582\3\u15b0\3\u15da\3\u15dd"+
		"\3\u1602\3\u1631\3\u1646\3\u1646\3\u1652\3\u165b\3\u1682\3\u16ac\3\u16c2"+
		"\3\u16cb\3\u1702\3\u171b\3\u1732\3\u173b\3\u18a2\3\u18eb\3\u1901\3\u1901"+
		"\3\u1a02\3\u1a02\3\u1a0d\3\u1a34\3\u1a3c\3\u1a3c\3\u1a52\3\u1a52\3\u1a5e"+
		"\3\u1a85\3\u1a88\3\u1a8b\3\u1ac2\3\u1afa\3\u1c02\3\u1c0a\3\u1c0c\3\u1c30"+
		"\3\u1c42\3\u1c42\3\u1c52\3\u1c5b\3\u1c74\3\u1c91\3\u1d02\3\u1d08\3\u1d0a"+
		"\3\u1d0b\3\u1d0d\3\u1d32\3\u1d48\3\u1d48\3\u1d52\3\u1d5b\3\u2002\3\u239b"+
		"\3\u2482\3\u2545\3\u3002\3\u3430\3\u4402\3\u4648\3\u6802\3\u6a3a\3\u6a42"+
		"\3\u6a60\3\u6a62\3\u6a6b\3\u6ad2\3\u6aef\3\u6b02\3\u6b31\3\u6b42\3\u6b45"+
		"\3\u6b52\3\u6b5b\3\u6b65\3\u6b79\3\u6b7f\3\u6b91\3\u6f02\3\u6f46\3\u6f52"+
		"\3\u6f52\3\u6f95\3\u6fa1\3\u6fe2\3\u6fe3\3\u7002\3\u87ee\3\u8802\3\u8af4"+
		"\3\ub002\3\ub120\3\ub172\3\ub2fd\3\ubc02\3\ubc6c\3\ubc72\3\ubc7e\3\ubc82"+
		"\3\ubc8a\3\ubc92\3\ubc9b\3\ud402\3\ud456\3\ud458\3\ud49e\3\ud4a0\3\ud4a1"+
		"\3\ud4a4\3\ud4a4\3\ud4a7\3\ud4a8\3\ud4ab\3\ud4ae\3\ud4b0\3\ud4bb\3\ud4bd"+
		"\3\ud4bd\3\ud4bf\3\ud4c5\3\ud4c7\3\ud507\3\ud509\3\ud50c\3\ud50f\3\ud516"+
		"\3\ud518\3\ud51e\3\ud520\3\ud53b\3\ud53d\3\ud540\3\ud542\3\ud546\3\ud548"+
		"\3\ud548\3\ud54c\3\ud552\3\ud554\3\ud6a7\3\ud6aa\3\ud6c2\3\ud6c4\3\ud6dc"+
		"\3\ud6de\3\ud6fc\3\ud6fe\3\ud716\3\ud718\3\ud736\3\ud738\3\ud750\3\ud752"+
		"\3\ud770\3\ud772\3\ud78a\3\ud78c\3\ud7aa\3\ud7ac\3\ud7c4\3\ud7c6\3\ud7cd"+
		"\3\ud7d0\3\ud801\3\ue802\3\ue8c6\3\ue902\3\ue945\3\ue952\3\ue95b\3\uee02"+
		"\3\uee05\3\uee07\3\uee21\3\uee23\3\uee24\3\uee26\3\uee26\3\uee29\3\uee29"+
		"\3\uee2b\3\uee34\3\uee36\3\uee39\3\uee3b\3\uee3b\3\uee3d\3\uee3d\3\uee44"+
		"\3\uee44\3\uee49\3\uee49\3\uee4b\3\uee4b\3\uee4d\3\uee4d\3\uee4f\3\uee51"+
		"\3\uee53\3\uee54\3\uee56\3\uee56\3\uee59\3\uee59\3\uee5b\3\uee5b\3\uee5d"+
		"\3\uee5d\3\uee5f\3\uee5f\3\uee61\3\uee61\3\uee63\3\uee64\3\uee66\3\uee66"+
		"\3\uee69\3\uee6c\3\uee6e\3\uee74\3\uee76\3\uee79\3\uee7b\3\uee7e\3\uee80"+
		"\3\uee80\3\uee82\3\uee8b\3\uee8d\3\uee9d\3\ueea3\3\ueea5\3\ueea7\3\ueeab"+
		"\3\ueead\3\ueebd\3\2\4\ua6d8\4\ua702\4\ub736\4\ub742\4\ub81f\4\ub822\4"+
		"\ucea3\4\uceb2\4\uebe2\4\uf802\4\ufa1f\4\u01fa\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2"+
		"\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2"+
		"\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2"+
		"\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2"+
		"\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y"+
		"\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2"+
		"\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2"+
		"\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177"+
		"\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2"+
		"\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u0097\3\2\2\2\5\u009c"+
		"\3\2\2\2\7\u00a3\3\2\2\2\t\u00a8\3\2\2\2\13\u00b0\3\2\2\2\r\u00b3\3\2"+
		"\2\2\17\u00b8\3\2\2\2\21\u00bd\3\2\2\2\23\u00c5\3\2\2\2\25\u00cc\3\2\2"+
		"\2\27\u00d0\3\2\2\2\31\u00d7\3\2\2\2\33\u00de\3\2\2\2\35\u00e3\3\2\2\2"+
		"\37\u00ea\3\2\2\2!\u00f3\3\2\2\2#\u00f9\3\2\2\2%\u00fe\3\2\2\2\'\u0108"+
		"\3\2\2\2)\u010d\3\2\2\2+\u0113\3\2\2\2-\u0117\3\2\2\2/\u011b\3\2\2\2\61"+
		"\u0121\3\2\2\2\63\u0127\3\2\2\2\65\u012a\3\2\2\2\67\u0130\3\2\2\29\u0133"+
		"\3\2\2\2;\u0135\3\2\2\2=\u0137\3\2\2\2?\u0139\3\2\2\2A\u013b\3\2\2\2C"+
		"\u013d\3\2\2\2E\u013f\3\2\2\2G\u0141\3\2\2\2I\u0143\3\2\2\2K\u0145\3\2"+
		"\2\2M\u0147\3\2\2\2O\u0149\3\2\2\2Q\u014c\3\2\2\2S\u014f\3\2\2\2U\u0152"+
		"\3\2\2\2W\u0156\3\2\2\2Y\u0159\3\2\2\2[\u015c\3\2\2\2]\u015e\3\2\2\2_"+
		"\u0161\3\2\2\2a\u0163\3\2\2\2c\u0166\3\2\2\2e\u0168\3\2\2\2g\u016a\3\2"+
		"\2\2i\u016c\3\2\2\2k\u016f\3\2\2\2m\u0172\3\2\2\2o\u0175\3\2\2\2q\u0177"+
		"\3\2\2\2s\u0179\3\2\2\2u\u017b\3\2\2\2w\u017d\3\2\2\2y\u017f\3\2\2\2{"+
		"\u0181\3\2\2\2}\u0198\3\2\2\2\177\u019a\3\2\2\2\u0081\u01a1\3\2\2\2\u0083"+
		"\u01aa\3\2\2\2\u0085\u01b4\3\2\2\2\u0087\u01b7\3\2\2\2\u0089\u01bd\3\2"+
		"\2\2\u008b\u01cc\3\2\2\2\u008d\u01d2\3\2\2\2\u008f\u01dd\3\2\2\2\u0091"+
		"\u01e0\3\2\2\2\u0093\u01e4\3\2\2\2\u0095\u01e8\3\2\2\2\u0097\u0098\7h"+
		"\2\2\u0098\u0099\7w\2\2\u0099\u009a\7p\2\2\u009a\u009b\7e\2\2\u009b\4"+
		"\3\2\2\2\u009c\u009d\7u\2\2\u009d\u009e\7y\2\2\u009e\u009f\7k\2\2\u009f"+
		"\u00a0\7v\2\2\u00a0\u00a1\7e\2\2\u00a1\u00a2\7j\2\2\u00a2\6\3\2\2\2\u00a3"+
		"\u00a4\7e\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7\7g\2\2"+
		"\u00a7\b\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7h"+
		"\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af"+
		"\7v\2\2\u00af\n\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7h\2\2\u00b2\f"+
		"\3\2\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7u\2\2\u00b6"+
		"\u00b7\7g\2\2\u00b7\16\3\2\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7{\2\2\u00ba"+
		"\u00bb\7r\2\2\u00bb\u00bc\7g\2\2\u00bc\20\3\2\2\2\u00bd\u00be\7r\2\2\u00be"+
		"\u00bf\7c\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7m\2\2\u00c1\u00c2\7c\2\2"+
		"\u00c2\u00c3\7i\2\2\u00c3\u00c4\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7"+
		"k\2\2\u00c6\u00c7\7o\2\2\u00c7\u00c8\7r\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca"+
		"\7t\2\2\u00ca\u00cb\7v\2\2\u00cb\24\3\2\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce"+
		"\7k\2\2\u00ce\u00cf\7n\2\2\u00cf\26\3\2\2\2\u00d0\u00d4\t\f\2\2\u00d1"+
		"\u00d3\t\r\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2"+
		"\2\2\u00d4\u00d5\3\2\2\2\u00d5\30\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8"+
		"\7u\2\2\u00d8\u00d9\7s\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7c\2\2\u00db"+
		"\u00dc\7t\2\2\u00dc\u00dd\7g\2\2\u00dd\32\3\2\2\2\u00de\u00df\7t\2\2\u00df"+
		"\u00e0\7g\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2\7v\2\2\u00e2\34\3\2\2\2\u00e3"+
		"\u00e4\7e\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7e\2\2"+
		"\u00e7\u00e8\7n\2\2\u00e8\u00e9\7g\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7"+
		"v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef"+
		"\7p\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7g\2\2\u00f2"+
		" \3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7j\2\2\u00f5\u00f6\7c\2\2\u00f6"+
		"\u00f7\7r\2\2\u00f7\u00f8\7g\2\2\u00f8\"\3\2\2\2\u00f9\u00fa\7f\2\2\u00fa"+
		"\u00fb\7t\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7y\2\2\u00fd$\3\2\2\2\u00fe"+
		"\u00ff\7%\2\2\u00ff\u0100\7x\2\2\u0100\u0101\7k\2\2\u0101\u0102\7g\2\2"+
		"\u0102\u0103\7y\2\2\u0103\u0104\7r\2\2\u0104\u0105\7q\2\2\u0105\u0106"+
		"\7t\2\2\u0106\u0107\7v\2\2\u0107&\3\2\2\2\u0108\u0109\7n\2\2\u0109\u010a"+
		"\7g\2\2\u010a\u010b\7h\2\2\u010b\u010c\7v\2\2\u010c(\3\2\2\2\u010d\u010e"+
		"\7t\2\2\u010e\u010f\7k\2\2\u010f\u0110\7i\2\2\u0110\u0111\7j\2\2\u0111"+
		"\u0112\7v\2\2\u0112*\3\2\2\2\u0113\u0114\7v\2\2\u0114\u0115\7q\2\2\u0115"+
		"\u0116\7r\2\2\u0116,\3\2\2\2\u0117\u0118\7d\2\2\u0118\u0119\7q\2\2\u0119"+
		"\u011a\7v\2\2\u011a.\3\2\2\2\u011b\u011c\7q\2\2\u011c\u011d\7w\2\2\u011d"+
		"\u011e\7v\2\2\u011e\u011f\7g\2\2\u011f\u0120\7t\2\2\u0120\60\3\2\2\2\u0121"+
		"\u0122\7k\2\2\u0122\u0123\7p\2\2\u0123\u0124\7p\2\2\u0124\u0125\7g\2\2"+
		"\u0125\u0126\7t\2\2\u0126\62\3\2\2\2\u0127\u0128\7q\2\2\u0128\u0129\7"+
		"p\2\2\u0129\64\3\2\2\2\u012a\u012b\7w\2\2\u012b\u012c\7p\2\2\u012c\u012d"+
		"\7f\2\2\u012d\u012e\7g\2\2\u012e\u012f\7t\2\2\u012f\66\3\2\2\2\u0130\u0131"+
		"\7k\2\2\u0131\u0132\7p\2\2\u01328\3\2\2\2\u0133\u0134\7*\2\2\u0134:\3"+
		"\2\2\2\u0135\u0136\7+\2\2\u0136<\3\2\2\2\u0137\u0138\7}\2\2\u0138>\3\2"+
		"\2\2\u0139\u013a\7\177\2\2\u013a@\3\2\2\2\u013b\u013c\7]\2\2\u013cB\3"+
		"\2\2\2\u013d\u013e\7_\2\2\u013eD\3\2\2\2\u013f\u0140\7?\2\2\u0140F\3\2"+
		"\2\2\u0141\u0142\7.\2\2\u0142H\3\2\2\2\u0143\u0144\7=\2\2\u0144J\3\2\2"+
		"\2\u0145\u0146\7<\2\2\u0146L\3\2\2\2\u0147\u0148\7\60\2\2\u0148N\3\2\2"+
		"\2\u0149\u014a\7-\2\2\u014a\u014b\7-\2\2\u014bP\3\2\2\2\u014c\u014d\7"+
		"/\2\2\u014d\u014e\7/\2\2\u014eR\3\2\2\2\u014f\u0150\7q\2\2\u0150\u0151"+
		"\7t\2\2\u0151T\3\2\2\2\u0152\u0153\7c\2\2\u0153\u0154\7p\2\2\u0154\u0155"+
		"\7f\2\2\u0155V\3\2\2\2\u0156\u0157\7?\2\2\u0157\u0158\7?\2\2\u0158X\3"+
		"\2\2\2\u0159\u015a\7#\2\2\u015a\u015b\7?\2\2\u015bZ\3\2\2\2\u015c\u015d"+
		"\7>\2\2\u015d\\\3\2\2\2\u015e\u015f\7>\2\2\u015f\u0160\7?\2\2\u0160^\3"+
		"\2\2\2\u0161\u0162\7@\2\2\u0162`\3\2\2\2\u0163\u0164\7@\2\2\u0164\u0165"+
		"\7?\2\2\u0165b\3\2\2\2\u0166\u0167\7~\2\2\u0167d\3\2\2\2\u0168\u0169\7"+
		"\61\2\2\u0169f\3\2\2\2\u016a\u016b\7\'\2\2\u016bh\3\2\2\2\u016c\u016d"+
		"\7>\2\2\u016d\u016e\7>\2\2\u016ej\3\2\2\2\u016f\u0170\7@\2\2\u0170\u0171"+
		"\7@\2\2\u0171l\3\2\2\2\u0172\u0173\7(\2\2\u0173\u0174\7`\2\2\u0174n\3"+
		"\2\2\2\u0175\u0176\7#\2\2\u0176p\3\2\2\2\u0177\u0178\7-\2\2\u0178r\3\2"+
		"\2\2\u0179\u017a\7/\2\2\u017at\3\2\2\2\u017b\u017c\7`\2\2\u017cv\3\2\2"+
		"\2\u017d\u017e\7,\2\2\u017ex\3\2\2\2\u017f\u0180\7(\2\2\u0180z\3\2\2\2"+
		"\u0181\u0185\t\2\2\2\u0182\u0184\t\3\2\2\u0183\u0182\3\2\2\2\u0184\u0187"+
		"\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186|\3\2\2\2\u0187"+
		"\u0185\3\2\2\2\u0188\u0191\5\u0093J\2\u0189\u018b\7\60\2\2\u018a\u018c"+
		"\5\u0093J\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2"+
		"\2\u018d\u018f\5\u0095K\2\u018e\u018d\3\2\2\2\u018e\u018f\3\2\2\2\u018f"+
		"\u0192\3\2\2\2\u0190\u0192\5\u0095K\2\u0191\u0189\3\2\2\2\u0191\u0190"+
		"\3\2\2\2\u0192\u0199\3\2\2\2\u0193\u0194\7\60\2\2\u0194\u0196\5\u0093"+
		"J\2\u0195\u0197\5\u0095K\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197"+
		"\u0199\3\2\2\2\u0198\u0188\3\2\2\2\u0198\u0193\3\2\2\2\u0199~\3\2\2\2"+
		"\u019a\u019d\7)\2\2\u019b\u019e\n\4\2\2\u019c\u019e\5\u008fH\2\u019d\u019b"+
		"\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\7)\2\2\u01a0"+
		"\u0080\3\2\2\2\u01a1\u01a5\7b\2\2\u01a2\u01a4\n\5\2\2\u01a3\u01a2\3\2"+
		"\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6"+
		"\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9\7b\2\2\u01a9\u0082\3\2"+
		"\2\2\u01aa\u01af\7$\2\2\u01ab\u01ae\n\6\2\2\u01ac\u01ae\5\u008fH\2\u01ad"+
		"\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2"+
		"\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2"+
		"\u01b3\7$\2\2\u01b3\u0084\3\2\2\2\u01b4\u01b5\5\u0091I\2\u01b5\u0086\3"+
		"\2\2\2\u01b6\u01b8\t\7\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9"+
		"\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\bD"+
		"\2\2\u01bc\u0088\3\2\2\2\u01bd\u01be\7\61\2\2\u01be\u01bf\7,\2\2\u01bf"+
		"\u01c3\3\2\2\2\u01c0\u01c2\13\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3"+
		"\2\2\2\u01c3\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5"+
		"\u01c3\3\2\2\2\u01c6\u01c7\7,\2\2\u01c7\u01c8\7\61\2\2\u01c8\u01c9\3\2"+
		"\2\2\u01c9\u01ca\bE\2\2\u01ca\u008a\3\2\2\2\u01cb\u01cd\t\b\2\2\u01cc"+
		"\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2"+
		"\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\bF\2\2\u01d1\u008c\3\2\2\2\u01d2"+
		"\u01d3\7\61\2\2\u01d3\u01d4\7\61\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d7\n"+
		"\b\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8"+
		"\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dc\bG"+
		"\2\2\u01dc\u008e\3\2\2\2\u01dd\u01de\7^\2\2\u01de\u01df\t\t\2\2\u01df"+
		"\u0090\3\2\2\2\u01e0\u01e1\5\u0093J\2\u01e1\u01e2\7\'\2\2\u01e2\u0092"+
		"\3\2\2\2\u01e3\u01e5\t\3\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6"+
		"\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u0094\3\2\2\2\u01e8\u01ea\t\n"+
		"\2\2\u01e9\u01eb\t\13\2\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb"+
		"\u01ec\3\2\2\2\u01ec\u01ed\5\u0093J\2\u01ed\u0096\3\2\2\2\24\2\u00d4\u0185"+
		"\u018b\u018e\u0191\u0196\u0198\u019d\u01a5\u01ad\u01af\u01b9\u01c3\u01ce"+
		"\u01d8\u01e6\u01ea\3\2\3\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}