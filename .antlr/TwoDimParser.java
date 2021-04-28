// Generated from /home/liza/TKK/projekt/Language-for-2D-graphics/TwoDimParser.g4 by ANTLR 4.8
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
		RULE_exprCaseClause = 23, RULE_exprSwitchCase = 24, RULE_typeName = 25, 
		RULE_expression = 26, RULE_primaryExpr = 27, RULE_operand = 28, RULE_literal = 29, 
		RULE_basicLit = 30, RULE_integer = 31, RULE_operandName = 32, RULE_string_ = 33, 
		RULE_arguments = 34, RULE_eos = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"sourceFile", "viewportClause", "declaration", "identifierList", "expressionList", 
			"functionDecl", "signature", "parameters", "parameterDecl", "drawClause", 
			"shapeDecl", "shapeSpec", "block", "statementList", "statement", "simpleStmt", 
			"expressionStmt", "shapeArguments", "assignment", "assign_op", "ifStmt", 
			"switchStmt", "exprSwitchStmt", "exprCaseClause", "exprSwitchCase", "typeName", 
			"expression", "primaryExpr", "operand", "literal", "basicLit", "integer", 
			"operandName", "string_", "arguments", "eos"
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
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VIEWPORT) {
				{
				setState(72);
				viewportClause();
				}
			}

			setState(83);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(77);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case FUNC:
						{
						setState(75);
						functionDecl();
						}
						break;
					case SQUARE:
					case RECT:
					case CIRCLE:
					case TRIANGLE:
					case SHAPE:
						{
						setState(76);
						declaration();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(79);
					eos();
					}
					} 
				}
				setState(85);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(86);
				statementList();
				}
				break;
			}
			setState(89);
			drawClause();
			setState(90);
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
			setState(92);
			match(VIEWPORT);
			setState(93);
			match(DECIMAL_LIT);
			setState(94);
			match(DECIMAL_LIT);
			setState(95);
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
			setState(97);
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
			setState(99);
			match(IDENTIFIER);
			setState(104);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(100);
					match(COMMA);
					setState(101);
					match(IDENTIFIER);
					}
					} 
				}
				setState(106);
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
			setState(107);
			expression();
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(108);
				match(COMMA);
				setState(109);
				expression();
				}
				}
				setState(114);
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
			setState(115);
			match(FUNC);
			setState(116);
			match(IDENTIFIER);
			{
			setState(117);
			signature();
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(118);
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
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(121);
				if (!(self.noTerminatorAfterParams(1))) throw new FailedPredicateException(this, "self.noTerminatorAfterParams(1)");
				setState(122);
				parameters();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(123);
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
			setState(126);
			match(L_PAREN);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SQUARE) | (1L << RECT) | (1L << CIRCLE) | (1L << TRIANGLE) | (1L << SHAPE))) != 0)) {
				{
				setState(127);
				parameterDecl();
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(128);
					match(COMMA);
					setState(129);
					parameterDecl();
					}
					}
					setState(134);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(137);
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
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
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
			setState(139);
			typeName();
			setState(141);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(140);
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
			setState(143);
			match(DRAW);
			setState(144);
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
			setState(146);
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
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
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
		public List<TerminalNode> WS() { return getTokens(TwoDimParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(TwoDimParser.WS, i);
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
			setState(148);
			typeName();
			setState(149);
			match(IDENTIFIER);
			setState(151);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(150);
				match(WS);
				}
				break;
			}
			setState(153);
			shapeArguments();
			setState(162);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(154);
					match(COMMA);
					setState(156);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(155);
						match(WS);
						}
					}

					setState(158);
					match(IDENTIFIER);
					setState(159);
					shapeArguments();
					}
					} 
				}
				setState(164);
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
			setState(165);
			match(L_CURLY);
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (DRAW - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(166);
				statementList();
				}
			}

			setState(169);
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
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(174); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(171);
					statement();
					setState(172);
					eos();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(176); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
			setState(183);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SQUARE:
			case RECT:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				declaration();
				}
				break;
			case NIL_LIT:
			case IDENTIFIER:
			case DRAW:
			case L_PAREN:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(179);
				simpleStmt();
				}
				break;
			case L_CURLY:
				enterOuterAlt(_localctx, 3);
				{
				setState(180);
				block();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 4);
				{
				setState(181);
				ifStmt();
				}
				break;
			case SWITCH:
				enterOuterAlt(_localctx, 5);
				{
				setState(182);
				switchStmt();
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

	public static class SimpleStmtContext extends ParserRuleContext {
		public ExpressionStmtContext expressionStmt() {
			return getRuleContext(ExpressionStmtContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public DrawClauseContext drawClause() {
			return getRuleContext(DrawClauseContext.class,0);
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
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(185);
				expressionStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(186);
				assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(187);
				drawClause();
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
			setState(190);
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
			setState(193);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(192);
				arguments();
				}
				break;
			}
			setState(196);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(195);
				match(WS);
				}
				break;
			}
			setState(214);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(198);
				match(L_BRACKET);
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(199);
					match(WS);
					}
				}

				setState(202);
				match(SIZE_LIT);
				setState(208);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(203);
					match(COMMA);
					setState(205);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(204);
						match(WS);
						}
					}

					setState(207);
					match(SIZE_LIT);
					}
				}

				setState(211);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(210);
					match(WS);
					}
				}

				setState(213);
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
			setState(216);
			match(IDENTIFIER);
			setState(217);
			assign_op();
			setState(218);
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
			setState(220);
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
			setState(222);
			match(IF);
			setState(226);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(223);
				simpleStmt();
				setState(224);
				match(SEMI);
				}
				break;
			}
			setState(228);
			expression();
			setState(229);
			block();
			setState(235);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(230);
				match(ELSE);
				setState(233);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF:
					{
					setState(231);
					ifStmt();
					}
					break;
				case L_CURLY:
					{
					setState(232);
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
			setState(237);
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
			setState(239);
			match(SWITCH);
			setState(243);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				setState(240);
				simpleStmt();
				setState(241);
				match(SEMI);
				}
				break;
			}
			setState(246);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (L_PAREN - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(245);
				expression();
				}
			}

			setState(248);
			match(L_CURLY);
			setState(252);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(249);
				exprCaseClause();
				}
				}
				setState(254);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(255);
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
			setState(257);
			exprSwitchCase();
			setState(258);
			match(COLON);
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (DRAW - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(259);
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
			setState(265);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(262);
				match(CASE);
				setState(263);
				expression();
				}
				break;
			case DEFAULT:
				enterOuterAlt(_localctx, 2);
				{
				setState(264);
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
		enterRule(_localctx, 50, RULE_typeName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
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
		enterRule(_localctx, 52, RULE_expression);
		int _la;
		try {
			setState(285);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				primaryExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				primaryExpr();
				setState(271);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFT) | (1L << RIGHT) | (1L << TOP) | (1L << BOT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(273);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OUTER || _la==INNER) {
					{
					setState(272);
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

				setState(275);
				primaryExpr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(277);
				primaryExpr();
				setState(278);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ON) | (1L << UNDER) | (1L << IN))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(279);
				primaryExpr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(281);
				primaryExpr();
				setState(282);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(283);
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
		enterRule(_localctx, 54, RULE_primaryExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
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
		enterRule(_localctx, 56, RULE_operand);
		try {
			setState(295);
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
				setState(289);
				literal();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(290);
				operandName();
				}
				break;
			case L_PAREN:
				enterOuterAlt(_localctx, 3);
				{
				setState(291);
				match(L_PAREN);
				setState(292);
				expression();
				setState(293);
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
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			basicLit();
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
		enterRule(_localctx, 60, RULE_basicLit);
		try {
			setState(304);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(299);
				match(NIL_LIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(300);
				integer();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(301);
				string_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(302);
				match(FLOAT_LIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(303);
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
		enterRule(_localctx, 62, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
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
		enterRule(_localctx, 64, RULE_operandName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
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
		enterRule(_localctx, 66, RULE_string_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
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
		enterRule(_localctx, 68, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			match(L_PAREN);
			setState(314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (L_PAREN - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(313);
				expressionList();
				}
			}

			setState(316);
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
		enterRule(_localctx, 70, RULE_eos);
		try {
			setState(323);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(318);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(319);
				match(SEMI);
				setState(320);
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(321);
				if (!(self.lineTerminatorAhead())) throw new FailedPredicateException(this, "self.lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(322);
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
		case 35:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H\u0148\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\5\2L\n\2\3\2\3\2\5\2P\n\2\3\2\3\2\7"+
		"\2T\n\2\f\2\16\2W\13\2\3\2\5\2Z\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3"+
		"\4\3\4\3\5\3\5\3\5\7\5i\n\5\f\5\16\5l\13\5\3\6\3\6\3\6\7\6q\n\6\f\6\16"+
		"\6t\13\6\3\7\3\7\3\7\3\7\5\7z\n\7\3\b\3\b\3\b\5\b\177\n\b\3\t\3\t\3\t"+
		"\3\t\7\t\u0085\n\t\f\t\16\t\u0088\13\t\5\t\u008a\n\t\3\t\3\t\3\n\3\n\5"+
		"\n\u0090\n\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r\u009a\n\r\3\r\3\r"+
		"\3\r\5\r\u009f\n\r\3\r\3\r\7\r\u00a3\n\r\f\r\16\r\u00a6\13\r\3\16\3\16"+
		"\5\16\u00aa\n\16\3\16\3\16\3\17\3\17\3\17\6\17\u00b1\n\17\r\17\16\17\u00b2"+
		"\3\20\3\20\3\20\3\20\3\20\5\20\u00ba\n\20\3\21\3\21\3\21\5\21\u00bf\n"+
		"\21\3\22\3\22\3\23\5\23\u00c4\n\23\3\23\5\23\u00c7\n\23\3\23\3\23\5\23"+
		"\u00cb\n\23\3\23\3\23\3\23\5\23\u00d0\n\23\3\23\5\23\u00d3\n\23\3\23\5"+
		"\23\u00d6\n\23\3\23\5\23\u00d9\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26"+
		"\3\26\3\26\3\26\5\26\u00e5\n\26\3\26\3\26\3\26\3\26\3\26\5\26\u00ec\n"+
		"\26\5\26\u00ee\n\26\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u00f6\n\30\3\30"+
		"\5\30\u00f9\n\30\3\30\3\30\7\30\u00fd\n\30\f\30\16\30\u0100\13\30\3\30"+
		"\3\30\3\31\3\31\3\31\5\31\u0107\n\31\3\32\3\32\3\32\5\32\u010c\n\32\3"+
		"\33\3\33\3\34\3\34\3\34\3\34\5\34\u0114\n\34\3\34\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\34\5\34\u0120\n\34\3\35\3\35\3\36\3\36\3\36\3\36"+
		"\3\36\3\36\5\36\u012a\n\36\3\37\3\37\3 \3 \3 \3 \3 \5 \u0133\n \3!\3!"+
		"\3\"\3\"\3#\3#\3$\3$\5$\u013d\n$\3$\3$\3%\3%\3%\3%\3%\5%\u0146\n%\3%\2"+
		"\2&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B"+
		"DFH\2\t\3\2\16\22\3\2\25\30\3\2\31\32\3\2\33\35\3\2:;\4\2??AA\3\2BC\2"+
		"\u0156\2K\3\2\2\2\4^\3\2\2\2\6c\3\2\2\2\be\3\2\2\2\nm\3\2\2\2\fu\3\2\2"+
		"\2\16~\3\2\2\2\20\u0080\3\2\2\2\22\u008d\3\2\2\2\24\u0091\3\2\2\2\26\u0094"+
		"\3\2\2\2\30\u0096\3\2\2\2\32\u00a7\3\2\2\2\34\u00b0\3\2\2\2\36\u00b9\3"+
		"\2\2\2 \u00be\3\2\2\2\"\u00c0\3\2\2\2$\u00c3\3\2\2\2&\u00da\3\2\2\2(\u00de"+
		"\3\2\2\2*\u00e0\3\2\2\2,\u00ef\3\2\2\2.\u00f1\3\2\2\2\60\u0103\3\2\2\2"+
		"\62\u010b\3\2\2\2\64\u010d\3\2\2\2\66\u011f\3\2\2\28\u0121\3\2\2\2:\u0129"+
		"\3\2\2\2<\u012b\3\2\2\2>\u0132\3\2\2\2@\u0134\3\2\2\2B\u0136\3\2\2\2D"+
		"\u0138\3\2\2\2F\u013a\3\2\2\2H\u0145\3\2\2\2JL\5\4\3\2KJ\3\2\2\2KL\3\2"+
		"\2\2LU\3\2\2\2MP\5\f\7\2NP\5\6\4\2OM\3\2\2\2ON\3\2\2\2PQ\3\2\2\2QR\5H"+
		"%\2RT\3\2\2\2SO\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VY\3\2\2\2WU\3\2"+
		"\2\2XZ\5\34\17\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\5\24\13\2\\]\5H%\2]"+
		"\3\3\2\2\2^_\7\24\2\2_`\7?\2\2`a\7?\2\2ab\5H%\2b\5\3\2\2\2cd\5\26\f\2"+
		"d\7\3\2\2\2ej\7\r\2\2fg\7%\2\2gi\7\r\2\2hf\3\2\2\2il\3\2\2\2jh\3\2\2\2"+
		"jk\3\2\2\2k\t\3\2\2\2lj\3\2\2\2mr\5\66\34\2no\7%\2\2oq\5\66\34\2pn\3\2"+
		"\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\13\3\2\2\2tr\3\2\2\2uv\7\3\2\2vw\7"+
		"\r\2\2wy\5\16\b\2xz\5\32\16\2yx\3\2\2\2yz\3\2\2\2z\r\3\2\2\2{|\6\b\2\2"+
		"|\177\5\20\t\2}\177\5\20\t\2~{\3\2\2\2~}\3\2\2\2\177\17\3\2\2\2\u0080"+
		"\u0089\7\36\2\2\u0081\u0086\5\22\n\2\u0082\u0083\7%\2\2\u0083\u0085\5"+
		"\22\n\2\u0084\u0082\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086"+
		"\u0087\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u0081\3\2"+
		"\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7\37\2\2\u008c"+
		"\21\3\2\2\2\u008d\u008f\5\64\33\2\u008e\u0090\5\b\5\2\u008f\u008e\3\2"+
		"\2\2\u008f\u0090\3\2\2\2\u0090\23\3\2\2\2\u0091\u0092\7\23\2\2\u0092\u0093"+
		"\7\r\2\2\u0093\25\3\2\2\2\u0094\u0095\5\30\r\2\u0095\27\3\2\2\2\u0096"+
		"\u0097\5\64\33\2\u0097\u0099\7\r\2\2\u0098\u009a\7E\2\2\u0099\u0098\3"+
		"\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a4\5$\23\2\u009c"+
		"\u009e\7%\2\2\u009d\u009f\7E\2\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2"+
		"\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\r\2\2\u00a1\u00a3\5$\23\2\u00a2\u009c"+
		"\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5"+
		"\31\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\7 \2\2\u00a8\u00aa\5\34\17"+
		"\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac"+
		"\7!\2\2\u00ac\33\3\2\2\2\u00ad\u00ae\5\36\20\2\u00ae\u00af\5H%\2\u00af"+
		"\u00b1\3\2\2\2\u00b0\u00ad\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2"+
		"\2\2\u00b2\u00b3\3\2\2\2\u00b3\35\3\2\2\2\u00b4\u00ba\5\6\4\2\u00b5\u00ba"+
		"\5 \21\2\u00b6\u00ba\5\32\16\2\u00b7\u00ba\5*\26\2\u00b8\u00ba\5,\27\2"+
		"\u00b9\u00b4\3\2\2\2\u00b9\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7"+
		"\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\37\3\2\2\2\u00bb\u00bf\5\"\22\2\u00bc"+
		"\u00bf\5&\24\2\u00bd\u00bf\5\24\13\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3"+
		"\2\2\2\u00be\u00bd\3\2\2\2\u00bf!\3\2\2\2\u00c0\u00c1\5\66\34\2\u00c1"+
		"#\3\2\2\2\u00c2\u00c4\5F$\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4"+
		"\u00c6\3\2\2\2\u00c5\u00c7\7E\2\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2"+
		"\2\2\u00c7\u00d8\3\2\2\2\u00c8\u00ca\7\"\2\2\u00c9\u00cb\7E\2\2\u00ca"+
		"\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00d2\7D"+
		"\2\2\u00cd\u00cf\7%\2\2\u00ce\u00d0\7E\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0"+
		"\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\7D\2\2\u00d2\u00cd\3\2\2\2\u00d2"+
		"\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d6\7E\2\2\u00d5\u00d4\3\2"+
		"\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\7#\2\2\u00d8"+
		"\u00c8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9%\3\2\2\2\u00da\u00db\7\r\2\2"+
		"\u00db\u00dc\5(\25\2\u00dc\u00dd\5\66\34\2\u00dd\'\3\2\2\2\u00de\u00df"+
		"\7$\2\2\u00df)\3\2\2\2\u00e0\u00e4\7\7\2\2\u00e1\u00e2\5 \21\2\u00e2\u00e3"+
		"\7&\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5"+
		"\u00e6\3\2\2\2\u00e6\u00e7\5\66\34\2\u00e7\u00ed\5\32\16\2\u00e8\u00eb"+
		"\7\b\2\2\u00e9\u00ec\5*\26\2\u00ea\u00ec\5\32\16\2\u00eb\u00e9\3\2\2\2"+
		"\u00eb\u00ea\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ed\u00ee"+
		"\3\2\2\2\u00ee+\3\2\2\2\u00ef\u00f0\5.\30\2\u00f0-\3\2\2\2\u00f1\u00f5"+
		"\7\4\2\2\u00f2\u00f3\5 \21\2\u00f3\u00f4\7&\2\2\u00f4\u00f6\3\2\2\2\u00f5"+
		"\u00f2\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f9\5\66"+
		"\34\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa"+
		"\u00fe\7 \2\2\u00fb\u00fd\5\60\31\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3"+
		"\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100"+
		"\u00fe\3\2\2\2\u0101\u0102\7!\2\2\u0102/\3\2\2\2\u0103\u0104\5\62\32\2"+
		"\u0104\u0106\7\'\2\2\u0105\u0107\5\34\17\2\u0106\u0105\3\2\2\2\u0106\u0107"+
		"\3\2\2\2\u0107\61\3\2\2\2\u0108\u0109\7\5\2\2\u0109\u010c\5\66\34\2\u010a"+
		"\u010c\7\6\2\2\u010b\u0108\3\2\2\2\u010b\u010a\3\2\2\2\u010c\63\3\2\2"+
		"\2\u010d\u010e\t\2\2\2\u010e\65\3\2\2\2\u010f\u0120\58\35\2\u0110\u0111"+
		"\58\35\2\u0111\u0113\t\3\2\2\u0112\u0114\t\4\2\2\u0113\u0112\3\2\2\2\u0113"+
		"\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\58\35\2\u0116\u0120\3\2"+
		"\2\2\u0117\u0118\58\35\2\u0118\u0119\t\5\2\2\u0119\u011a\58\35\2\u011a"+
		"\u0120\3\2\2\2\u011b\u011c\58\35\2\u011c\u011d\t\6\2\2\u011d\u011e\58"+
		"\35\2\u011e\u0120\3\2\2\2\u011f\u010f\3\2\2\2\u011f\u0110\3\2\2\2\u011f"+
		"\u0117\3\2\2\2\u011f\u011b\3\2\2\2\u0120\67\3\2\2\2\u0121\u0122\5:\36"+
		"\2\u01229\3\2\2\2\u0123\u012a\5<\37\2\u0124\u012a\5B\"\2\u0125\u0126\7"+
		"\36\2\2\u0126\u0127\5\66\34\2\u0127\u0128\7\37\2\2\u0128\u012a\3\2\2\2"+
		"\u0129\u0123\3\2\2\2\u0129\u0124\3\2\2\2\u0129\u0125\3\2\2\2\u012a;\3"+
		"\2\2\2\u012b\u012c\5> \2\u012c=\3\2\2\2\u012d\u0133\7\f\2\2\u012e\u0133"+
		"\5@!\2\u012f\u0133\5D#\2\u0130\u0133\7@\2\2\u0131\u0133\7A\2\2\u0132\u012d"+
		"\3\2\2\2\u0132\u012e\3\2\2\2\u0132\u012f\3\2\2\2\u0132\u0130\3\2\2\2\u0132"+
		"\u0131\3\2\2\2\u0133?\3\2\2\2\u0134\u0135\t\7\2\2\u0135A\3\2\2\2\u0136"+
		"\u0137\7\r\2\2\u0137C\3\2\2\2\u0138\u0139\t\b\2\2\u0139E\3\2\2\2\u013a"+
		"\u013c\7\36\2\2\u013b\u013d\5\n\6\2\u013c\u013b\3\2\2\2\u013c\u013d\3"+
		"\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\7\37\2\2\u013fG\3\2\2\2\u0140\u0146"+
		"\7&\2\2\u0141\u0142\7&\2\2\u0142\u0146\7\2\2\3\u0143\u0146\6%\3\2\u0144"+
		"\u0146\6%\4\2\u0145\u0140\3\2\2\2\u0145\u0141\3\2\2\2\u0145\u0143\3\2"+
		"\2\2\u0145\u0144\3\2\2\2\u0146I\3\2\2\2)KOUYjry~\u0086\u0089\u008f\u0099"+
		"\u009e\u00a4\u00a9\u00b2\u00b9\u00be\u00c3\u00c6\u00ca\u00cf\u00d2\u00d5"+
		"\u00d8\u00e4\u00eb\u00ed\u00f5\u00f8\u00fe\u0106\u010b\u0113\u011f\u0129"+
		"\u0132\u013c\u0145";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}