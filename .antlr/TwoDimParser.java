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
		IMPORT=9, NIL_LIT=10, IDENTIFIER=11, DRAW=12, LEFT=13, RIGHT=14, TOP=15, 
		BOT=16, OUTER=17, INNER=18, ON=19, UNDER=20, IN=21, L_PAREN=22, R_PAREN=23, 
		L_CURLY=24, R_CURLY=25, L_BRACKET=26, R_BRACKET=27, ASSIGN=28, COMMA=29, 
		SEMI=30, COLON=31, DOT=32, PLUS_PLUS=33, MINUS_MINUS=34, LOGICAL_OR=35, 
		LOGICAL_AND=36, EQUALS=37, NOT_EQUALS=38, LESS=39, LESS_OR_EQUALS=40, 
		GREATER=41, GREATER_OR_EQUALS=42, OR=43, DIV=44, MOD=45, LSHIFT=46, RSHIFT=47, 
		BIT_CLEAR=48, EXCLAMATION=49, PLUS=50, MINUS=51, CARET=52, STAR=53, AMPERSAND=54, 
		DECIMAL_LIT=55, FLOAT_LIT=56, RUNE_LIT=57, RAW_STRING_LIT=58, INTERPRETED_STRING_LIT=59, 
		WS=60, COMMENT=61, TERMINATOR=62, LINE_COMMENT=63, VIEWPORT=64, DECIMALS=65, 
		SIZE=66, RECT=67, SQUARE=68, CIRCLE=69, TRIANGLE=70, SHAPE=71;
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
			"'type'", "'package'", "'import'", "'nil'", null, "'draw'", "'left'", 
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
			"IMPORT", "NIL_LIT", "IDENTIFIER", "DRAW", "LEFT", "RIGHT", "TOP", "BOT", 
			"OUTER", "INNER", "ON", "UNDER", "IN", "L_PAREN", "R_PAREN", "L_CURLY", 
			"R_CURLY", "L_BRACKET", "R_BRACKET", "ASSIGN", "COMMA", "SEMI", "COLON", 
			"DOT", "PLUS_PLUS", "MINUS_MINUS", "LOGICAL_OR", "LOGICAL_AND", "EQUALS", 
			"NOT_EQUALS", "LESS", "LESS_OR_EQUALS", "GREATER", "GREATER_OR_EQUALS", 
			"OR", "DIV", "MOD", "LSHIFT", "RSHIFT", "BIT_CLEAR", "EXCLAMATION", "PLUS", 
			"MINUS", "CARET", "STAR", "AMPERSAND", "DECIMAL_LIT", "FLOAT_LIT", "RUNE_LIT", 
			"RAW_STRING_LIT", "INTERPRETED_STRING_LIT", "WS", "COMMENT", "TERMINATOR", 
			"LINE_COMMENT", "VIEWPORT", "DECIMALS", "SIZE", "RECT", "SQUARE", "CIRCLE", 
			"TRIANGLE", "SHAPE"
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
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
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
			while (((((_la - 22)) & ~0x3f) == 0 && ((1L << (_la - 22)) & ((1L << (L_PAREN - 22)) | (1L << (RECT - 22)) | (1L << (SQUARE - 22)) | (1L << (CIRCLE - 22)) | (1L << (TRIANGLE - 22)) | (1L << (SHAPE - 22)))) != 0)) {
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
			setState(83);
			match(VIEWPORT);
			setState(84);
			match(WS);
			setState(85);
			match(DECIMALS);
			setState(86);
			match(WS);
			setState(87);
			match(DECIMALS);
			setState(88);
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
			setState(90);
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
			setState(92);
			match(IDENTIFIER);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(93);
				match(COMMA);
				setState(94);
				match(IDENTIFIER);
				}
				}
				setState(99);
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
			setState(100);
			match(DRAW);
			setState(101);
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
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(103);
				varSpec();
				}
				break;
			case 2:
				{
				setState(104);
				match(L_PAREN);
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (((((_la - 22)) & ~0x3f) == 0 && ((1L << (_la - 22)) & ((1L << (L_PAREN - 22)) | (1L << (RECT - 22)) | (1L << (SQUARE - 22)) | (1L << (CIRCLE - 22)) | (1L << (TRIANGLE - 22)) | (1L << (SHAPE - 22)))) != 0)) {
					{
					{
					setState(105);
					varSpec();
					setState(106);
					eos();
					}
					}
					setState(112);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(113);
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
			setState(116);
			type_();
			setState(117);
			identifierList();
			setState(118);
			match(ASSIGN);
			setState(119);
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
			setState(121);
			match(L_CURLY);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SWITCH) | (1L << IF) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0) || ((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & ((1L << (RECT - 67)) | (1L << (SQUARE - 67)) | (1L << (CIRCLE - 67)) | (1L << (TRIANGLE - 67)) | (1L << (SHAPE - 67)))) != 0)) {
				{
				setState(122);
				statementList();
				}
			}

			setState(125);
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
			setState(130); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(127);
				statement();
				setState(128);
				eos();
				}
				}
				setState(132); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SWITCH) | (1L << IF) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0) || ((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & ((1L << (RECT - 67)) | (1L << (SQUARE - 67)) | (1L << (CIRCLE - 67)) | (1L << (TRIANGLE - 67)) | (1L << (SHAPE - 67)))) != 0) );
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
			setState(139);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(134);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(135);
				simpleStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(136);
				block();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(137);
				ifStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(138);
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
			setState(143);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				expressionStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(142);
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
			setState(145);
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
			setState(147);
			type_();
			setState(148);
			match(L_PAREN);
			setState(149);
			arguments();
			setState(150);
			match(R_PAREN);
			setState(161);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(151);
				match(L_BRACKET);
				setState(152);
				match(SIZE);
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(153);
					match(COMMA);
					setState(155);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==WS) {
						{
						setState(154);
						match(WS);
						}
					}

					setState(157);
					match(SIZE);
					}
				}

				setState(160);
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
			setState(163);
			match(IDENTIFIER);
			setState(164);
			assign_op();
			setState(165);
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
			setState(167);
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
			setState(169);
			match(IF);
			setState(173);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(170);
				simpleStmt();
				setState(171);
				match(SEMI);
				}
				break;
			}
			setState(175);
			expression();
			setState(176);
			block();
			setState(182);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(177);
				match(ELSE);
				setState(180);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF:
					{
					setState(178);
					ifStmt();
					}
					break;
				case L_CURLY:
					{
					setState(179);
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
			setState(184);
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
			setState(186);
			match(SWITCH);
			setState(190);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(187);
				simpleStmt();
				setState(188);
				match(SEMI);
				}
				break;
			}
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (L_PAREN - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)) | (1L << (RECT - 10)) | (1L << (SQUARE - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)))) != 0)) {
				{
				setState(192);
				expression();
				}
			}

			setState(195);
			match(L_CURLY);
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(196);
				exprCaseClause();
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(202);
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
			setState(204);
			exprSwitchCase();
			setState(205);
			match(COLON);
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SWITCH) | (1L << IF) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0) || ((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & ((1L << (RECT - 67)) | (1L << (SQUARE - 67)) | (1L << (CIRCLE - 67)) | (1L << (TRIANGLE - 67)) | (1L << (SHAPE - 67)))) != 0)) {
				{
				setState(206);
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
			setState(212);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				match(CASE);
				setState(210);
				expression();
				}
				break;
			case DEFAULT:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
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
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RECT:
			case SQUARE:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(214);
				typeName();
				}
				break;
			case L_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(215);
				match(L_PAREN);
				setState(216);
				type_();
				setState(217);
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
			setState(221);
			_la = _input.LA(1);
			if ( !(((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & ((1L << (RECT - 67)) | (1L << (SQUARE - 67)) | (1L << (CIRCLE - 67)) | (1L << (TRIANGLE - 67)) | (1L << (SHAPE - 67)))) != 0)) ) {
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
			setState(223);
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
			setState(241);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				primaryExpr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				primaryExpr();
				setState(227);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LEFT) | (1L << RIGHT) | (1L << TOP) | (1L << BOT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(229);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==OUTER || _la==INNER) {
					{
					setState(228);
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

				setState(231);
				primaryExpr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(233);
				primaryExpr();
				setState(234);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ON) | (1L << UNDER) | (1L << IN))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(235);
				primaryExpr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(237);
				primaryExpr();
				setState(238);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(239);
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
			setState(243);
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
			setState(247);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NIL_LIT:
			case L_PAREN:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
			case RECT:
			case SQUARE:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(245);
				literal();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(246);
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
			setState(251);
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
				setState(249);
				basicLit();
				}
				break;
			case L_PAREN:
			case RECT:
			case SQUARE:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(250);
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
			setState(258);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				match(NIL_LIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(254);
				integer();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(255);
				string_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(256);
				match(FLOAT_LIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(257);
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
			setState(260);
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
			setState(262);
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
			setState(264);
			literalType();
			setState(265);
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
			setState(267);
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
			setState(269);
			match(L_CURLY);
			setState(271);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 10)) & ~0x3f) == 0 && ((1L << (_la - 10)) & ((1L << (NIL_LIT - 10)) | (1L << (IDENTIFIER - 10)) | (1L << (L_PAREN - 10)) | (1L << (L_CURLY - 10)) | (1L << (DECIMAL_LIT - 10)) | (1L << (FLOAT_LIT - 10)) | (1L << (RUNE_LIT - 10)) | (1L << (RAW_STRING_LIT - 10)) | (1L << (INTERPRETED_STRING_LIT - 10)) | (1L << (RECT - 10)) | (1L << (SQUARE - 10)) | (1L << (CIRCLE - 10)) | (1L << (TRIANGLE - 10)) | (1L << (SHAPE - 10)))) != 0)) {
				{
				setState(270);
				element();
				}
			}

			setState(273);
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
			setState(277);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NIL_LIT:
			case IDENTIFIER:
			case L_PAREN:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
			case RECT:
			case SQUARE:
			case CIRCLE:
			case TRIANGLE:
			case SHAPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(275);
				expression();
				}
				break;
			case L_CURLY:
				enterOuterAlt(_localctx, 2);
				{
				setState(276);
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
			setState(279);
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
			setState(281);
			match(L_PAREN);
			setState(282);
			match(SIZE);
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(283);
				match(COMMA);
				setState(285);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(284);
					match(WS);
					}
				}

				setState(287);
				match(SIZE);
				}
			}

			setState(290);
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
			setState(296);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(294);
				if (!(lineTerminatorAhead())) throw new FailedPredicateException(this, "lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(295);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I\u012d\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\3\2\3\2\7\2Q\n\2\f\2\16\2"+
		"T\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5b\n\5\f\5\16"+
		"\5e\13\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7o\n\7\f\7\16\7r\13\7\3\7\5"+
		"\7u\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t~\n\t\3\t\3\t\3\n\3\n\3\n\6\n\u0085"+
		"\n\n\r\n\16\n\u0086\3\13\3\13\3\13\3\13\3\13\5\13\u008e\n\13\3\f\3\f\5"+
		"\f\u0092\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u009e"+
		"\n\16\3\16\5\16\u00a1\n\16\3\16\5\16\u00a4\n\16\3\17\3\17\3\17\3\17\3"+
		"\20\3\20\3\21\3\21\3\21\3\21\5\21\u00b0\n\21\3\21\3\21\3\21\3\21\3\21"+
		"\5\21\u00b7\n\21\5\21\u00b9\n\21\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00c1"+
		"\n\23\3\23\5\23\u00c4\n\23\3\23\3\23\7\23\u00c8\n\23\f\23\16\23\u00cb"+
		"\13\23\3\23\3\23\3\24\3\24\3\24\5\24\u00d2\n\24\3\25\3\25\3\25\5\25\u00d7"+
		"\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00de\n\26\3\27\3\27\3\30\3\30\3\31"+
		"\3\31\3\31\3\31\5\31\u00e8\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\5\31\u00f4\n\31\3\32\3\32\3\33\3\33\5\33\u00fa\n\33\3\34\3"+
		"\34\5\34\u00fe\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u0105\n\35\3\36\3\36"+
		"\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\5\"\u0112\n\"\3\"\3\"\3#\3#\5#\u0118"+
		"\n#\3$\3$\3%\3%\3%\3%\5%\u0120\n%\3%\5%\u0123\n%\3%\3%\3&\3&\3&\3&\5&"+
		"\u012b\n&\3&\2\2\'\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60"+
		"\62\64\668:<>@BDFHJ\2\t\3\2EI\3\2\17\22\3\2\23\24\3\2\25\27\3\2\64\65"+
		"\4\299;;\3\2<=\2\u012f\2L\3\2\2\2\4U\3\2\2\2\6\\\3\2\2\2\b^\3\2\2\2\n"+
		"f\3\2\2\2\ft\3\2\2\2\16v\3\2\2\2\20{\3\2\2\2\22\u0084\3\2\2\2\24\u008d"+
		"\3\2\2\2\26\u0091\3\2\2\2\30\u0093\3\2\2\2\32\u0095\3\2\2\2\34\u00a5\3"+
		"\2\2\2\36\u00a9\3\2\2\2 \u00ab\3\2\2\2\"\u00ba\3\2\2\2$\u00bc\3\2\2\2"+
		"&\u00ce\3\2\2\2(\u00d6\3\2\2\2*\u00dd\3\2\2\2,\u00df\3\2\2\2.\u00e1\3"+
		"\2\2\2\60\u00f3\3\2\2\2\62\u00f5\3\2\2\2\64\u00f9\3\2\2\2\66\u00fd\3\2"+
		"\2\28\u0104\3\2\2\2:\u0106\3\2\2\2<\u0108\3\2\2\2>\u010a\3\2\2\2@\u010d"+
		"\3\2\2\2B\u010f\3\2\2\2D\u0117\3\2\2\2F\u0119\3\2\2\2H\u011b\3\2\2\2J"+
		"\u012a\3\2\2\2LR\5\4\3\2MN\5\6\4\2NO\5J&\2OQ\3\2\2\2PM\3\2\2\2QT\3\2\2"+
		"\2RP\3\2\2\2RS\3\2\2\2S\3\3\2\2\2TR\3\2\2\2UV\7B\2\2VW\7>\2\2WX\7C\2\2"+
		"XY\7>\2\2YZ\7C\2\2Z[\5J&\2[\5\3\2\2\2\\]\5\f\7\2]\7\3\2\2\2^c\7\r\2\2"+
		"_`\7\37\2\2`b\7\r\2\2a_\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\t\3\2\2"+
		"\2ec\3\2\2\2fg\7\16\2\2gh\7\r\2\2h\13\3\2\2\2iu\5\16\b\2jp\7\30\2\2kl"+
		"\5\16\b\2lm\5J&\2mo\3\2\2\2nk\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qs"+
		"\3\2\2\2rp\3\2\2\2su\7\31\2\2ti\3\2\2\2tj\3\2\2\2u\r\3\2\2\2vw\5*\26\2"+
		"wx\5\b\5\2xy\7\36\2\2yz\5\32\16\2z\17\3\2\2\2{}\7\32\2\2|~\5\22\n\2}|"+
		"\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080\7\33\2\2\u0080\21\3\2\2\2\u0081"+
		"\u0082\5\24\13\2\u0082\u0083\5J&\2\u0083\u0085\3\2\2\2\u0084\u0081\3\2"+
		"\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087"+
		"\23\3\2\2\2\u0088\u008e\5\6\4\2\u0089\u008e\5\26\f\2\u008a\u008e\5\20"+
		"\t\2\u008b\u008e\5 \21\2\u008c\u008e\5\"\22\2\u008d\u0088\3\2\2\2\u008d"+
		"\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2"+
		"\2\2\u008e\25\3\2\2\2\u008f\u0092\5\30\r\2\u0090\u0092\5\34\17\2\u0091"+
		"\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\27\3\2\2\2\u0093\u0094\5\60\31"+
		"\2\u0094\31\3\2\2\2\u0095\u0096\5*\26\2\u0096\u0097\7\30\2\2\u0097\u0098"+
		"\5H%\2\u0098\u00a3\7\31\2\2\u0099\u009a\7\34\2\2\u009a\u00a0\7D\2\2\u009b"+
		"\u009d\7\37\2\2\u009c\u009e\7>\2\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2"+
		"\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\7D\2\2\u00a0\u009b\3\2\2\2\u00a0"+
		"\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\7\35\2\2\u00a3\u0099\3"+
		"\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\33\3\2\2\2\u00a5\u00a6\7\r\2\2\u00a6"+
		"\u00a7\5\36\20\2\u00a7\u00a8\5\60\31\2\u00a8\35\3\2\2\2\u00a9\u00aa\7"+
		"\36\2\2\u00aa\37\3\2\2\2\u00ab\u00af\7\7\2\2\u00ac\u00ad\5\26\f\2\u00ad"+
		"\u00ae\7 \2\2\u00ae\u00b0\3\2\2\2\u00af\u00ac\3\2\2\2\u00af\u00b0\3\2"+
		"\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\5\60\31\2\u00b2\u00b8\5\20\t\2\u00b3"+
		"\u00b6\7\b\2\2\u00b4\u00b7\5 \21\2\u00b5\u00b7\5\20\t\2\u00b6\u00b4\3"+
		"\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8"+
		"\u00b9\3\2\2\2\u00b9!\3\2\2\2\u00ba\u00bb\5$\23\2\u00bb#\3\2\2\2\u00bc"+
		"\u00c0\7\4\2\2\u00bd\u00be\5\26\f\2\u00be\u00bf\7 \2\2\u00bf\u00c1\3\2"+
		"\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2"+
		"\u00c4\5\60\31\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3"+
		"\2\2\2\u00c5\u00c9\7\32\2\2\u00c6\u00c8\5&\24\2\u00c7\u00c6\3\2\2\2\u00c8"+
		"\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2"+
		"\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\7\33\2\2\u00cd%\3\2\2\2\u00ce\u00cf"+
		"\5(\25\2\u00cf\u00d1\7!\2\2\u00d0\u00d2\5\22\n\2\u00d1\u00d0\3\2\2\2\u00d1"+
		"\u00d2\3\2\2\2\u00d2\'\3\2\2\2\u00d3\u00d4\7\5\2\2\u00d4\u00d7\5\60\31"+
		"\2\u00d5\u00d7\7\6\2\2\u00d6\u00d3\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7)"+
		"\3\2\2\2\u00d8\u00de\5,\27\2\u00d9\u00da\7\30\2\2\u00da\u00db\5*\26\2"+
		"\u00db\u00dc\7\31\2\2\u00dc\u00de\3\2\2\2\u00dd\u00d8\3\2\2\2\u00dd\u00d9"+
		"\3\2\2\2\u00de+\3\2\2\2\u00df\u00e0\t\2\2\2\u00e0-\3\2\2\2\u00e1\u00e2"+
		"\5*\26\2\u00e2/\3\2\2\2\u00e3\u00f4\5\62\32\2\u00e4\u00e5\5\62\32\2\u00e5"+
		"\u00e7\t\3\2\2\u00e6\u00e8\t\4\2\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8\3\2"+
		"\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\5\62\32\2\u00ea\u00f4\3\2\2\2\u00eb"+
		"\u00ec\5\62\32\2\u00ec\u00ed\t\5\2\2\u00ed\u00ee\5\62\32\2\u00ee\u00f4"+
		"\3\2\2\2\u00ef\u00f0\5\62\32\2\u00f0\u00f1\t\6\2\2\u00f1\u00f2\5\62\32"+
		"\2\u00f2\u00f4\3\2\2\2\u00f3\u00e3\3\2\2\2\u00f3\u00e4\3\2\2\2\u00f3\u00eb"+
		"\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f4\61\3\2\2\2\u00f5\u00f6\5\64\33\2\u00f6"+
		"\63\3\2\2\2\u00f7\u00fa\5\66\34\2\u00f8\u00fa\5<\37\2\u00f9\u00f7\3\2"+
		"\2\2\u00f9\u00f8\3\2\2\2\u00fa\65\3\2\2\2\u00fb\u00fe\58\35\2\u00fc\u00fe"+
		"\5> \2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\67\3\2\2\2\u00ff"+
		"\u0105\7\f\2\2\u0100\u0105\5:\36\2\u0101\u0105\5F$\2\u0102\u0105\7:\2"+
		"\2\u0103\u0105\7;\2\2\u0104\u00ff\3\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101"+
		"\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u01059\3\2\2\2\u0106"+
		"\u0107\t\7\2\2\u0107;\3\2\2\2\u0108\u0109\7\r\2\2\u0109=\3\2\2\2\u010a"+
		"\u010b\5@!\2\u010b\u010c\5B\"\2\u010c?\3\2\2\2\u010d\u010e\5.\30\2\u010e"+
		"A\3\2\2\2\u010f\u0111\7\32\2\2\u0110\u0112\5D#\2\u0111\u0110\3\2\2\2\u0111"+
		"\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\7\33\2\2\u0114C\3\2\2\2"+
		"\u0115\u0118\5\60\31\2\u0116\u0118\5B\"\2\u0117\u0115\3\2\2\2\u0117\u0116"+
		"\3\2\2\2\u0118E\3\2\2\2\u0119\u011a\t\b\2\2\u011aG\3\2\2\2\u011b\u011c"+
		"\7\30\2\2\u011c\u0122\7D\2\2\u011d\u011f\7\37\2\2\u011e\u0120\7>\2\2\u011f"+
		"\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\7D"+
		"\2\2\u0122\u011d\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124"+
		"\u0125\7\31\2\2\u0125I\3\2\2\2\u0126\u012b\7 \2\2\u0127\u012b\7\2\2\3"+
		"\u0128\u012b\6&\2\2\u0129\u012b\6&\3\2\u012a\u0126\3\2\2\2\u012a\u0127"+
		"\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012bK\3\2\2\2 Rcpt}"+
		"\u0086\u008d\u0091\u009d\u00a0\u00a3\u00af\u00b6\u00b8\u00c0\u00c3\u00c9"+
		"\u00d1\u00d6\u00dd\u00e7\u00f3\u00f9\u00fd\u0104\u0111\u0117\u011f\u0122"+
		"\u012a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}