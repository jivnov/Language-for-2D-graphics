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
		RUNE_LIT=63, RAW_STRING_LIT=64, INTERPRETED_STRING_LIT=65, WS=66, COMMENT=67, 
		TERMINATOR=68, LINE_COMMENT=69, DECIMALS=70, SIZE=71;
	public static final int
		RULE_sourceFile = 0, RULE_viewportClause = 1, RULE_declaration = 2, RULE_identifierList = 3, 
		RULE_drawClause = 4, RULE_varDecl = 5, RULE_varSpec = 6, RULE_block = 7, 
		RULE_statementList = 8, RULE_statement = 9, RULE_simpleStmt = 10, RULE_expressionStmt = 11, 
		RULE_declStmt = 12, RULE_assignment = 13, RULE_assign_op = 14, RULE_ifStmt = 15, 
		RULE_switchStmt = 16, RULE_exprSwitchStmt = 17, RULE_exprCaseClause = 18, 
		RULE_exprSwitchCase = 19, RULE_type_ = 20, RULE_typeName = 21, RULE_elementType = 22, 
		RULE_expression = 23, RULE_primaryExpr = 24, RULE_operand = 25, RULE_literal = 26, 
		RULE_basicLit = 27, RULE_integer = 28, RULE_operandName = 29, RULE_compositeLit = 30, 
		RULE_literalType = 31, RULE_literalValue = 32, RULE_element = 33, RULE_string_ = 34, 
		RULE_arguments = 35, RULE_eos = 36;
	private static String[] makeRuleNames() {
		return new String[] {
			"sourceFile", "viewportClause", "declaration", "identifierList", "drawClause", 
			"varDecl", "varSpec", "block", "statementList", "statement", "simpleStmt", 
			"expressionStmt", "declStmt", "assignment", "assign_op", "ifStmt", "switchStmt", 
			"exprSwitchStmt", "exprCaseClause", "exprSwitchCase", "type_", "typeName", 
			"elementType", "expression", "primaryExpr", "operand", "literal", "basicLit", 
			"integer", "operandName", "compositeLit", "literalType", "literalValue", 
			"element", "string_", "arguments", "eos"
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
			"RAW_STRING_LIT", "INTERPRETED_STRING_LIT", "WS", "COMMENT", "TERMINATOR", 
			"LINE_COMMENT", "DECIMALS", "SIZE"
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
		public ViewportClauseContext viewportClause() {
			return getRuleContext(ViewportClauseContext.class,0);
		}
		public DrawClauseContext drawClause() {
			return getRuleContext(DrawClauseContext.class,0);
		}
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			viewportClause();
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SQUARE) | (1L << RECT) | (1L << CIRCLE) | (1L << TRIANGLE) | (1L << SHAPE) | (1L << L_PAREN))) != 0)) {
				{
				{
				setState(75);
				declaration();
				setState(76);
				eos();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			drawClause();
			setState(84);
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
		public List<TerminalNode> DECIMALS() { return getTokens(TwoDimParser.DECIMALS); }
		public TerminalNode DECIMALS(int i) {
			return getToken(TwoDimParser.DECIMALS, i);
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
			setState(86);
			match(VIEWPORT);
			setState(87);
			match(WS);
			setState(88);
			match(DECIMALS);
			setState(89);
			match(WS);
			setState(90);
			match(DECIMALS);
			setState(91);
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
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
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
			setState(93);
			varDecl();
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(IDENTIFIER);
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(96);
				match(COMMA);
				setState(97);
				match(IDENTIFIER);
				}
				}
				setState(102);
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
		enterRule(_localctx, 8, RULE_drawClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(DRAW);
			setState(104);
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

	public static class VarDeclContext extends ParserRuleContext {
		public List<VarSpecContext> varSpec() {
			return getRuleContexts(VarSpecContext.class);
		}
		public VarSpecContext varSpec(int i) {
			return getRuleContext(VarSpecContext.class,i);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(106);
				varSpec();
				}
				break;
			case 2:
				{
				setState(107);
				match(L_PAREN);
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SQUARE) | (1L << RECT) | (1L << CIRCLE) | (1L << TRIANGLE) | (1L << SHAPE) | (1L << L_PAREN))) != 0)) {
					{
					{
					setState(108);
					varSpec();
					setState(109);
					eos();
					}
					}
					setState(115);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(116);
				match(R_PAREN);
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

	public static class VarSpecContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(TwoDimParser.ASSIGN, 0); }
		public DeclStmtContext declStmt() {
			return getRuleContext(DeclStmtContext.class,0);
		}
		public VarSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varSpec; }
	}

	public final VarSpecContext varSpec() throws RecognitionException {
		VarSpecContext _localctx = new VarSpecContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_varSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			type_();
			setState(120);
			identifierList();
			setState(121);
			match(ASSIGN);
			setState(122);
			declStmt();
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
		enterRule(_localctx, 14, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(L_CURLY);
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(125);
				statementList();
				}
			}

			setState(128);
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
		enterRule(_localctx, 16, RULE_statementList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(130);
				statement();
				setState(131);
				eos();
				}
				}
				setState(135); 
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
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				simpleStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(139);
				block();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(140);
				ifStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(141);
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
		enterRule(_localctx, 20, RULE_simpleStmt);
		try {
			setState(146);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(144);
				expressionStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(145);
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
		enterRule(_localctx, 22, RULE_expressionStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
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

	public static class DeclStmtContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public TerminalNode L_BRACKET() { return getToken(TwoDimParser.L_BRACKET, 0); }
		public List<TerminalNode> SIZE() { return getTokens(TwoDimParser.SIZE); }
		public TerminalNode SIZE(int i) {
			return getToken(TwoDimParser.SIZE, i);
		}
		public TerminalNode R_BRACKET() { return getToken(TwoDimParser.R_BRACKET, 0); }
		public TerminalNode COMMA() { return getToken(TwoDimParser.COMMA, 0); }
		public TerminalNode WS() { return getToken(TwoDimParser.WS, 0); }
		public DeclStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declStmt; }
	}

	public final DeclStmtContext declStmt() throws RecognitionException {
		DeclStmtContext _localctx = new DeclStmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_declStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			type_();
			setState(151);
			match(L_PAREN);
			setState(152);
			arguments();
			setState(153);
			match(R_PAREN);
			setState(164);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(154);
				match(L_BRACKET);
				setState(155);
				match(SIZE);
				setState(161);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(156);
					match(COMMA);
					setState(158);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(157);
						match(WS);
						}
					}

					setState(160);
					match(SIZE);
					}
				}

				setState(163);
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
		enterRule(_localctx, 26, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(IDENTIFIER);
			setState(167);
			assign_op();
			setState(168);
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
		enterRule(_localctx, 28, RULE_assign_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
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
		enterRule(_localctx, 30, RULE_ifStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(IF);
			setState(176);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(173);
				simpleStmt();
				setState(174);
				match(SEMI);
				}
				break;
			}
			setState(178);
			expression();
			setState(179);
			block();
			setState(185);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(180);
				match(ELSE);
				setState(183);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF:
					{
					setState(181);
					ifStmt();
					}
					break;
				case L_CURLY:
					{
					setState(182);
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
		enterRule(_localctx, 32, RULE_switchStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
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
		enterRule(_localctx, 34, RULE_exprSwitchStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			match(SWITCH);
			setState(193);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(190);
				simpleStmt();
				setState(191);
				match(SEMI);
				}
				break;
			}
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (SQUARE - 10)) | (1L << (RECT - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)) | (1L << (L_PAREN - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(195);
				expression();
				}
			}

			setState(198);
			match(L_CURLY);
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(199);
				exprCaseClause();
				}
				}
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(205);
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
		enterRule(_localctx, 36, RULE_exprCaseClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			exprSwitchCase();
			setState(208);
			match(COLON);
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 2)) & ~0x3f) == 0 && ((1L << (_la - 2)) & ((1L << (SWITCH - 2)) | (1L << (IF - 2)) | (1L << (NIL_LIT - 2)) | (1L << (IDENTIFIER - 2)) | (1L << (SQUARE - 2)) | (1L << (RECT - 2)) | (1L << (CIRCLE - 2)) | (1L << (TRIANGLE - 2)) | (1L << (SHAPE - 2)) | (1L << (L_PAREN - 2)) | (1L << (L_CURLY - 2)) | (1L << (DECIMAL_LIT - 2)) | (1L << (FLOAT_LIT - 2)) | (1L << (RUNE_LIT - 2)) | (1L << (RAW_STRING_LIT - 2)) | (1L << (INTERPRETED_STRING_LIT - 2)))) != 0)) {
				{
				setState(209);
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
		enterRule(_localctx, 38, RULE_exprSwitchCase);
		try {
			setState(215);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(212);
				match(CASE);
				setState(213);
				expression();
				}
				break;
			case DEFAULT:
				enterOuterAlt(_localctx, 2);
				{
				setState(214);
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
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public Type_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_; }
	}

	public final Type_Context type_() throws RecognitionException {
		Type_Context _localctx = new Type_Context(_ctx, getState());
		enterRule(_localctx, 40, RULE_type_);
		try {
			setState(222);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SQUARE:
			case RECT:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(217);
				typeName();
				}
				break;
			case L_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(218);
				match(L_PAREN);
				setState(219);
				type_();
				setState(220);
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
		enterRule(_localctx, 42, RULE_typeName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
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
		enterRule(_localctx, 44, RULE_elementType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
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
		enterRule(_localctx, 46, RULE_expression);
		int _la;
		try {
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				primaryExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(229);
				primaryExpr();
				setState(230);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFT) | (1L << RIGHT) | (1L << TOP) | (1L << BOT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(232);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OUTER || _la==INNER) {
					{
					setState(231);
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

				setState(234);
				primaryExpr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(236);
				primaryExpr();
				setState(237);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ON) | (1L << UNDER) | (1L << IN))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(238);
				primaryExpr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(240);
				primaryExpr();
				setState(241);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(242);
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
		enterRule(_localctx, 48, RULE_primaryExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
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
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_operand);
		try {
			setState(250);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NIL_LIT:
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
				setState(248);
				literal();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(249);
				operandName();
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
		enterRule(_localctx, 52, RULE_literal);
		try {
			setState(254);
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
				setState(252);
				basicLit();
				}
				break;
			case SQUARE:
			case RECT:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
			case L_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(253);
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
		enterRule(_localctx, 54, RULE_basicLit);
		try {
			setState(261);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(256);
				match(NIL_LIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(257);
				integer();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(258);
				string_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(259);
				match(FLOAT_LIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(260);
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
		enterRule(_localctx, 56, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
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
		enterRule(_localctx, 58, RULE_operandName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
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
		enterRule(_localctx, 60, RULE_compositeLit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			literalType();
			setState(268);
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
		public LiteralTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalType; }
	}

	public final LiteralTypeContext literalType() throws RecognitionException {
		LiteralTypeContext _localctx = new LiteralTypeContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_literalType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			elementType();
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
		enterRule(_localctx, 64, RULE_literalValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(L_CURLY);
			setState(274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (SQUARE - 10)) | (1L << (RECT - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)) | (1L << (L_PAREN - 10)) | (1L << (L_CURLY - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)))) != 0)) {
				{
				setState(273);
				element();
				}
			}

			setState(276);
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
		enterRule(_localctx, 66, RULE_element);
		try {
			setState(280);
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
				setState(278);
				expression();
				}
				break;
			case L_CURLY:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
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
		enterRule(_localctx, 68, RULE_string_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
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
		public List<TerminalNode> SIZE() { return getTokens(TwoDimParser.SIZE); }
		public TerminalNode SIZE(int i) {
			return getToken(TwoDimParser.SIZE, i);
		}
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public TerminalNode COMMA() { return getToken(TwoDimParser.COMMA, 0); }
		public TerminalNode WS() { return getToken(TwoDimParser.WS, 0); }
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(L_PAREN);
			setState(285);
			match(SIZE);
			setState(291);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(286);
				match(COMMA);
				setState(288);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(287);
					match(WS);
					}
				}

				setState(290);
				match(SIZE);
				}
			}

			setState(293);
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
		enterRule(_localctx, 72, RULE_eos);
		try {
			setState(299);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(295);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(296);
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(297);
				if (!(lineTerminatorAhead())) throw new FailedPredicateException(this, "lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(298);
				if (!(checkPreviousTokenText("}"))) throw new FailedPredicateException(this, "checkPreviousTokenText(\"}\")");
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
		case 36:
			return eos_sempred((EosContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean eos_sempred(EosContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return lineTerminatorAhead();
		case 1:
			return checkPreviousTokenText("}");
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I\u0130\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\3\2\3\2\7\2Q\n\2\f\2\16\2"+
		"T\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5"+
		"e\n\5\f\5\16\5h\13\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7r\n\7\f\7\16\7"+
		"u\13\7\3\7\5\7x\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u0081\n\t\3\t\3\t"+
		"\3\n\3\n\3\n\6\n\u0088\n\n\r\n\16\n\u0089\3\13\3\13\3\13\3\13\3\13\5\13"+
		"\u0091\n\13\3\f\3\f\5\f\u0095\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\5\16\u00a1\n\16\3\16\5\16\u00a4\n\16\3\16\5\16\u00a7\n\16\3"+
		"\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00b3\n\21\3\21"+
		"\3\21\3\21\3\21\3\21\5\21\u00ba\n\21\5\21\u00bc\n\21\3\22\3\22\3\23\3"+
		"\23\3\23\3\23\5\23\u00c4\n\23\3\23\5\23\u00c7\n\23\3\23\3\23\7\23\u00cb"+
		"\n\23\f\23\16\23\u00ce\13\23\3\23\3\23\3\24\3\24\3\24\5\24\u00d5\n\24"+
		"\3\25\3\25\3\25\5\25\u00da\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00e1\n"+
		"\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u00eb\n\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00f7\n\31\3\32\3\32\3\33"+
		"\3\33\5\33\u00fd\n\33\3\34\3\34\5\34\u0101\n\34\3\35\3\35\3\35\3\35\3"+
		"\35\5\35\u0108\n\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\5\"\u0115"+
		"\n\"\3\"\3\"\3#\3#\5#\u011b\n#\3$\3$\3%\3%\3%\3%\5%\u0123\n%\3%\5%\u0126"+
		"\n%\3%\3%\3&\3&\3&\3&\5&\u012e\n&\3&\2\2\'\2\4\6\b\n\f\16\20\22\24\26"+
		"\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJ\2\t\3\2\16\22\3\2\25\30\3"+
		"\2\31\32\3\2\33\35\3\2:;\4\2??AA\3\2BC\2\u0132\2L\3\2\2\2\4X\3\2\2\2\6"+
		"_\3\2\2\2\ba\3\2\2\2\ni\3\2\2\2\fw\3\2\2\2\16y\3\2\2\2\20~\3\2\2\2\22"+
		"\u0087\3\2\2\2\24\u0090\3\2\2\2\26\u0094\3\2\2\2\30\u0096\3\2\2\2\32\u0098"+
		"\3\2\2\2\34\u00a8\3\2\2\2\36\u00ac\3\2\2\2 \u00ae\3\2\2\2\"\u00bd\3\2"+
		"\2\2$\u00bf\3\2\2\2&\u00d1\3\2\2\2(\u00d9\3\2\2\2*\u00e0\3\2\2\2,\u00e2"+
		"\3\2\2\2.\u00e4\3\2\2\2\60\u00f6\3\2\2\2\62\u00f8\3\2\2\2\64\u00fc\3\2"+
		"\2\2\66\u0100\3\2\2\28\u0107\3\2\2\2:\u0109\3\2\2\2<\u010b\3\2\2\2>\u010d"+
		"\3\2\2\2@\u0110\3\2\2\2B\u0112\3\2\2\2D\u011a\3\2\2\2F\u011c\3\2\2\2H"+
		"\u011e\3\2\2\2J\u012d\3\2\2\2LR\5\4\3\2MN\5\6\4\2NO\5J&\2OQ\3\2\2\2PM"+
		"\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\5\n\6\2V"+
		"W\5J&\2W\3\3\2\2\2XY\7\24\2\2YZ\7D\2\2Z[\7H\2\2[\\\7D\2\2\\]\7H\2\2]^"+
		"\5J&\2^\5\3\2\2\2_`\5\f\7\2`\7\3\2\2\2af\7\r\2\2bc\7%\2\2ce\7\r\2\2db"+
		"\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2g\t\3\2\2\2hf\3\2\2\2ij\7\23\2\2"+
		"jk\7\r\2\2k\13\3\2\2\2lx\5\16\b\2ms\7\36\2\2no\5\16\b\2op\5J&\2pr\3\2"+
		"\2\2qn\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vx\7\37"+
		"\2\2wl\3\2\2\2wm\3\2\2\2x\r\3\2\2\2yz\5*\26\2z{\5\b\5\2{|\7$\2\2|}\5\32"+
		"\16\2}\17\3\2\2\2~\u0080\7 \2\2\177\u0081\5\22\n\2\u0080\177\3\2\2\2\u0080"+
		"\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7!\2\2\u0083\21\3\2\2\2"+
		"\u0084\u0085\5\24\13\2\u0085\u0086\5J&\2\u0086\u0088\3\2\2\2\u0087\u0084"+
		"\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a"+
		"\23\3\2\2\2\u008b\u0091\5\6\4\2\u008c\u0091\5\26\f\2\u008d\u0091\5\20"+
		"\t\2\u008e\u0091\5 \21\2\u008f\u0091\5\"\22\2\u0090\u008b\3\2\2\2\u0090"+
		"\u008c\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2"+
		"\2\2\u0091\25\3\2\2\2\u0092\u0095\5\30\r\2\u0093\u0095\5\34\17\2\u0094"+
		"\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095\27\3\2\2\2\u0096\u0097\5\60\31"+
		"\2\u0097\31\3\2\2\2\u0098\u0099\5*\26\2\u0099\u009a\7\36\2\2\u009a\u009b"+
		"\5H%\2\u009b\u00a6\7\37\2\2\u009c\u009d\7\"\2\2\u009d\u00a3\7I\2\2\u009e"+
		"\u00a0\7%\2\2\u009f\u00a1\7D\2\2\u00a0\u009f\3\2\2\2\u00a0\u00a1\3\2\2"+
		"\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\7I\2\2\u00a3\u009e\3\2\2\2\u00a3\u00a4"+
		"\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7\7#\2\2\u00a6\u009c\3\2\2\2\u00a6"+
		"\u00a7\3\2\2\2\u00a7\33\3\2\2\2\u00a8\u00a9\7\r\2\2\u00a9\u00aa\5\36\20"+
		"\2\u00aa\u00ab\5\60\31\2\u00ab\35\3\2\2\2\u00ac\u00ad\7$\2\2\u00ad\37"+
		"\3\2\2\2\u00ae\u00b2\7\7\2\2\u00af\u00b0\5\26\f\2\u00b0\u00b1\7&\2\2\u00b1"+
		"\u00b3\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2"+
		"\2\2\u00b4\u00b5\5\60\31\2\u00b5\u00bb\5\20\t\2\u00b6\u00b9\7\b\2\2\u00b7"+
		"\u00ba\5 \21\2\u00b8\u00ba\5\20\t\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3"+
		"\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b6\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc"+
		"!\3\2\2\2\u00bd\u00be\5$\23\2\u00be#\3\2\2\2\u00bf\u00c3\7\4\2\2\u00c0"+
		"\u00c1\5\26\f\2\u00c1\u00c2\7&\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c0\3\2"+
		"\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c7\5\60\31\2\u00c6"+
		"\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cc\7 "+
		"\2\2\u00c9\u00cb\5&\24\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc"+
		"\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2"+
		"\2\2\u00cf\u00d0\7!\2\2\u00d0%\3\2\2\2\u00d1\u00d2\5(\25\2\u00d2\u00d4"+
		"\7\'\2\2\u00d3\u00d5\5\22\n\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2"+
		"\u00d5\'\3\2\2\2\u00d6\u00d7\7\5\2\2\u00d7\u00da\5\60\31\2\u00d8\u00da"+
		"\7\6\2\2\u00d9\u00d6\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da)\3\2\2\2\u00db"+
		"\u00e1\5,\27\2\u00dc\u00dd\7\36\2\2\u00dd\u00de\5*\26\2\u00de\u00df\7"+
		"\37\2\2\u00df\u00e1\3\2\2\2\u00e0\u00db\3\2\2\2\u00e0\u00dc\3\2\2\2\u00e1"+
		"+\3\2\2\2\u00e2\u00e3\t\2\2\2\u00e3-\3\2\2\2\u00e4\u00e5\5*\26\2\u00e5"+
		"/\3\2\2\2\u00e6\u00f7\5\62\32\2\u00e7\u00e8\5\62\32\2\u00e8\u00ea\t\3"+
		"\2\2\u00e9\u00eb\t\4\2\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb"+
		"\u00ec\3\2\2\2\u00ec\u00ed\5\62\32\2\u00ed\u00f7\3\2\2\2\u00ee\u00ef\5"+
		"\62\32\2\u00ef\u00f0\t\5\2\2\u00f0\u00f1\5\62\32\2\u00f1\u00f7\3\2\2\2"+
		"\u00f2\u00f3\5\62\32\2\u00f3\u00f4\t\6\2\2\u00f4\u00f5\5\62\32\2\u00f5"+
		"\u00f7\3\2\2\2\u00f6\u00e6\3\2\2\2\u00f6\u00e7\3\2\2\2\u00f6\u00ee\3\2"+
		"\2\2\u00f6\u00f2\3\2\2\2\u00f7\61\3\2\2\2\u00f8\u00f9\5\64\33\2\u00f9"+
		"\63\3\2\2\2\u00fa\u00fd\5\66\34\2\u00fb\u00fd\5<\37\2\u00fc\u00fa\3\2"+
		"\2\2\u00fc\u00fb\3\2\2\2\u00fd\65\3\2\2\2\u00fe\u0101\58\35\2\u00ff\u0101"+
		"\5> \2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101\67\3\2\2\2\u0102"+
		"\u0108\7\f\2\2\u0103\u0108\5:\36\2\u0104\u0108\5F$\2\u0105\u0108\7@\2"+
		"\2\u0106\u0108\7A\2\2\u0107\u0102\3\2\2\2\u0107\u0103\3\2\2\2\u0107\u0104"+
		"\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u01089\3\2\2\2\u0109"+
		"\u010a\t\7\2\2\u010a;\3\2\2\2\u010b\u010c\7\r\2\2\u010c=\3\2\2\2\u010d"+
		"\u010e\5@!\2\u010e\u010f\5B\"\2\u010f?\3\2\2\2\u0110\u0111\5.\30\2\u0111"+
		"A\3\2\2\2\u0112\u0114\7 \2\2\u0113\u0115\5D#\2\u0114\u0113\3\2\2\2\u0114"+
		"\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\7!\2\2\u0117C\3\2\2\2\u0118"+
		"\u011b\5\60\31\2\u0119\u011b\5B\"\2\u011a\u0118\3\2\2\2\u011a\u0119\3"+
		"\2\2\2\u011bE\3\2\2\2\u011c\u011d\t\b\2\2\u011dG\3\2\2\2\u011e\u011f\7"+
		"\36\2\2\u011f\u0125\7I\2\2\u0120\u0122\7%\2\2\u0121\u0123\7D\2\2\u0122"+
		"\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\7I"+
		"\2\2\u0125\u0120\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127"+
		"\u0128\7\37\2\2\u0128I\3\2\2\2\u0129\u012e\7&\2\2\u012a\u012e\7\2\2\3"+
		"\u012b\u012e\6&\2\2\u012c\u012e\6&\3\2\u012d\u0129\3\2\2\2\u012d\u012a"+
		"\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012c\3\2\2\2\u012eK\3\2\2\2 Rfsw\u0080"+
		"\u0089\u0090\u0094\u00a0\u00a3\u00a6\u00b2\u00b9\u00bb\u00c3\u00c6\u00cc"+
		"\u00d4\u00d9\u00e0\u00ea\u00f6\u00fc\u0100\u0107\u0114\u011a\u0122\u0125"+
		"\u012d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}