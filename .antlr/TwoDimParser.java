// Generated from /home/pbilko/Desktop/SZKOŁA/KOMPILATORY/Language-for-2D-graphics/TwoDimParser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TwoDimParser extends TwoDimParserBase {
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
	public static final int
		RULE_sourceFile = 0, RULE_viewportClause = 1, RULE_declaration = 2, RULE_identifierList = 3, 
		RULE_expressionList = 4, RULE_functionDecl = 5, RULE_signature = 6, RULE_parameters = 7, 
		RULE_parameterDecl = 8, RULE_drawClause = 9, RULE_shapeDecl = 10, RULE_shapeSpec = 11, 
		RULE_block = 12, RULE_statementList = 13, RULE_statement = 14, RULE_simpleStmt = 15, 
		RULE_expressionStmt = 16, RULE_shapeArguments = 17, RULE_assignment = 18, 
		RULE_assign_op = 19, RULE_ifStmt = 20, RULE_switchStmt = 21, RULE_exprSwitchStmt = 22, 
		RULE_exprCaseClause = 23, RULE_exprSwitchCase = 24, RULE_type_ = 25, RULE_typeName = 26, 
		RULE_elementType = 27, RULE_expression = 28, RULE_primaryExpr = 29, RULE_operand = 30, 
		RULE_literal = 31, RULE_basicLit = 32, RULE_integer = 33, RULE_operandName = 34, 
		RULE_compositeLit = 35, RULE_literalType = 36, RULE_literalValue = 37, 
		RULE_element = 38, RULE_string_ = 39, RULE_arguments = 40, RULE_eos = 41;
	private static String[] makeRuleNames() {
		return new String[] {
			"sourceFile", "viewportClause", "declaration", "identifierList", "expressionList", 
			"functionDecl", "signature", "parameters", "parameterDecl", "drawClause", 
			"shapeDecl", "shapeSpec", "block", "statementList", "statement", "simpleStmt", 
			"expressionStmt", "shapeArguments", "assignment", "assign_op", "ifStmt", 
			"switchStmt", "exprSwitchStmt", "exprCaseClause", "exprSwitchCase", "type_", 
			"typeName", "elementType", "expression", "primaryExpr", "operand", "literal", 
			"basicLit", "integer", "operandName", "compositeLit", "literalType", 
			"literalValue", "element", "string_", "arguments", "eos"
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

	@Override
	public String getGrammarFileName() { return "TwoDimParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TwoDimParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class SourceFileContext extends ParserRuleContext {
		public DrawClauseContext drawClause() {
			return getRuleContext(DrawClauseContext.class,0);
		}
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
		}
		public ViewportClauseContext viewportClause() {
			return getRuleContext(ViewportClauseContext.class,0);
		}
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public List<FunctionDeclContext> functionDecl() {
			return getRuleContexts(FunctionDeclContext.class);
		}
		public FunctionDeclContext functionDecl(int i) {
			return getRuleContext(FunctionDeclContext.class,i);
		}
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public SourceFileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sourceFile; }
	}

	public final SourceFileContext sourceFile() throws RecognitionException {
		SourceFileContext _localctx = new SourceFileContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_sourceFile);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VIEWPORT) {
				{
				setState(84);
				viewportClause();
				}
			}

			setState(95);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(89);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case FUNC:
						{
						setState(87);
						functionDecl();
						}
						break;
					case SQUARE:
					case RECT:
					case CIRCLE:
					case TRIANGLE:
					case SHAPE:
						{
						setState(88);
						declaration();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(91);
					eos();
					}
					} 
				}
				setState(97);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(98);
				statementList();
				}
			}

			setState(101);
			drawClause();
			setState(102);
			eos();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ViewportClauseContext extends ParserRuleContext {
		public TerminalNode VIEWPORT() { return getToken(TwoDimParser.VIEWPORT, 0); }
		public List<TerminalNode> WS() { return getTokens(TwoDimParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(TwoDimParser.WS, i);
		}
		public List<TerminalNode> DECIMAL_LIT() { return getTokens(TwoDimParser.DECIMAL_LIT); }
		public TerminalNode DECIMAL_LIT(int i) {
			return getToken(TwoDimParser.DECIMAL_LIT, i);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public ViewportClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_viewportClause; }
	}

	public final ViewportClauseContext viewportClause() throws RecognitionException {
		ViewportClauseContext _localctx = new ViewportClauseContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_viewportClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(VIEWPORT);
			setState(105);
			match(WS);
			setState(106);
			match(DECIMAL_LIT);
			setState(107);
			match(WS);
			setState(108);
			match(DECIMAL_LIT);
			setState(109);
			eos();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public ShapeDeclContext shapeDecl() {
			return getRuleContext(ShapeDeclContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			shapeDecl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierListContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(TwoDimParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(TwoDimParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public IdentifierListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierList; }
	}

	public final IdentifierListContext identifierList() throws RecognitionException {
		IdentifierListContext _localctx = new IdentifierListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_identifierList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(IDENTIFIER);
			setState(118);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(114);
					match(COMMA);
					setState(115);
					match(IDENTIFIER);
					}
					} 
				}
				setState(120);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public ExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionList; }
	}

	public final ExpressionListContext expressionList() throws RecognitionException {
		ExpressionListContext _localctx = new ExpressionListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_expressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			expression();
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(122);
				match(COMMA);
				setState(123);
				expression();
				}
				}
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDeclContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(TwoDimParser.FUNC, 0); }
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_functionDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(FUNC);
			setState(130);
			match(IDENTIFIER);
			{
			setState(131);
			signature();
			setState(133);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(132);
				block();
				}
				break;
			}
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SignatureContext extends ParserRuleContext {
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public SignatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signature; }
	}

	public final SignatureContext signature() throws RecognitionException {
		SignatureContext _localctx = new SignatureContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_signature);
		try {
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				if (!(self.noTerminatorAfterParams(1))) throw new FailedPredicateException(this, "self.noTerminatorAfterParams(1)");
				setState(136);
				parameters();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(137);
				parameters();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParametersContext extends ParserRuleContext {
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public List<ParameterDeclContext> parameterDecl() {
			return getRuleContexts(ParameterDeclContext.class);
		}
		public ParameterDeclContext parameterDecl(int i) {
			return getRuleContext(ParameterDeclContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			match(L_PAREN);
			setState(149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SQUARE) | (1L << RECT) | (1L << CIRCLE) | (1L << TRIANGLE) | (1L << SHAPE))) != 0)) {
				{
				setState(141);
				parameterDecl();
				setState(146);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(142);
					match(COMMA);
					setState(143);
					parameterDecl();
					}
					}
					setState(148);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(151);
			match(R_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterDeclContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public ParameterDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterDecl; }
	}

	public final ParameterDeclContext parameterDecl() throws RecognitionException {
		ParameterDeclContext _localctx = new ParameterDeclContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameterDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			type_();
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(154);
				identifierList();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DrawClauseContext extends ParserRuleContext {
		public TerminalNode DRAW() { return getToken(TwoDimParser.DRAW, 0); }
		public TerminalNode WS() { return getToken(TwoDimParser.WS, 0); }
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public DrawClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_drawClause; }
	}

	public final DrawClauseContext drawClause() throws RecognitionException {
		DrawClauseContext _localctx = new DrawClauseContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_drawClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(DRAW);
			setState(158);
			match(WS);
			setState(159);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShapeDeclContext extends ParserRuleContext {
		public ShapeSpecContext shapeSpec() {
			return getRuleContext(ShapeSpecContext.class,0);
		}
		public ShapeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeDecl; }
	}

	public final ShapeDeclContext shapeDecl() throws RecognitionException {
		ShapeDeclContext _localctx = new ShapeDeclContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_shapeDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			shapeSpec();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShapeSpecContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(TwoDimParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(TwoDimParser.WS, i);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(TwoDimParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(TwoDimParser.IDENTIFIER, i);
		}
		public List<ShapeArgumentsContext> shapeArguments() {
			return getRuleContexts(ShapeArgumentsContext.class);
		}
		public ShapeArgumentsContext shapeArguments(int i) {
			return getRuleContext(ShapeArgumentsContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public ShapeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeSpec; }
	}

	public final ShapeSpecContext shapeSpec() throws RecognitionException {
		ShapeSpecContext _localctx = new ShapeSpecContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_shapeSpec);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			type_();
			setState(164);
			match(WS);
			setState(165);
			match(IDENTIFIER);
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(166);
				match(WS);
				}
				break;
			}
			setState(169);
			shapeArguments();
			setState(178);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(170);
					match(COMMA);
					setState(172);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(171);
						match(WS);
						}
					}

					setState(174);
					match(IDENTIFIER);
					setState(175);
					shapeArguments();
					}
					} 
				}
				setState(180);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode L_CURLY() { return getToken(TwoDimParser.L_CURLY, 0); }
		public TerminalNode R_CURLY() { return getToken(TwoDimParser.R_CURLY, 0); }
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(L_CURLY);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(182);
				statementList();
				}
			}

			setState(185);
			match(R_CURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementListContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
		}
		public StatementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementList; }
	}

	public final StatementListContext statementList() throws RecognitionException {
		StatementListContext _localctx = new StatementListContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_statementList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(187);
				statement();
				setState(188);
				eos();
				}
				}
				setState(192); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( ((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public SwitchStmtContext switchStmt() {
			return getRuleContext(SwitchStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_statement);
		try {
			setState(199);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(194);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(195);
				simpleStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(196);
				block();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(197);
				ifStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(198);
				switchStmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SimpleStmtContext extends ParserRuleContext {
		public ExpressionStmtContext expressionStmt() {
			return getRuleContext(ExpressionStmtContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public SimpleStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStmt; }
	}

	public final SimpleStmtContext simpleStmt() throws RecognitionException {
		SimpleStmtContext _localctx = new SimpleStmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_simpleStmt);
		try {
			setState(203);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(201);
				expressionStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(202);
				assignment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionStmtContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionStmt; }
	}

	public final ExpressionStmtContext expressionStmt() throws RecognitionException {
		ExpressionStmtContext _localctx = new ExpressionStmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expressionStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShapeArgumentsContext extends ParserRuleContext {
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(TwoDimParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(TwoDimParser.WS, i);
		}
		public TerminalNode L_BRACKET() { return getToken(TwoDimParser.L_BRACKET, 0); }
		public List<TerminalNode> SIZE_LIT() { return getTokens(TwoDimParser.SIZE_LIT); }
		public TerminalNode SIZE_LIT(int i) {
			return getToken(TwoDimParser.SIZE_LIT, i);
		}
		public TerminalNode R_BRACKET() { return getToken(TwoDimParser.R_BRACKET, 0); }
		public TerminalNode COMMA() { return getToken(TwoDimParser.COMMA, 0); }
		public ShapeArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeArguments; }
	}

	public final ShapeArgumentsContext shapeArguments() throws RecognitionException {
		ShapeArgumentsContext _localctx = new ShapeArgumentsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_shapeArguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(207);
				arguments();
				}
				break;
			}
			setState(211);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(210);
				match(WS);
				}
				break;
			}
			setState(229);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(213);
				match(L_BRACKET);
				setState(215);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(214);
					match(WS);
					}
				}

				setState(217);
				match(SIZE_LIT);
				setState(223);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(218);
					match(COMMA);
					setState(220);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(219);
						match(WS);
						}
					}

					setState(222);
					match(SIZE_LIT);
					}
				}

				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(225);
					match(WS);
					}
				}

				setState(228);
				match(R_BRACKET);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(IDENTIFIER);
			setState(232);
			assign_op();
			setState(233);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_opContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(TwoDimParser.ASSIGN, 0); }
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_assign_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(ASSIGN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(TwoDimParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(TwoDimParser.SEMI, 0); }
		public TerminalNode ELSE() { return getToken(TwoDimParser.ELSE, 0); }
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_ifStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(IF);
			setState(241);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(238);
				simpleStmt();
				setState(239);
				match(SEMI);
				}
				break;
			}
			setState(243);
			expression();
			setState(244);
			block();
			setState(250);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(245);
				match(ELSE);
				setState(248);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF:
					{
					setState(246);
					ifStmt();
					}
					break;
				case L_CURLY:
					{
					setState(247);
					block();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SwitchStmtContext extends ParserRuleContext {
		public ExprSwitchStmtContext exprSwitchStmt() {
			return getRuleContext(ExprSwitchStmtContext.class,0);
		}
		public SwitchStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStmt; }
	}

	public final SwitchStmtContext switchStmt() throws RecognitionException {
		SwitchStmtContext _localctx = new SwitchStmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_switchStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			exprSwitchStmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprSwitchStmtContext extends ParserRuleContext {
		public TerminalNode SWITCH() { return getToken(TwoDimParser.SWITCH, 0); }
		public TerminalNode L_CURLY() { return getToken(TwoDimParser.L_CURLY, 0); }
		public TerminalNode R_CURLY() { return getToken(TwoDimParser.R_CURLY, 0); }
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(TwoDimParser.SEMI, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<ExprCaseClauseContext> exprCaseClause() {
			return getRuleContexts(ExprCaseClauseContext.class);
		}
		public ExprCaseClauseContext exprCaseClause(int i) {
			return getRuleContext(ExprCaseClauseContext.class,i);
		}
		public ExprSwitchStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprSwitchStmt; }
	}

	public final ExprSwitchStmtContext exprSwitchStmt() throws RecognitionException {
		ExprSwitchStmtContext _localctx = new ExprSwitchStmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_exprSwitchStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(SWITCH);
			setState(258);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				setState(255);
				simpleStmt();
				setState(256);
				match(SEMI);
				}
				break;
			}
			setState(261);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (SQUARE - 10)) | (1L << (RECT - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)) | (1L << (L_PAREN - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(260);
				expression();
				}
			}

			setState(263);
			match(L_CURLY);
			setState(267);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(264);
				exprCaseClause();
				}
				}
				setState(269);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(270);
			match(R_CURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprCaseClauseContext extends ParserRuleContext {
		public ExprSwitchCaseContext exprSwitchCase() {
			return getRuleContext(ExprSwitchCaseContext.class,0);
		}
		public TerminalNode COLON() { return getToken(TwoDimParser.COLON, 0); }
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public ExprCaseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprCaseClause; }
	}

	public final ExprCaseClauseContext exprCaseClause() throws RecognitionException {
		ExprCaseClauseContext _localctx = new ExprCaseClauseContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_exprCaseClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			exprSwitchCase();
			setState(273);
			match(COLON);
			setState(275);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(274);
				statementList();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprSwitchCaseContext extends ParserRuleContext {
		public TerminalNode CASE() { return getToken(TwoDimParser.CASE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DEFAULT() { return getToken(TwoDimParser.DEFAULT, 0); }
		public ExprSwitchCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprSwitchCase; }
	}

	public final ExprSwitchCaseContext exprSwitchCase() throws RecognitionException {
		ExprSwitchCaseContext _localctx = new ExprSwitchCaseContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_exprSwitchCase);
		try {
			setState(280);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(277);
				match(CASE);
				setState(278);
				expression();
				}
				break;
			case DEFAULT:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
				match(DEFAULT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Type_Context extends ParserRuleContext {
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public Type_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_; }
	}

	public final Type_Context type_() throws RecognitionException {
		Type_Context _localctx = new Type_Context(_ctx, getState());
		enterRule(_localctx, 50, RULE_type_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			typeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeNameContext extends ParserRuleContext {
		public TerminalNode RECT() { return getToken(TwoDimParser.RECT, 0); }
		public TerminalNode SQUARE() { return getToken(TwoDimParser.SQUARE, 0); }
		public TerminalNode CIRCLE() { return getToken(TwoDimParser.CIRCLE, 0); }
		public TerminalNode TRIANGLE() { return getToken(TwoDimParser.TRIANGLE, 0); }
		public TerminalNode SHAPE() { return getToken(TwoDimParser.SHAPE, 0); }
		public TypeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeName; }
	}

	public final TypeNameContext typeName() throws RecognitionException {
		TypeNameContext _localctx = new TypeNameContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_typeName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SQUARE) | (1L << RECT) | (1L << CIRCLE) | (1L << TRIANGLE) | (1L << SHAPE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementTypeContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public ElementTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementType; }
	}

	public final ElementTypeContext elementType() throws RecognitionException {
		ElementTypeContext _localctx = new ElementTypeContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_elementType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			type_();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public List<PrimaryExprContext> primaryExpr() {
			return getRuleContexts(PrimaryExprContext.class);
		}
		public PrimaryExprContext primaryExpr(int i) {
			return getRuleContext(PrimaryExprContext.class,i);
		}
		public TerminalNode LEFT() { return getToken(TwoDimParser.LEFT, 0); }
		public TerminalNode RIGHT() { return getToken(TwoDimParser.RIGHT, 0); }
		public TerminalNode TOP() { return getToken(TwoDimParser.TOP, 0); }
		public TerminalNode BOT() { return getToken(TwoDimParser.BOT, 0); }
		public TerminalNode INNER() { return getToken(TwoDimParser.INNER, 0); }
		public TerminalNode OUTER() { return getToken(TwoDimParser.OUTER, 0); }
		public TerminalNode IN() { return getToken(TwoDimParser.IN, 0); }
		public TerminalNode ON() { return getToken(TwoDimParser.ON, 0); }
		public TerminalNode UNDER() { return getToken(TwoDimParser.UNDER, 0); }
		public TerminalNode PLUS() { return getToken(TwoDimParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(TwoDimParser.MINUS, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_expression);
		int _la;
		try {
			setState(304);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(288);
				primaryExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(289);
				primaryExpr();
				setState(290);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFT) | (1L << RIGHT) | (1L << TOP) | (1L << BOT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(292);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OUTER || _la==INNER) {
					{
					setState(291);
					_la = _input.LA(1);
					if ( !(_la==OUTER || _la==INNER) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(294);
				primaryExpr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(296);
				primaryExpr();
				setState(297);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ON) | (1L << UNDER) | (1L << IN))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(298);
				primaryExpr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(300);
				primaryExpr();
				setState(301);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(302);
				primaryExpr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryExprContext extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public PrimaryExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpr; }
	}

	public final PrimaryExprContext primaryExpr() throws RecognitionException {
		PrimaryExprContext _localctx = new PrimaryExprContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_primaryExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			operand();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperandContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public OperandNameContext operandName() {
			return getRuleContext(OperandNameContext.class,0);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_operand);
		try {
			setState(314);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NIL_LIT:
			case SQUARE:
			case RECT:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(308);
				literal();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(309);
				operandName();
				}
				break;
			case L_PAREN:
				enterOuterAlt(_localctx, 3);
				{
				setState(310);
				match(L_PAREN);
				setState(311);
				expression();
				setState(312);
				match(R_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public BasicLitContext basicLit() {
			return getRuleContext(BasicLitContext.class,0);
		}
		public CompositeLitContext compositeLit() {
			return getRuleContext(CompositeLitContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_literal);
		try {
			setState(318);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NIL_LIT:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(316);
				basicLit();
				}
				break;
			case SQUARE:
			case RECT:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(317);
				compositeLit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BasicLitContext extends ParserRuleContext {
		public TerminalNode NIL_LIT() { return getToken(TwoDimParser.NIL_LIT, 0); }
		public IntegerContext integer() {
			return getRuleContext(IntegerContext.class,0);
		}
		public String_Context string_() {
			return getRuleContext(String_Context.class,0);
		}
		public TerminalNode FLOAT_LIT() { return getToken(TwoDimParser.FLOAT_LIT, 0); }
		public TerminalNode RUNE_LIT() { return getToken(TwoDimParser.RUNE_LIT, 0); }
		public BasicLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_basicLit; }
	}

	public final BasicLitContext basicLit() throws RecognitionException {
		BasicLitContext _localctx = new BasicLitContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_basicLit);
		try {
			setState(325);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(320);
				match(NIL_LIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(321);
				integer();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(322);
				string_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(323);
				match(FLOAT_LIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(324);
				match(RUNE_LIT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntegerContext extends ParserRuleContext {
		public TerminalNode DECIMAL_LIT() { return getToken(TwoDimParser.DECIMAL_LIT, 0); }
		public TerminalNode RUNE_LIT() { return getToken(TwoDimParser.RUNE_LIT, 0); }
		public IntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integer; }
	}

	public final IntegerContext integer() throws RecognitionException {
		IntegerContext _localctx = new IntegerContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			_la = _input.LA(1);
			if ( !(_la==DECIMAL_LIT || _la==RUNE_LIT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperandNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public OperandNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operandName; }
	}

	public final OperandNameContext operandName() throws RecognitionException {
		OperandNameContext _localctx = new OperandNameContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_operandName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompositeLitContext extends ParserRuleContext {
		public LiteralTypeContext literalType() {
			return getRuleContext(LiteralTypeContext.class,0);
		}
		public LiteralValueContext literalValue() {
			return getRuleContext(LiteralValueContext.class,0);
		}
		public CompositeLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compositeLit; }
	}

	public final CompositeLitContext compositeLit() throws RecognitionException {
		CompositeLitContext _localctx = new CompositeLitContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_compositeLit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(331);
			literalType();
			setState(332);
			literalValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralTypeContext extends ParserRuleContext {
		public ElementTypeContext elementType() {
			return getRuleContext(ElementTypeContext.class,0);
		}
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public LiteralTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalType; }
	}

	public final LiteralTypeContext literalType() throws RecognitionException {
		LiteralTypeContext _localctx = new LiteralTypeContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_literalType);
		try {
			setState(336);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(334);
				elementType();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(335);
				typeName();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralValueContext extends ParserRuleContext {
		public TerminalNode L_CURLY() { return getToken(TwoDimParser.L_CURLY, 0); }
		public TerminalNode R_CURLY() { return getToken(TwoDimParser.R_CURLY, 0); }
		public ElementContext element() {
			return getRuleContext(ElementContext.class,0);
		}
		public LiteralValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalValue; }
	}

	public final LiteralValueContext literalValue() throws RecognitionException {
		LiteralValueContext _localctx = new LiteralValueContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_literalValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(338);
			match(L_CURLY);
			setState(340);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (SQUARE - 10)) | (1L << (RECT - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)) | (1L << (L_PAREN - 10)) | (1L << (L_CURLY - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(339);
				element();
				}
			}

			setState(342);
			match(R_CURLY);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LiteralValueContext literalValue() {
			return getRuleContext(LiteralValueContext.class,0);
		}
		public ElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element; }
	}

	public final ElementContext element() throws RecognitionException {
		ElementContext _localctx = new ElementContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_element);
		try {
			setState(346);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NIL_LIT:
			case IDENTIFIER:
			case SQUARE:
			case RECT:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
			case L_PAREN:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(344);
				expression();
				}
				break;
			case L_CURLY:
				enterOuterAlt(_localctx, 2);
				{
				setState(345);
				literalValue();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class String_Context extends ParserRuleContext {
		public TerminalNode RAW_STRING_LIT() { return getToken(TwoDimParser.RAW_STRING_LIT, 0); }
		public TerminalNode INTERPRETED_STRING_LIT() { return getToken(TwoDimParser.INTERPRETED_STRING_LIT, 0); }
		public String_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_; }
	}

	public final String_Context string_() throws RecognitionException {
		String_Context _localctx = new String_Context(_ctx, getState());
		enterRule(_localctx, 78, RULE_string_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			_la = _input.LA(1);
			if ( !(_la==RAW_STRING_LIT || _la==INTERPRETED_STRING_LIT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentsContext extends ParserRuleContext {
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			match(L_PAREN);
			setState(352);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (SQUARE - 10)) | (1L << (RECT - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)) | (1L << (L_PAREN - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(351);
				expressionList();
				}
			}

			setState(354);
			match(R_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EosContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(TwoDimParser.SEMI, 0); }
		public TerminalNode EOF() { return getToken(TwoDimParser.EOF, 0); }
		public EosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eos; }
	}

	public final EosContext eos() throws RecognitionException {
		EosContext _localctx = new EosContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_eos);
		try {
			setState(361);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(356);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(357);
				match(SEMI);
				setState(358);
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(359);
				if (!(self.lineTerminatorAhead())) throw new FailedPredicateException(this, "self.lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(360);
				if (!(self.checkPreviousTokenText("}"))) throw new FailedPredicateException(this, "self.checkPreviousTokenText(\"}\")");
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return signature_sempred((SignatureContext)_localctx, predIndex);
		case 41:
			return eos_sempred((EosContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean signature_sempred(SignatureContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return self.noTerminatorAfterParams(1);
		}
		return true;
	}
	private boolean eos_sempred(EosContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return self.lineTerminatorAhead();
		case 2:
			return self.checkPreviousTokenText("}");
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H\u016e\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\5\2X\n\2\3\2\3\2\5\2\\\n\2\3\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\5\2"+
		"f\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5"+
		"w\n\5\f\5\16\5z\13\5\3\6\3\6\3\6\7\6\177\n\6\f\6\16\6\u0082\13\6\3\7\3"+
		"\7\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\5\b\u008d\n\b\3\t\3\t\3\t\3\t\7\t"+
		"\u0093\n\t\f\t\16\t\u0096\13\t\5\t\u0098\n\t\3\t\3\t\3\n\3\n\5\n\u009e"+
		"\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00aa\n\r\3\r\3\r"+
		"\3\r\5\r\u00af\n\r\3\r\3\r\7\r\u00b3\n\r\f\r\16\r\u00b6\13\r\3\16\3\16"+
		"\5\16\u00ba\n\16\3\16\3\16\3\17\3\17\3\17\6\17\u00c1\n\17\r\17\16\17\u00c2"+
		"\3\20\3\20\3\20\3\20\3\20\5\20\u00ca\n\20\3\21\3\21\5\21\u00ce\n\21\3"+
		"\22\3\22\3\23\5\23\u00d3\n\23\3\23\5\23\u00d6\n\23\3\23\3\23\5\23\u00da"+
		"\n\23\3\23\3\23\3\23\5\23\u00df\n\23\3\23\5\23\u00e2\n\23\3\23\5\23\u00e5"+
		"\n\23\3\23\5\23\u00e8\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26"+
		"\3\26\5\26\u00f4\n\26\3\26\3\26\3\26\3\26\3\26\5\26\u00fb\n\26\5\26\u00fd"+
		"\n\26\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0105\n\30\3\30\5\30\u0108\n"+
		"\30\3\30\3\30\7\30\u010c\n\30\f\30\16\30\u010f\13\30\3\30\3\30\3\31\3"+
		"\31\3\31\5\31\u0116\n\31\3\32\3\32\3\32\5\32\u011b\n\32\3\33\3\33\3\34"+
		"\3\34\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u0127\n\36\3\36\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0133\n\36\3\37\3\37\3 \3 \3 \3 \3"+
		" \3 \5 \u013d\n \3!\3!\5!\u0141\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0148\n\"\3"+
		"#\3#\3$\3$\3%\3%\3%\3&\3&\5&\u0153\n&\3\'\3\'\5\'\u0157\n\'\3\'\3\'\3"+
		"(\3(\5(\u015d\n(\3)\3)\3*\3*\5*\u0163\n*\3*\3*\3+\3+\3+\3+\3+\5+\u016c"+
		"\n+\3+\2\2,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66"+
		"8:<>@BDFHJLNPRT\2\t\3\2\16\22\3\2\25\30\3\2\31\32\3\2\33\35\3\2:;\4\2"+
		"??AA\3\2BC\2\u0179\2W\3\2\2\2\4j\3\2\2\2\6q\3\2\2\2\bs\3\2\2\2\n{\3\2"+
		"\2\2\f\u0083\3\2\2\2\16\u008c\3\2\2\2\20\u008e\3\2\2\2\22\u009b\3\2\2"+
		"\2\24\u009f\3\2\2\2\26\u00a3\3\2\2\2\30\u00a5\3\2\2\2\32\u00b7\3\2\2\2"+
		"\34\u00c0\3\2\2\2\36\u00c9\3\2\2\2 \u00cd\3\2\2\2\"\u00cf\3\2\2\2$\u00d2"+
		"\3\2\2\2&\u00e9\3\2\2\2(\u00ed\3\2\2\2*\u00ef\3\2\2\2,\u00fe\3\2\2\2."+
		"\u0100\3\2\2\2\60\u0112\3\2\2\2\62\u011a\3\2\2\2\64\u011c\3\2\2\2\66\u011e"+
		"\3\2\2\28\u0120\3\2\2\2:\u0132\3\2\2\2<\u0134\3\2\2\2>\u013c\3\2\2\2@"+
		"\u0140\3\2\2\2B\u0147\3\2\2\2D\u0149\3\2\2\2F\u014b\3\2\2\2H\u014d\3\2"+
		"\2\2J\u0152\3\2\2\2L\u0154\3\2\2\2N\u015c\3\2\2\2P\u015e\3\2\2\2R\u0160"+
		"\3\2\2\2T\u016b\3\2\2\2VX\5\4\3\2WV\3\2\2\2WX\3\2\2\2Xa\3\2\2\2Y\\\5\f"+
		"\7\2Z\\\5\6\4\2[Y\3\2\2\2[Z\3\2\2\2\\]\3\2\2\2]^\5T+\2^`\3\2\2\2_[\3\2"+
		"\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2be\3\2\2\2ca\3\2\2\2df\5\34\17\2ed\3"+
		"\2\2\2ef\3\2\2\2fg\3\2\2\2gh\5\24\13\2hi\5T+\2i\3\3\2\2\2jk\7\24\2\2k"+
		"l\7E\2\2lm\7?\2\2mn\7E\2\2no\7?\2\2op\5T+\2p\5\3\2\2\2qr\5\26\f\2r\7\3"+
		"\2\2\2sx\7\r\2\2tu\7%\2\2uw\7\r\2\2vt\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3"+
		"\2\2\2y\t\3\2\2\2zx\3\2\2\2{\u0080\5:\36\2|}\7%\2\2}\177\5:\36\2~|\3\2"+
		"\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\13\3\2"+
		"\2\2\u0082\u0080\3\2\2\2\u0083\u0084\7\3\2\2\u0084\u0085\7\r\2\2\u0085"+
		"\u0087\5\16\b\2\u0086\u0088\5\32\16\2\u0087\u0086\3\2\2\2\u0087\u0088"+
		"\3\2\2\2\u0088\r\3\2\2\2\u0089\u008a\6\b\2\2\u008a\u008d\5\20\t\2\u008b"+
		"\u008d\5\20\t\2\u008c\u0089\3\2\2\2\u008c\u008b\3\2\2\2\u008d\17\3\2\2"+
		"\2\u008e\u0097\7\36\2\2\u008f\u0094\5\22\n\2\u0090\u0091\7%\2\2\u0091"+
		"\u0093\5\22\n\2\u0092\u0090\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3"+
		"\2\2\2\u0094\u0095\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0097"+
		"\u008f\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\7\37"+
		"\2\2\u009a\21\3\2\2\2\u009b\u009d\5\64\33\2\u009c\u009e\5\b\5\2\u009d"+
		"\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\23\3\2\2\2\u009f\u00a0\7\23\2"+
		"\2\u00a0\u00a1\7E\2\2\u00a1\u00a2\7\r\2\2\u00a2\25\3\2\2\2\u00a3\u00a4"+
		"\5\30\r\2\u00a4\27\3\2\2\2\u00a5\u00a6\5\64\33\2\u00a6\u00a7\7E\2\2\u00a7"+
		"\u00a9\7\r\2\2\u00a8\u00aa\7E\2\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2"+
		"\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00b4\5$\23\2\u00ac\u00ae\7%\2\2\u00ad"+
		"\u00af\7E\2\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2"+
		"\2\2\u00b0\u00b1\7\r\2\2\u00b1\u00b3\5$\23\2\u00b2\u00ac\3\2\2\2\u00b3"+
		"\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\31\3\2\2"+
		"\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9\7 \2\2\u00b8\u00ba\5\34\17\2\u00b9"+
		"\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7!"+
		"\2\2\u00bc\33\3\2\2\2\u00bd\u00be\5\36\20\2\u00be\u00bf\5T+\2\u00bf\u00c1"+
		"\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2"+
		"\u00c3\3\2\2\2\u00c3\35\3\2\2\2\u00c4\u00ca\5\6\4\2\u00c5\u00ca\5 \21"+
		"\2\u00c6\u00ca\5\32\16\2\u00c7\u00ca\5*\26\2\u00c8\u00ca\5,\27\2\u00c9"+
		"\u00c4\3\2\2\2\u00c9\u00c5\3\2\2\2\u00c9\u00c6\3\2\2\2\u00c9\u00c7\3\2"+
		"\2\2\u00c9\u00c8\3\2\2\2\u00ca\37\3\2\2\2\u00cb\u00ce\5\"\22\2\u00cc\u00ce"+
		"\5&\24\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce!\3\2\2\2\u00cf"+
		"\u00d0\5:\36\2\u00d0#\3\2\2\2\u00d1\u00d3\5R*\2\u00d2\u00d1\3\2\2\2\u00d2"+
		"\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d6\7E\2\2\u00d5\u00d4\3\2"+
		"\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00e7\3\2\2\2\u00d7\u00d9\7\"\2\2\u00d8"+
		"\u00da\7E\2\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2"+
		"\2\2\u00db\u00e1\7D\2\2\u00dc\u00de\7%\2\2\u00dd\u00df\7E\2\2\u00de\u00dd"+
		"\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\7D\2\2\u00e1"+
		"\u00dc\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e5\7E"+
		"\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6"+
		"\u00e8\7#\2\2\u00e7\u00d7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8%\3\2\2\2\u00e9"+
		"\u00ea\7\r\2\2\u00ea\u00eb\5(\25\2\u00eb\u00ec\5:\36\2\u00ec\'\3\2\2\2"+
		"\u00ed\u00ee\7$\2\2\u00ee)\3\2\2\2\u00ef\u00f3\7\7\2\2\u00f0\u00f1\5 "+
		"\21\2\u00f1\u00f2\7&\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f0\3\2\2\2\u00f3"+
		"\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\5:\36\2\u00f6\u00fc\5\32"+
		"\16\2\u00f7\u00fa\7\b\2\2\u00f8\u00fb\5*\26\2\u00f9\u00fb\5\32\16\2\u00fa"+
		"\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00f7\3\2"+
		"\2\2\u00fc\u00fd\3\2\2\2\u00fd+\3\2\2\2\u00fe\u00ff\5.\30\2\u00ff-\3\2"+
		"\2\2\u0100\u0104\7\4\2\2\u0101\u0102\5 \21\2\u0102\u0103\7&\2\2\u0103"+
		"\u0105\3\2\2\2\u0104\u0101\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0107\3\2"+
		"\2\2\u0106\u0108\5:\36\2\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108"+
		"\u0109\3\2\2\2\u0109\u010d\7 \2\2\u010a\u010c\5\60\31\2\u010b\u010a\3"+
		"\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e"+
		"\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\7!\2\2\u0111/\3\2\2\2\u0112"+
		"\u0113\5\62\32\2\u0113\u0115\7\'\2\2\u0114\u0116\5\34\17\2\u0115\u0114"+
		"\3\2\2\2\u0115\u0116\3\2\2\2\u0116\61\3\2\2\2\u0117\u0118\7\5\2\2\u0118"+
		"\u011b\5:\36\2\u0119\u011b\7\6\2\2\u011a\u0117\3\2\2\2\u011a\u0119\3\2"+
		"\2\2\u011b\63\3\2\2\2\u011c\u011d\5\66\34\2\u011d\65\3\2\2\2\u011e\u011f"+
		"\t\2\2\2\u011f\67\3\2\2\2\u0120\u0121\5\64\33\2\u01219\3\2\2\2\u0122\u0133"+
		"\5<\37\2\u0123\u0124\5<\37\2\u0124\u0126\t\3\2\2\u0125\u0127\t\4\2\2\u0126"+
		"\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\5<"+
		"\37\2\u0129\u0133\3\2\2\2\u012a\u012b\5<\37\2\u012b\u012c\t\5\2\2\u012c"+
		"\u012d\5<\37\2\u012d\u0133\3\2\2\2\u012e\u012f\5<\37\2\u012f\u0130\t\6"+
		"\2\2\u0130\u0131\5<\37\2\u0131\u0133\3\2\2\2\u0132\u0122\3\2\2\2\u0132"+
		"\u0123\3\2\2\2\u0132\u012a\3\2\2\2\u0132\u012e\3\2\2\2\u0133;\3\2\2\2"+
		"\u0134\u0135\5> \2\u0135=\3\2\2\2\u0136\u013d\5@!\2\u0137\u013d\5F$\2"+
		"\u0138\u0139\7\36\2\2\u0139\u013a\5:\36\2\u013a\u013b\7\37\2\2\u013b\u013d"+
		"\3\2\2\2\u013c\u0136\3\2\2\2\u013c\u0137\3\2\2\2\u013c\u0138\3\2\2\2\u013d"+
		"?\3\2\2\2\u013e\u0141\5B\"\2\u013f\u0141\5H%\2\u0140\u013e\3\2\2\2\u0140"+
		"\u013f\3\2\2\2\u0141A\3\2\2\2\u0142\u0148\7\f\2\2\u0143\u0148\5D#\2\u0144"+
		"\u0148\5P)\2\u0145\u0148\7@\2\2\u0146\u0148\7A\2\2\u0147\u0142\3\2\2\2"+
		"\u0147\u0143\3\2\2\2\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146"+
		"\3\2\2\2\u0148C\3\2\2\2\u0149\u014a\t\7\2\2\u014aE\3\2\2\2\u014b\u014c"+
		"\7\r\2\2\u014cG\3\2\2\2\u014d\u014e\5J&\2\u014e\u014f\5L\'\2\u014fI\3"+
		"\2\2\2\u0150\u0153\58\35\2\u0151\u0153\5\66\34\2\u0152\u0150\3\2\2\2\u0152"+
		"\u0151\3\2\2\2\u0153K\3\2\2\2\u0154\u0156\7 \2\2\u0155\u0157\5N(\2\u0156"+
		"\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\7!"+
		"\2\2\u0159M\3\2\2\2\u015a\u015d\5:\36\2\u015b\u015d\5L\'\2\u015c\u015a"+
		"\3\2\2\2\u015c\u015b\3\2\2\2\u015dO\3\2\2\2\u015e\u015f\t\b\2\2\u015f"+
		"Q\3\2\2\2\u0160\u0162\7\36\2\2\u0161\u0163\5\n\6\2\u0162\u0161\3\2\2\2"+
		"\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7\37\2\2\u0165S\3"+
		"\2\2\2\u0166\u016c\7&\2\2\u0167\u0168\7&\2\2\u0168\u016c\7\2\2\3\u0169"+
		"\u016c\6+\3\2\u016a\u016c\6+\4\2\u016b\u0166\3\2\2\2\u016b\u0167\3\2\2"+
		"\2\u016b\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016cU\3\2\2\2-W[aex\u0080"+
		"\u0087\u008c\u0094\u0097\u009d\u00a9\u00ae\u00b4\u00b9\u00c2\u00c9\u00cd"+
		"\u00d2\u00d5\u00d9\u00de\u00e1\u00e4\u00e7\u00f3\u00fa\u00fc\u0104\u0107"+
		"\u010d\u0115\u011a\u0126\u0132\u013c\u0140\u0147\u0152\u0156\u015c\u0162"+
		"\u016b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}