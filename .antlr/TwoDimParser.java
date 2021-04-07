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
		IMPORT=9, NIL_LIT=10, IDENTIFIER=11, DRAW=12, LEFT=13, RIGHT=14, TOP=15, 
		BOT=16, OUTER=17, INNER=18, ON=19, UNDER=20, IN=21, L_PAREN=22, R_PAREN=23, 
		L_CURLY=24, R_CURLY=25, L_BRACKET=26, R_BRACKET=27, ASSIGN=28, COMMA=29, 
		SEMI=30, COLON=31, DOT=32, PLUS_PLUS=33, MINUS_MINUS=34, LOGICAL_OR=35, 
		LOGICAL_AND=36, EQUALS=37, NOT_EQUALS=38, LESS=39, LESS_OR_EQUALS=40, 
		GREATER=41, GREATER_OR_EQUALS=42, OR=43, DIV=44, MOD=45, LSHIFT=46, RSHIFT=47, 
		BIT_CLEAR=48, EXCLAMATION=49, PLUS=50, MINUS=51, CARET=52, STAR=53, AMPERSAND=54, 
		DECIMAL_LIT=55, FLOAT_LIT=56, RUNE_LIT=57, RAW_STRING_LIT=58, INTERPRETED_STRING_LIT=59, 
		WS=60, COMMENT=61, TERMINATOR=62, LINE_COMMENT=63;
	public static final int
		RULE_sourceFile = 0, RULE_packageClause = 1, RULE_importDecl = 2, RULE_importSpec = 3, 
		RULE_importPath = 4, RULE_declaration = 5, RULE_identifierList = 6, RULE_expressionList = 7, 
		RULE_typeDecl = 8, RULE_typeSpec = 9, RULE_functionDecl = 10, RULE_methodDecl = 11, 
		RULE_receiver = 12, RULE_varDecl = 13, RULE_varSpec = 14, RULE_block = 15, 
		RULE_statementList = 16, RULE_statement = 17, RULE_simpleStmt = 18, RULE_expressionStmt = 19, 
		RULE_incDecStmt = 20, RULE_assignment = 21, RULE_assign_op = 22, RULE_emptyStmt = 23, 
		RULE_labeledStmt = 24, RULE_ifStmt = 25, RULE_switchStmt = 26, RULE_exprSwitchStmt = 27, 
		RULE_exprCaseClause = 28, RULE_exprSwitchCase = 29, RULE_typeSwitchStmt = 30, 
		RULE_typeSwitchGuard = 31, RULE_typeCaseClause = 32, RULE_typeSwitchCase = 33, 
		RULE_typeList = 34, RULE_recvStmt = 35, RULE_type_ = 36, RULE_typeName = 37, 
		RULE_typeLit = 38, RULE_elementType = 39, RULE_methodSpec = 40, RULE_functionType = 41, 
		RULE_signature = 42, RULE_result = 43, RULE_parameters = 44, RULE_parameterDecl = 45, 
		RULE_expression = 46, RULE_primaryExpr = 47, RULE_unaryExpr = 48, RULE_conversion = 49, 
		RULE_operand = 50, RULE_literal = 51, RULE_basicLit = 52, RULE_integer = 53, 
		RULE_operandName = 54, RULE_qualifiedIdent = 55, RULE_compositeLit = 56, 
		RULE_literalType = 57, RULE_literalValue = 58, RULE_elementList = 59, 
		RULE_keyedElement = 60, RULE_key = 61, RULE_element = 62, RULE_fieldDecl = 63, 
		RULE_string_ = 64, RULE_anonymousField = 65, RULE_functionLit = 66, RULE_index = 67, 
		RULE_typeAssertion = 68, RULE_arguments = 69, RULE_methodExpr = 70, RULE_receiverType = 71, 
		RULE_eos = 72;
	private static String[] makeRuleNames() {
		return new String[] {
			"sourceFile", "packageClause", "importDecl", "importSpec", "importPath", 
			"declaration", "identifierList", "expressionList", "typeDecl", "typeSpec", 
			"functionDecl", "methodDecl", "receiver", "varDecl", "varSpec", "block", 
			"statementList", "statement", "simpleStmt", "expressionStmt", "incDecStmt", 
			"assignment", "assign_op", "emptyStmt", "labeledStmt", "ifStmt", "switchStmt", 
			"exprSwitchStmt", "exprCaseClause", "exprSwitchCase", "typeSwitchStmt", 
			"typeSwitchGuard", "typeCaseClause", "typeSwitchCase", "typeList", "recvStmt", 
			"type_", "typeName", "typeLit", "elementType", "methodSpec", "functionType", 
			"signature", "result", "parameters", "parameterDecl", "expression", "primaryExpr", 
			"unaryExpr", "conversion", "operand", "literal", "basicLit", "integer", 
			"operandName", "qualifiedIdent", "compositeLit", "literalType", "literalValue", 
			"elementList", "keyedElement", "key", "element", "fieldDecl", "string_", 
			"anonymousField", "functionLit", "index", "typeAssertion", "arguments", 
			"methodExpr", "receiverType", "eos"
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
			"LINE_COMMENT"
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
		public PackageClauseContext packageClause() {
			return getRuleContext(PackageClauseContext.class,0);
		}
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
		}
		public List<ImportDeclContext> importDecl() {
			return getRuleContexts(ImportDeclContext.class);
		}
		public ImportDeclContext importDecl(int i) {
			return getRuleContext(ImportDeclContext.class,i);
		}
		public List<FunctionDeclContext> functionDecl() {
			return getRuleContexts(FunctionDeclContext.class);
		}
		public FunctionDeclContext functionDecl(int i) {
			return getRuleContext(FunctionDeclContext.class,i);
		}
		public List<MethodDeclContext> methodDecl() {
			return getRuleContexts(MethodDeclContext.class);
		}
		public MethodDeclContext methodDecl(int i) {
			return getRuleContext(MethodDeclContext.class,i);
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
			setState(146);
			packageClause();
			setState(147);
			eos();
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IMPORT) {
				{
				{
				setState(148);
				importDecl();
				setState(149);
				eos();
				}
				}
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << TYPE) | (1L << IDENTIFIER) | (1L << L_PAREN))) != 0)) {
				{
				{
				setState(159);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(156);
					functionDecl();
					}
					break;
				case 2:
					{
					setState(157);
					methodDecl();
					}
					break;
				case 3:
					{
					setState(158);
					declaration();
					}
					break;
				}
				setState(161);
				eos();
				}
				}
				setState(167);
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

	public static class PackageClauseContext extends ParserRuleContext {
		public TerminalNode PACKAGE() { return getToken(TwoDimParser.PACKAGE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public PackageClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_packageClause; }
	}

	public final PackageClauseContext packageClause() throws RecognitionException {
		PackageClauseContext _localctx = new PackageClauseContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_packageClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(PACKAGE);
			setState(169);
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

	public static class ImportDeclContext extends ParserRuleContext {
		public TerminalNode IMPORT() { return getToken(TwoDimParser.IMPORT, 0); }
		public List<ImportSpecContext> importSpec() {
			return getRuleContexts(ImportSpecContext.class);
		}
		public ImportSpecContext importSpec(int i) {
			return getRuleContext(ImportSpecContext.class,i);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
		}
		public ImportDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importDecl; }
	}

	public final ImportDeclContext importDecl() throws RecognitionException {
		ImportDeclContext _localctx = new ImportDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_importDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(IMPORT);
			setState(183);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
			case DOT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				{
				setState(172);
				importSpec();
				}
				break;
			case L_PAREN:
				{
				setState(173);
				match(L_PAREN);
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IDENTIFIER) | (1L << DOT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
					{
					{
					setState(174);
					importSpec();
					setState(175);
					eos();
					}
					}
					setState(181);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(182);
				match(R_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ImportSpecContext extends ParserRuleContext {
		public ImportPathContext importPath() {
			return getRuleContext(ImportPathContext.class,0);
		}
		public TerminalNode DOT() { return getToken(TwoDimParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public ImportSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importSpec; }
	}

	public final ImportSpecContext importSpec() throws RecognitionException {
		ImportSpecContext _localctx = new ImportSpecContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_importSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER || _la==DOT) {
				{
				setState(185);
				_la = _input.LA(1);
				if ( !(_la==IDENTIFIER || _la==DOT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(188);
			importPath();
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

	public static class ImportPathContext extends ParserRuleContext {
		public String_Context string_() {
			return getRuleContext(String_Context.class,0);
		}
		public ImportPathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importPath; }
	}

	public final ImportPathContext importPath() throws RecognitionException {
		ImportPathContext _localctx = new ImportPathContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_importPath);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			string_();
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
		public TypeDeclContext typeDecl() {
			return getRuleContext(TypeDeclContext.class,0);
		}
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
		enterRule(_localctx, 10, RULE_declaration);
		try {
			setState(194);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(192);
				typeDecl();
				}
				break;
			case FUNC:
			case IDENTIFIER:
			case L_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(193);
				varDecl();
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
		enterRule(_localctx, 12, RULE_identifierList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(IDENTIFIER);
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(197);
				match(COMMA);
				setState(198);
				match(IDENTIFIER);
				}
				}
				setState(203);
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
		enterRule(_localctx, 14, RULE_expressionList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			expression(0);
			setState(209);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(205);
					match(COMMA);
					setState(206);
					expression(0);
					}
					} 
				}
				setState(211);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
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

	public static class TypeDeclContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(TwoDimParser.TYPE, 0); }
		public List<TypeSpecContext> typeSpec() {
			return getRuleContexts(TypeSpecContext.class);
		}
		public TypeSpecContext typeSpec(int i) {
			return getRuleContext(TypeSpecContext.class,i);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public List<EosContext> eos() {
			return getRuleContexts(EosContext.class);
		}
		public EosContext eos(int i) {
			return getRuleContext(EosContext.class,i);
		}
		public TypeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeDecl; }
	}

	public final TypeDeclContext typeDecl() throws RecognitionException {
		TypeDeclContext _localctx = new TypeDeclContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_typeDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(TYPE);
			setState(224);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(213);
				typeSpec();
				}
				break;
			case L_PAREN:
				{
				setState(214);
				match(L_PAREN);
				setState(220);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==IDENTIFIER) {
					{
					{
					setState(215);
					typeSpec();
					setState(216);
					eos();
					}
					}
					setState(222);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(223);
				match(R_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class TypeSpecContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(TwoDimParser.ASSIGN, 0); }
		public TypeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSpec; }
	}

	public final TypeSpecContext typeSpec() throws RecognitionException {
		TypeSpecContext _localctx = new TypeSpecContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_typeSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			match(IDENTIFIER);
			setState(228);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(227);
				match(ASSIGN);
				}
			}

			setState(230);
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
		enterRule(_localctx, 20, RULE_functionDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(FUNC);
			setState(233);
			match(IDENTIFIER);
			{
			setState(234);
			signature();
			setState(236);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(235);
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

	public static class MethodDeclContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(TwoDimParser.FUNC, 0); }
		public ReceiverContext receiver() {
			return getRuleContext(ReceiverContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public MethodDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDecl; }
	}

	public final MethodDeclContext methodDecl() throws RecognitionException {
		MethodDeclContext _localctx = new MethodDeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_methodDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(FUNC);
			setState(239);
			receiver();
			setState(240);
			match(IDENTIFIER);
			{
			setState(241);
			signature();
			setState(243);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(242);
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

	public static class ReceiverContext extends ParserRuleContext {
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public ReceiverContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_receiver; }
	}

	public final ReceiverContext receiver() throws RecognitionException {
		ReceiverContext _localctx = new ReceiverContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_receiver);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			parameters();
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
		enterRule(_localctx, 26, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(247);
				varSpec();
				}
				break;
			case 2:
				{
				setState(248);
				match(L_PAREN);
				setState(254);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << IDENTIFIER) | (1L << L_PAREN))) != 0)) {
					{
					{
					setState(249);
					varSpec();
					setState(250);
					eos();
					}
					}
					setState(256);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(257);
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
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public VarSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varSpec; }
	}

	public final VarSpecContext varSpec() throws RecognitionException {
		VarSpecContext _localctx = new VarSpecContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_varSpec);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			type_();
			setState(261);
			identifierList();
			setState(262);
			match(ASSIGN);
			setState(263);
			expressionList();
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
		enterRule(_localctx, 30, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			match(L_CURLY);
			setState(267);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << SWITCH) | (1L << IF) | (1L << TYPE) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << L_BRACKET) | (1L << SEMI) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
				{
				setState(266);
				statementList();
				}
			}

			setState(269);
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
		enterRule(_localctx, 32, RULE_statementList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(271);
				statement();
				setState(272);
				eos();
				}
				}
				setState(276); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << SWITCH) | (1L << IF) | (1L << TYPE) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << L_BRACKET) | (1L << SEMI) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0) );
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
		public LabeledStmtContext labeledStmt() {
			return getRuleContext(LabeledStmtContext.class,0);
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
		enterRule(_localctx, 34, RULE_statement);
		try {
			setState(284);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(278);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
				labeledStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(280);
				simpleStmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(281);
				block();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(282);
				ifStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(283);
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
		public IncDecStmtContext incDecStmt() {
			return getRuleContext(IncDecStmtContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public EmptyStmtContext emptyStmt() {
			return getRuleContext(EmptyStmtContext.class,0);
		}
		public SimpleStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStmt; }
	}

	public final SimpleStmtContext simpleStmt() throws RecognitionException {
		SimpleStmtContext _localctx = new SimpleStmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_simpleStmt);
		try {
			setState(290);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				expressionStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(287);
				incDecStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(288);
				assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(289);
				emptyStmt();
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
		enterRule(_localctx, 38, RULE_expressionStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			expression(0);
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

	public static class IncDecStmtContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PLUS_PLUS() { return getToken(TwoDimParser.PLUS_PLUS, 0); }
		public TerminalNode MINUS_MINUS() { return getToken(TwoDimParser.MINUS_MINUS, 0); }
		public IncDecStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incDecStmt; }
	}

	public final IncDecStmtContext incDecStmt() throws RecognitionException {
		IncDecStmtContext _localctx = new IncDecStmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_incDecStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			expression(0);
			setState(295);
			_la = _input.LA(1);
			if ( !(_la==PLUS_PLUS || _la==MINUS_MINUS) ) {
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

	public static class AssignmentContext extends ParserRuleContext {
		public List<ExpressionListContext> expressionList() {
			return getRuleContexts(ExpressionListContext.class);
		}
		public ExpressionListContext expressionList(int i) {
			return getRuleContext(ExpressionListContext.class,i);
		}
		public Assign_opContext assign_op() {
			return getRuleContext(Assign_opContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			expressionList();
			setState(298);
			assign_op();
			setState(299);
			expressionList();
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
		public TerminalNode PLUS() { return getToken(TwoDimParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(TwoDimParser.MINUS, 0); }
		public Assign_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_op; }
	}

	public final Assign_opContext assign_op() throws RecognitionException {
		Assign_opContext _localctx = new Assign_opContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_assign_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PLUS || _la==MINUS) {
				{
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
				}
			}

			setState(304);
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

	public static class EmptyStmtContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(TwoDimParser.SEMI, 0); }
		public EmptyStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emptyStmt; }
	}

	public final EmptyStmtContext emptyStmt() throws RecognitionException {
		EmptyStmtContext _localctx = new EmptyStmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_emptyStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			match(SEMI);
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

	public static class LabeledStmtContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public TerminalNode COLON() { return getToken(TwoDimParser.COLON, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public LabeledStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_labeledStmt; }
	}

	public final LabeledStmtContext labeledStmt() throws RecognitionException {
		LabeledStmtContext _localctx = new LabeledStmtContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_labeledStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			match(IDENTIFIER);
			setState(309);
			match(COLON);
			setState(310);
			statement();
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
		enterRule(_localctx, 50, RULE_ifStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			match(IF);
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(313);
				simpleStmt();
				setState(314);
				match(SEMI);
				}
				break;
			}
			setState(318);
			expression(0);
			setState(319);
			block();
			setState(325);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				setState(320);
				match(ELSE);
				setState(323);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case IF:
					{
					setState(321);
					ifStmt();
					}
					break;
				case L_CURLY:
					{
					setState(322);
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
		public TypeSwitchStmtContext typeSwitchStmt() {
			return getRuleContext(TypeSwitchStmtContext.class,0);
		}
		public SwitchStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStmt; }
	}

	public final SwitchStmtContext switchStmt() throws RecognitionException {
		SwitchStmtContext _localctx = new SwitchStmtContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_switchStmt);
		try {
			setState(329);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(327);
				exprSwitchStmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(328);
				typeSwitchStmt();
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
		enterRule(_localctx, 54, RULE_exprSwitchStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(331);
			match(SWITCH);
			setState(335);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(332);
				simpleStmt();
				setState(333);
				match(SEMI);
				}
				break;
			}
			setState(338);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_BRACKET) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
				{
				setState(337);
				expression(0);
				}
			}

			setState(340);
			match(L_CURLY);
			setState(344);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(341);
				exprCaseClause();
				}
				}
				setState(346);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(347);
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
		enterRule(_localctx, 56, RULE_exprCaseClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			exprSwitchCase();
			setState(350);
			match(COLON);
			setState(352);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << SWITCH) | (1L << IF) | (1L << TYPE) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << L_BRACKET) | (1L << SEMI) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
				{
				setState(351);
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
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode DEFAULT() { return getToken(TwoDimParser.DEFAULT, 0); }
		public ExprSwitchCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprSwitchCase; }
	}

	public final ExprSwitchCaseContext exprSwitchCase() throws RecognitionException {
		ExprSwitchCaseContext _localctx = new ExprSwitchCaseContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_exprSwitchCase);
		try {
			setState(357);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(354);
				match(CASE);
				setState(355);
				expressionList();
				}
				break;
			case DEFAULT:
				enterOuterAlt(_localctx, 2);
				{
				setState(356);
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

	public static class TypeSwitchStmtContext extends ParserRuleContext {
		public TerminalNode SWITCH() { return getToken(TwoDimParser.SWITCH, 0); }
		public TypeSwitchGuardContext typeSwitchGuard() {
			return getRuleContext(TypeSwitchGuardContext.class,0);
		}
		public TerminalNode L_CURLY() { return getToken(TwoDimParser.L_CURLY, 0); }
		public TerminalNode R_CURLY() { return getToken(TwoDimParser.R_CURLY, 0); }
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(TwoDimParser.SEMI, 0); }
		public List<TypeCaseClauseContext> typeCaseClause() {
			return getRuleContexts(TypeCaseClauseContext.class);
		}
		public TypeCaseClauseContext typeCaseClause(int i) {
			return getRuleContext(TypeCaseClauseContext.class,i);
		}
		public TypeSwitchStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSwitchStmt; }
	}

	public final TypeSwitchStmtContext typeSwitchStmt() throws RecognitionException {
		TypeSwitchStmtContext _localctx = new TypeSwitchStmtContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_typeSwitchStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(SWITCH);
			setState(363);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				{
				setState(360);
				simpleStmt();
				setState(361);
				match(SEMI);
				}
				break;
			}
			setState(365);
			typeSwitchGuard();
			setState(366);
			match(L_CURLY);
			setState(370);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE || _la==DEFAULT) {
				{
				{
				setState(367);
				typeCaseClause();
				}
				}
				setState(372);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(373);
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

	public static class TypeSwitchGuardContext extends ParserRuleContext {
		public PrimaryExprContext primaryExpr() {
			return getRuleContext(PrimaryExprContext.class,0);
		}
		public TerminalNode DOT() { return getToken(TwoDimParser.DOT, 0); }
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode TYPE() { return getToken(TwoDimParser.TYPE, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public TypeSwitchGuardContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSwitchGuard; }
	}

	public final TypeSwitchGuardContext typeSwitchGuard() throws RecognitionException {
		TypeSwitchGuardContext _localctx = new TypeSwitchGuardContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_typeSwitchGuard);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			primaryExpr(0);
			setState(376);
			match(DOT);
			setState(377);
			match(L_PAREN);
			setState(378);
			match(TYPE);
			setState(379);
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

	public static class TypeCaseClauseContext extends ParserRuleContext {
		public TypeSwitchCaseContext typeSwitchCase() {
			return getRuleContext(TypeSwitchCaseContext.class,0);
		}
		public TerminalNode COLON() { return getToken(TwoDimParser.COLON, 0); }
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public TypeCaseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeCaseClause; }
	}

	public final TypeCaseClauseContext typeCaseClause() throws RecognitionException {
		TypeCaseClauseContext _localctx = new TypeCaseClauseContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_typeCaseClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(381);
			typeSwitchCase();
			setState(382);
			match(COLON);
			setState(384);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << SWITCH) | (1L << IF) | (1L << TYPE) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << L_BRACKET) | (1L << SEMI) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
				{
				setState(383);
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

	public static class TypeSwitchCaseContext extends ParserRuleContext {
		public TerminalNode CASE() { return getToken(TwoDimParser.CASE, 0); }
		public TypeListContext typeList() {
			return getRuleContext(TypeListContext.class,0);
		}
		public TerminalNode DEFAULT() { return getToken(TwoDimParser.DEFAULT, 0); }
		public TypeSwitchCaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSwitchCase; }
	}

	public final TypeSwitchCaseContext typeSwitchCase() throws RecognitionException {
		TypeSwitchCaseContext _localctx = new TypeSwitchCaseContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_typeSwitchCase);
		try {
			setState(389);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(386);
				match(CASE);
				setState(387);
				typeList();
				}
				break;
			case DEFAULT:
				enterOuterAlt(_localctx, 2);
				{
				setState(388);
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

	public static class TypeListContext extends ParserRuleContext {
		public List<Type_Context> type_() {
			return getRuleContexts(Type_Context.class);
		}
		public Type_Context type_(int i) {
			return getRuleContext(Type_Context.class,i);
		}
		public List<TerminalNode> NIL_LIT() { return getTokens(TwoDimParser.NIL_LIT); }
		public TerminalNode NIL_LIT(int i) {
			return getToken(TwoDimParser.NIL_LIT, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public TypeListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeList; }
	}

	public final TypeListContext typeList() throws RecognitionException {
		TypeListContext _localctx = new TypeListContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_typeList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(393);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
			case IDENTIFIER:
			case L_PAREN:
				{
				setState(391);
				type_();
				}
				break;
			case NIL_LIT:
				{
				setState(392);
				match(NIL_LIT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(402);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(395);
				match(COMMA);
				setState(398);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case FUNC:
				case IDENTIFIER:
				case L_PAREN:
					{
					setState(396);
					type_();
					}
					break;
				case NIL_LIT:
					{
					setState(397);
					match(NIL_LIT);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(404);
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

	public static class RecvStmtContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(TwoDimParser.ASSIGN, 0); }
		public RecvStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recvStmt; }
	}

	public final RecvStmtContext recvStmt() throws RecognitionException {
		RecvStmtContext _localctx = new RecvStmtContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_recvStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(408);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(405);
				expressionList();
				setState(406);
				match(ASSIGN);
				}
				break;
			}
			setState(410);
			expression(0);
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
		public TypeLitContext typeLit() {
			return getRuleContext(TypeLitContext.class,0);
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
		enterRule(_localctx, 72, RULE_type_);
		try {
			setState(418);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(412);
				typeName();
				}
				break;
			case FUNC:
				enterOuterAlt(_localctx, 2);
				{
				setState(413);
				typeLit();
				}
				break;
			case L_PAREN:
				enterOuterAlt(_localctx, 3);
				{
				setState(414);
				match(L_PAREN);
				setState(415);
				type_();
				setState(416);
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
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public QualifiedIdentContext qualifiedIdent() {
			return getRuleContext(QualifiedIdentContext.class,0);
		}
		public TypeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeName; }
	}

	public final TypeNameContext typeName() throws RecognitionException {
		TypeNameContext _localctx = new TypeNameContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_typeName);
		try {
			setState(422);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(420);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(421);
				qualifiedIdent();
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

	public static class TypeLitContext extends ParserRuleContext {
		public FunctionTypeContext functionType() {
			return getRuleContext(FunctionTypeContext.class,0);
		}
		public TypeLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeLit; }
	}

	public final TypeLitContext typeLit() throws RecognitionException {
		TypeLitContext _localctx = new TypeLitContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_typeLit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			functionType();
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
		enterRule(_localctx, 78, RULE_elementType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(426);
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

	public static class MethodSpecContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public ResultContext result() {
			return getRuleContext(ResultContext.class,0);
		}
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public MethodSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodSpec; }
	}

	public final MethodSpecContext methodSpec() throws RecognitionException {
		MethodSpecContext _localctx = new MethodSpecContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_methodSpec);
		try {
			setState(436);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(428);
				if (!(noTerminatorAfterParams(2))) throw new FailedPredicateException(this, "noTerminatorAfterParams(2)");
				setState(429);
				match(IDENTIFIER);
				setState(430);
				parameters();
				setState(431);
				result();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(433);
				typeName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(434);
				match(IDENTIFIER);
				setState(435);
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

	public static class FunctionTypeContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(TwoDimParser.FUNC, 0); }
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public FunctionTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionType; }
	}

	public final FunctionTypeContext functionType() throws RecognitionException {
		FunctionTypeContext _localctx = new FunctionTypeContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_functionType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
			match(FUNC);
			setState(439);
			signature();
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
		public ResultContext result() {
			return getRuleContext(ResultContext.class,0);
		}
		public SignatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signature; }
	}

	public final SignatureContext signature() throws RecognitionException {
		SignatureContext _localctx = new SignatureContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_signature);
		try {
			setState(446);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(441);
				if (!(noTerminatorAfterParams(1))) throw new FailedPredicateException(this, "noTerminatorAfterParams(1)");
				setState(442);
				parameters();
				setState(443);
				result();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(445);
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

	public static class ResultContext extends ParserRuleContext {
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public ResultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_result; }
	}

	public final ResultContext result() throws RecognitionException {
		ResultContext _localctx = new ResultContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_result);
		try {
			setState(450);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(448);
				parameters();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(449);
				type_();
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
		enterRule(_localctx, 88, RULE_parameters);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(452);
			match(L_PAREN);
			setState(464);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << IDENTIFIER) | (1L << L_PAREN))) != 0)) {
				{
				setState(453);
				parameterDecl();
				setState(458);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(454);
						match(COMMA);
						setState(455);
						parameterDecl();
						}
						} 
					}
					setState(460);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
				}
				setState(462);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(461);
					match(COMMA);
					}
				}

				}
			}

			setState(466);
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
		enterRule(_localctx, 90, RULE_parameterDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(469);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				{
				setState(468);
				identifierList();
				}
				break;
			}
			setState(471);
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
		public PrimaryExprContext primaryExpr() {
			return getRuleContext(PrimaryExprContext.class,0);
		}
		public UnaryExprContext unaryExpr() {
			return getRuleContext(UnaryExprContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode STAR() { return getToken(TwoDimParser.STAR, 0); }
		public TerminalNode DIV() { return getToken(TwoDimParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(TwoDimParser.MOD, 0); }
		public TerminalNode LSHIFT() { return getToken(TwoDimParser.LSHIFT, 0); }
		public TerminalNode RSHIFT() { return getToken(TwoDimParser.RSHIFT, 0); }
		public TerminalNode AMPERSAND() { return getToken(TwoDimParser.AMPERSAND, 0); }
		public TerminalNode BIT_CLEAR() { return getToken(TwoDimParser.BIT_CLEAR, 0); }
		public TerminalNode PLUS() { return getToken(TwoDimParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(TwoDimParser.MINUS, 0); }
		public TerminalNode OR() { return getToken(TwoDimParser.OR, 0); }
		public TerminalNode CARET() { return getToken(TwoDimParser.CARET, 0); }
		public TerminalNode EQUALS() { return getToken(TwoDimParser.EQUALS, 0); }
		public TerminalNode NOT_EQUALS() { return getToken(TwoDimParser.NOT_EQUALS, 0); }
		public TerminalNode LESS() { return getToken(TwoDimParser.LESS, 0); }
		public TerminalNode LESS_OR_EQUALS() { return getToken(TwoDimParser.LESS_OR_EQUALS, 0); }
		public TerminalNode GREATER() { return getToken(TwoDimParser.GREATER, 0); }
		public TerminalNode GREATER_OR_EQUALS() { return getToken(TwoDimParser.GREATER_OR_EQUALS, 0); }
		public TerminalNode LOGICAL_AND() { return getToken(TwoDimParser.LOGICAL_AND, 0); }
		public TerminalNode LOGICAL_OR() { return getToken(TwoDimParser.LOGICAL_OR, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 92;
		enterRecursionRule(_localctx, 92, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(476);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				{
				setState(474);
				primaryExpr(0);
				}
				break;
			case 2:
				{
				setState(475);
				unaryExpr();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(495);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,49,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(493);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(478);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(479);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DIV) | (1L << MOD) | (1L << LSHIFT) | (1L << RSHIFT) | (1L << BIT_CLEAR) | (1L << STAR) | (1L << AMPERSAND))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(480);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(481);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(482);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << OR) | (1L << PLUS) | (1L << MINUS) | (1L << CARET))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(483);
						expression(5);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(484);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(485);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUALS) | (1L << NOT_EQUALS) | (1L << LESS) | (1L << LESS_OR_EQUALS) | (1L << GREATER) | (1L << GREATER_OR_EQUALS))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(486);
						expression(4);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(487);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(488);
						match(LOGICAL_AND);
						setState(489);
						expression(3);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(490);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(491);
						match(LOGICAL_OR);
						setState(492);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(497);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,49,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PrimaryExprContext extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public ConversionContext conversion() {
			return getRuleContext(ConversionContext.class,0);
		}
		public PrimaryExprContext primaryExpr() {
			return getRuleContext(PrimaryExprContext.class,0);
		}
		public TerminalNode DOT() { return getToken(TwoDimParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public IndexContext index() {
			return getRuleContext(IndexContext.class,0);
		}
		public TypeAssertionContext typeAssertion() {
			return getRuleContext(TypeAssertionContext.class,0);
		}
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public PrimaryExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpr; }
	}

	public final PrimaryExprContext primaryExpr() throws RecognitionException {
		return primaryExpr(0);
	}

	private PrimaryExprContext primaryExpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PrimaryExprContext _localctx = new PrimaryExprContext(_ctx, _parentState);
		PrimaryExprContext _prevctx = _localctx;
		int _startState = 94;
		enterRecursionRule(_localctx, 94, RULE_primaryExpr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(501);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				{
				setState(499);
				operand();
				}
				break;
			case 2:
				{
				setState(500);
				conversion();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(513);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,52,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PrimaryExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_primaryExpr);
					setState(503);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(509);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
					case 1:
						{
						setState(504);
						match(DOT);
						setState(505);
						match(IDENTIFIER);
						}
						break;
					case 2:
						{
						setState(506);
						index();
						}
						break;
					case 3:
						{
						setState(507);
						typeAssertion();
						}
						break;
					case 4:
						{
						setState(508);
						arguments();
						}
						break;
					}
					}
					} 
				}
				setState(515);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,52,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class UnaryExprContext extends ParserRuleContext {
		public PrimaryExprContext primaryExpr() {
			return getRuleContext(PrimaryExprContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(TwoDimParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(TwoDimParser.MINUS, 0); }
		public TerminalNode EXCLAMATION() { return getToken(TwoDimParser.EXCLAMATION, 0); }
		public TerminalNode CARET() { return getToken(TwoDimParser.CARET, 0); }
		public TerminalNode STAR() { return getToken(TwoDimParser.STAR, 0); }
		public TerminalNode AMPERSAND() { return getToken(TwoDimParser.AMPERSAND, 0); }
		public UnaryExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpr; }
	}

	public final UnaryExprContext unaryExpr() throws RecognitionException {
		UnaryExprContext _localctx = new UnaryExprContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_unaryExpr);
		int _la;
		try {
			setState(519);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
			case NIL_LIT:
			case IDENTIFIER:
			case L_PAREN:
			case L_BRACKET:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(516);
				primaryExpr(0);
				}
				break;
			case EXCLAMATION:
			case PLUS:
			case MINUS:
			case CARET:
			case STAR:
			case AMPERSAND:
				enterOuterAlt(_localctx, 2);
				{
				setState(517);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(518);
				expression(0);
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

	public static class ConversionContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public TerminalNode COMMA() { return getToken(TwoDimParser.COMMA, 0); }
		public ConversionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conversion; }
	}

	public final ConversionContext conversion() throws RecognitionException {
		ConversionContext _localctx = new ConversionContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_conversion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(521);
			type_();
			setState(522);
			match(L_PAREN);
			setState(523);
			expression(0);
			setState(525);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(524);
				match(COMMA);
				}
			}

			setState(527);
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

	public static class OperandContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public OperandNameContext operandName() {
			return getRuleContext(OperandNameContext.class,0);
		}
		public MethodExprContext methodExpr() {
			return getRuleContext(MethodExprContext.class,0);
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
		enterRule(_localctx, 100, RULE_operand);
		try {
			setState(536);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(529);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(530);
				operandName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(531);
				methodExpr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(532);
				match(L_PAREN);
				setState(533);
				expression(0);
				setState(534);
				match(R_PAREN);
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

	public static class LiteralContext extends ParserRuleContext {
		public BasicLitContext basicLit() {
			return getRuleContext(BasicLitContext.class,0);
		}
		public CompositeLitContext compositeLit() {
			return getRuleContext(CompositeLitContext.class,0);
		}
		public FunctionLitContext functionLit() {
			return getRuleContext(FunctionLitContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_literal);
		try {
			setState(541);
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
				setState(538);
				basicLit();
				}
				break;
			case IDENTIFIER:
			case L_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(539);
				compositeLit();
				}
				break;
			case FUNC:
				enterOuterAlt(_localctx, 3);
				{
				setState(540);
				functionLit();
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
		enterRule(_localctx, 104, RULE_basicLit);
		try {
			setState(548);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,57,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(543);
				match(NIL_LIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(544);
				integer();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(545);
				string_();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(546);
				match(FLOAT_LIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(547);
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
		enterRule(_localctx, 106, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(550);
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
		public QualifiedIdentContext qualifiedIdent() {
			return getRuleContext(QualifiedIdentContext.class,0);
		}
		public OperandNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operandName; }
	}

	public final OperandNameContext operandName() throws RecognitionException {
		OperandNameContext _localctx = new OperandNameContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_operandName);
		try {
			setState(554);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,58,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(552);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(553);
				qualifiedIdent();
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

	public static class QualifiedIdentContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(TwoDimParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(TwoDimParser.IDENTIFIER, i);
		}
		public TerminalNode DOT() { return getToken(TwoDimParser.DOT, 0); }
		public QualifiedIdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifiedIdent; }
	}

	public final QualifiedIdentContext qualifiedIdent() throws RecognitionException {
		QualifiedIdentContext _localctx = new QualifiedIdentContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_qualifiedIdent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			match(IDENTIFIER);
			setState(557);
			match(DOT);
			setState(558);
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
		enterRule(_localctx, 112, RULE_compositeLit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(560);
			literalType();
			setState(561);
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
		public TerminalNode L_BRACKET() { return getToken(TwoDimParser.L_BRACKET, 0); }
		public TerminalNode R_BRACKET() { return getToken(TwoDimParser.R_BRACKET, 0); }
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
		enterRule(_localctx, 114, RULE_literalType);
		try {
			setState(567);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case L_BRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(563);
				match(L_BRACKET);
				setState(564);
				match(R_BRACKET);
				setState(565);
				elementType();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(566);
				typeName();
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

	public static class LiteralValueContext extends ParserRuleContext {
		public TerminalNode L_CURLY() { return getToken(TwoDimParser.L_CURLY, 0); }
		public TerminalNode R_CURLY() { return getToken(TwoDimParser.R_CURLY, 0); }
		public ElementListContext elementList() {
			return getRuleContext(ElementListContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(TwoDimParser.COMMA, 0); }
		public LiteralValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalValue; }
	}

	public final LiteralValueContext literalValue() throws RecognitionException {
		LiteralValueContext _localctx = new LiteralValueContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_literalValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(569);
			match(L_CURLY);
			setState(574);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_CURLY) | (1L << L_BRACKET) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
				{
				setState(570);
				elementList();
				setState(572);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(571);
					match(COMMA);
					}
				}

				}
			}

			setState(576);
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

	public static class ElementListContext extends ParserRuleContext {
		public List<KeyedElementContext> keyedElement() {
			return getRuleContexts(KeyedElementContext.class);
		}
		public KeyedElementContext keyedElement(int i) {
			return getRuleContext(KeyedElementContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public ElementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementList; }
	}

	public final ElementListContext elementList() throws RecognitionException {
		ElementListContext _localctx = new ElementListContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_elementList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(578);
			keyedElement();
			setState(583);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,62,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(579);
					match(COMMA);
					setState(580);
					keyedElement();
					}
					} 
				}
				setState(585);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,62,_ctx);
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

	public static class KeyedElementContext extends ParserRuleContext {
		public ElementContext element() {
			return getRuleContext(ElementContext.class,0);
		}
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public TerminalNode COLON() { return getToken(TwoDimParser.COLON, 0); }
		public KeyedElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyedElement; }
	}

	public final KeyedElementContext keyedElement() throws RecognitionException {
		KeyedElementContext _localctx = new KeyedElementContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_keyedElement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(589);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,63,_ctx) ) {
			case 1:
				{
				setState(586);
				key();
				setState(587);
				match(COLON);
				}
				break;
			}
			setState(591);
			element();
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

	public static class KeyContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LiteralValueContext literalValue() {
			return getRuleContext(LiteralValueContext.class,0);
		}
		public KeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_key; }
	}

	public final KeyContext key() throws RecognitionException {
		KeyContext _localctx = new KeyContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_key);
		try {
			setState(596);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(593);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(594);
				expression(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(595);
				literalValue();
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
		enterRule(_localctx, 124, RULE_element);
		try {
			setState(600);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
			case NIL_LIT:
			case IDENTIFIER:
			case L_PAREN:
			case L_BRACKET:
			case EXCLAMATION:
			case PLUS:
			case MINUS:
			case CARET:
			case STAR:
			case AMPERSAND:
			case DECIMAL_LIT:
			case FLOAT_LIT:
			case RUNE_LIT:
			case RAW_STRING_LIT:
			case INTERPRETED_STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(598);
				expression(0);
				}
				break;
			case L_CURLY:
				enterOuterAlt(_localctx, 2);
				{
				setState(599);
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

	public static class FieldDeclContext extends ParserRuleContext {
		public IdentifierListContext identifierList() {
			return getRuleContext(IdentifierListContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public AnonymousFieldContext anonymousField() {
			return getRuleContext(AnonymousFieldContext.class,0);
		}
		public String_Context string_() {
			return getRuleContext(String_Context.class,0);
		}
		public FieldDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fieldDecl; }
	}

	public final FieldDeclContext fieldDecl() throws RecognitionException {
		FieldDeclContext _localctx = new FieldDeclContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_fieldDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(607);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,66,_ctx) ) {
			case 1:
				{
				setState(602);
				if (!(noTerminatorBetween(2))) throw new FailedPredicateException(this, "noTerminatorBetween(2)");
				setState(603);
				identifierList();
				setState(604);
				type_();
				}
				break;
			case 2:
				{
				setState(606);
				anonymousField();
				}
				break;
			}
			setState(610);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==RAW_STRING_LIT || _la==INTERPRETED_STRING_LIT) {
				{
				setState(609);
				string_();
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
		enterRule(_localctx, 128, RULE_string_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(612);
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

	public static class AnonymousFieldContext extends ParserRuleContext {
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public TerminalNode STAR() { return getToken(TwoDimParser.STAR, 0); }
		public AnonymousFieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_anonymousField; }
	}

	public final AnonymousFieldContext anonymousField() throws RecognitionException {
		AnonymousFieldContext _localctx = new AnonymousFieldContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_anonymousField);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(615);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STAR) {
				{
				setState(614);
				match(STAR);
				}
			}

			setState(617);
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

	public static class FunctionLitContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(TwoDimParser.FUNC, 0); }
		public SignatureContext signature() {
			return getRuleContext(SignatureContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FunctionLitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionLit; }
	}

	public final FunctionLitContext functionLit() throws RecognitionException {
		FunctionLitContext _localctx = new FunctionLitContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_functionLit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(619);
			match(FUNC);
			setState(620);
			signature();
			setState(621);
			block();
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

	public static class IndexContext extends ParserRuleContext {
		public TerminalNode L_BRACKET() { return getToken(TwoDimParser.L_BRACKET, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode R_BRACKET() { return getToken(TwoDimParser.R_BRACKET, 0); }
		public IndexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index; }
	}

	public final IndexContext index() throws RecognitionException {
		IndexContext _localctx = new IndexContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_index);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(623);
			match(L_BRACKET);
			setState(624);
			expression(0);
			setState(625);
			match(R_BRACKET);
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

	public static class TypeAssertionContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(TwoDimParser.DOT, 0); }
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public TypeAssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeAssertion; }
	}

	public final TypeAssertionContext typeAssertion() throws RecognitionException {
		TypeAssertionContext _localctx = new TypeAssertionContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_typeAssertion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(627);
			match(DOT);
			setState(628);
			match(L_PAREN);
			setState(629);
			type_();
			setState(630);
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

	public static class ArgumentsContext extends ParserRuleContext {
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(TwoDimParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(TwoDimParser.COMMA, i);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(632);
			match(L_PAREN);
			setState(644);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FUNC) | (1L << NIL_LIT) | (1L << IDENTIFIER) | (1L << L_PAREN) | (1L << L_BRACKET) | (1L << EXCLAMATION) | (1L << PLUS) | (1L << MINUS) | (1L << CARET) | (1L << STAR) | (1L << AMPERSAND) | (1L << DECIMAL_LIT) | (1L << FLOAT_LIT) | (1L << RUNE_LIT) | (1L << RAW_STRING_LIT) | (1L << INTERPRETED_STRING_LIT))) != 0)) {
				{
				setState(639);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,70,_ctx) ) {
				case 1:
					{
					setState(633);
					expressionList();
					}
					break;
				case 2:
					{
					setState(634);
					type_();
					setState(637);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,69,_ctx) ) {
					case 1:
						{
						setState(635);
						match(COMMA);
						setState(636);
						expressionList();
						}
						break;
					}
					}
					break;
				}
				setState(642);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(641);
					match(COMMA);
					}
				}

				}
			}

			setState(646);
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

	public static class MethodExprContext extends ParserRuleContext {
		public ReceiverTypeContext receiverType() {
			return getRuleContext(ReceiverTypeContext.class,0);
		}
		public TerminalNode DOT() { return getToken(TwoDimParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(TwoDimParser.IDENTIFIER, 0); }
		public MethodExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodExpr; }
	}

	public final MethodExprContext methodExpr() throws RecognitionException {
		MethodExprContext _localctx = new MethodExprContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_methodExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(648);
			receiverType();
			setState(649);
			match(DOT);
			setState(650);
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

	public static class ReceiverTypeContext extends ParserRuleContext {
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public TerminalNode L_PAREN() { return getToken(TwoDimParser.L_PAREN, 0); }
		public TerminalNode R_PAREN() { return getToken(TwoDimParser.R_PAREN, 0); }
		public TerminalNode STAR() { return getToken(TwoDimParser.STAR, 0); }
		public ReceiverTypeContext receiverType() {
			return getRuleContext(ReceiverTypeContext.class,0);
		}
		public ReceiverTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_receiverType; }
	}

	public final ReceiverTypeContext receiverType() throws RecognitionException {
		ReceiverTypeContext _localctx = new ReceiverTypeContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_receiverType);
		try {
			setState(661);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(652);
				typeName();
				}
				break;
			case L_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(653);
				match(L_PAREN);
				setState(657);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case STAR:
					{
					setState(654);
					match(STAR);
					setState(655);
					typeName();
					}
					break;
				case IDENTIFIER:
				case L_PAREN:
					{
					setState(656);
					receiverType();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(659);
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
		enterRule(_localctx, 144, RULE_eos);
		try {
			setState(667);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,75,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(663);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(664);
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(665);
				if (!(lineTerminatorAhead())) throw new FailedPredicateException(this, "lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(666);
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
		case 40:
			return methodSpec_sempred((MethodSpecContext)_localctx, predIndex);
		case 42:
			return signature_sempred((SignatureContext)_localctx, predIndex);
		case 46:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 47:
			return primaryExpr_sempred((PrimaryExprContext)_localctx, predIndex);
		case 63:
			return fieldDecl_sempred((FieldDeclContext)_localctx, predIndex);
		case 72:
			return eos_sempred((EosContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean methodSpec_sempred(MethodSpecContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return noTerminatorAfterParams(2);
		}
		return true;
	}
	private boolean signature_sempred(SignatureContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return noTerminatorAfterParams(1);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 4);
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 2);
		case 6:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean primaryExpr_sempred(PrimaryExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean fieldDecl_sempred(FieldDeclContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8:
			return noTerminatorBetween(2);
		}
		return true;
	}
	private boolean eos_sempred(EosContext _localctx, int predIndex) {
		switch (predIndex) {
		case 9:
			return lineTerminatorAhead();
		case 10:
			return checkPreviousTokenText("}");
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A\u02a0\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\3\2\3\2\3\2\3\2\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\3"+
		"\2\3\2\5\2\u00a2\n\2\3\2\3\2\7\2\u00a6\n\2\f\2\16\2\u00a9\13\2\3\3\3\3"+
		"\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00b4\n\4\f\4\16\4\u00b7\13\4\3\4\5\4"+
		"\u00ba\n\4\3\5\5\5\u00bd\n\5\3\5\3\5\3\6\3\6\3\7\3\7\5\7\u00c5\n\7\3\b"+
		"\3\b\3\b\7\b\u00ca\n\b\f\b\16\b\u00cd\13\b\3\t\3\t\3\t\7\t\u00d2\n\t\f"+
		"\t\16\t\u00d5\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00dd\n\n\f\n\16\n\u00e0"+
		"\13\n\3\n\5\n\u00e3\n\n\3\13\3\13\5\13\u00e7\n\13\3\13\3\13\3\f\3\f\3"+
		"\f\3\f\5\f\u00ef\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00f6\n\r\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\7\17\u00ff\n\17\f\17\16\17\u0102\13\17\3\17\5\17"+
		"\u0105\n\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u010e\n\21\3\21\3"+
		"\21\3\22\3\22\3\22\6\22\u0115\n\22\r\22\16\22\u0116\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\5\23\u011f\n\23\3\24\3\24\3\24\3\24\5\24\u0125\n\24\3\25\3"+
		"\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\5\30\u0131\n\30\3\30\3\30"+
		"\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u013f\n\33\3\33"+
		"\3\33\3\33\3\33\3\33\5\33\u0146\n\33\5\33\u0148\n\33\3\34\3\34\5\34\u014c"+
		"\n\34\3\35\3\35\3\35\3\35\5\35\u0152\n\35\3\35\5\35\u0155\n\35\3\35\3"+
		"\35\7\35\u0159\n\35\f\35\16\35\u015c\13\35\3\35\3\35\3\36\3\36\3\36\5"+
		"\36\u0163\n\36\3\37\3\37\3\37\5\37\u0168\n\37\3 \3 \3 \3 \5 \u016e\n "+
		"\3 \3 \3 \7 \u0173\n \f \16 \u0176\13 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\""+
		"\3\"\5\"\u0183\n\"\3#\3#\3#\5#\u0188\n#\3$\3$\5$\u018c\n$\3$\3$\3$\5$"+
		"\u0191\n$\7$\u0193\n$\f$\16$\u0196\13$\3%\3%\3%\5%\u019b\n%\3%\3%\3&\3"+
		"&\3&\3&\3&\3&\5&\u01a5\n&\3\'\3\'\5\'\u01a9\n\'\3(\3(\3)\3)\3*\3*\3*\3"+
		"*\3*\3*\3*\3*\5*\u01b7\n*\3+\3+\3+\3,\3,\3,\3,\3,\5,\u01c1\n,\3-\3-\5"+
		"-\u01c5\n-\3.\3.\3.\3.\7.\u01cb\n.\f.\16.\u01ce\13.\3.\5.\u01d1\n.\5."+
		"\u01d3\n.\3.\3.\3/\5/\u01d8\n/\3/\3/\3\60\3\60\3\60\5\60\u01df\n\60\3"+
		"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3"+
		"\60\7\60\u01f0\n\60\f\60\16\60\u01f3\13\60\3\61\3\61\3\61\5\61\u01f8\n"+
		"\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0200\n\61\7\61\u0202\n\61\f\61"+
		"\16\61\u0205\13\61\3\62\3\62\3\62\5\62\u020a\n\62\3\63\3\63\3\63\3\63"+
		"\5\63\u0210\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u021b"+
		"\n\64\3\65\3\65\3\65\5\65\u0220\n\65\3\66\3\66\3\66\3\66\3\66\5\66\u0227"+
		"\n\66\3\67\3\67\38\38\58\u022d\n8\39\39\39\39\3:\3:\3:\3;\3;\3;\3;\5;"+
		"\u023a\n;\3<\3<\3<\5<\u023f\n<\5<\u0241\n<\3<\3<\3=\3=\3=\7=\u0248\n="+
		"\f=\16=\u024b\13=\3>\3>\3>\5>\u0250\n>\3>\3>\3?\3?\3?\5?\u0257\n?\3@\3"+
		"@\5@\u025b\n@\3A\3A\3A\3A\3A\5A\u0262\nA\3A\5A\u0265\nA\3B\3B\3C\5C\u026a"+
		"\nC\3C\3C\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\5G\u0280"+
		"\nG\5G\u0282\nG\3G\5G\u0285\nG\5G\u0287\nG\3G\3G\3H\3H\3H\3H\3I\3I\3I"+
		"\3I\3I\5I\u0294\nI\3I\3I\5I\u0298\nI\3J\3J\3J\3J\5J\u029e\nJ\3J\2\4^`"+
		"K\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF"+
		"HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c"+
		"\u008e\u0090\u0092\2\13\4\2\r\r\"\"\3\2#$\3\2\64\65\4\2.\62\678\4\2--"+
		"\64\66\3\2\',\3\2\638\4\299;;\3\2<=\2\u02b9\2\u0094\3\2\2\2\4\u00aa\3"+
		"\2\2\2\6\u00ad\3\2\2\2\b\u00bc\3\2\2\2\n\u00c0\3\2\2\2\f\u00c4\3\2\2\2"+
		"\16\u00c6\3\2\2\2\20\u00ce\3\2\2\2\22\u00d6\3\2\2\2\24\u00e4\3\2\2\2\26"+
		"\u00ea\3\2\2\2\30\u00f0\3\2\2\2\32\u00f7\3\2\2\2\34\u0104\3\2\2\2\36\u0106"+
		"\3\2\2\2 \u010b\3\2\2\2\"\u0114\3\2\2\2$\u011e\3\2\2\2&\u0124\3\2\2\2"+
		"(\u0126\3\2\2\2*\u0128\3\2\2\2,\u012b\3\2\2\2.\u0130\3\2\2\2\60\u0134"+
		"\3\2\2\2\62\u0136\3\2\2\2\64\u013a\3\2\2\2\66\u014b\3\2\2\28\u014d\3\2"+
		"\2\2:\u015f\3\2\2\2<\u0167\3\2\2\2>\u0169\3\2\2\2@\u0179\3\2\2\2B\u017f"+
		"\3\2\2\2D\u0187\3\2\2\2F\u018b\3\2\2\2H\u019a\3\2\2\2J\u01a4\3\2\2\2L"+
		"\u01a8\3\2\2\2N\u01aa\3\2\2\2P\u01ac\3\2\2\2R\u01b6\3\2\2\2T\u01b8\3\2"+
		"\2\2V\u01c0\3\2\2\2X\u01c4\3\2\2\2Z\u01c6\3\2\2\2\\\u01d7\3\2\2\2^\u01de"+
		"\3\2\2\2`\u01f7\3\2\2\2b\u0209\3\2\2\2d\u020b\3\2\2\2f\u021a\3\2\2\2h"+
		"\u021f\3\2\2\2j\u0226\3\2\2\2l\u0228\3\2\2\2n\u022c\3\2\2\2p\u022e\3\2"+
		"\2\2r\u0232\3\2\2\2t\u0239\3\2\2\2v\u023b\3\2\2\2x\u0244\3\2\2\2z\u024f"+
		"\3\2\2\2|\u0256\3\2\2\2~\u025a\3\2\2\2\u0080\u0261\3\2\2\2\u0082\u0266"+
		"\3\2\2\2\u0084\u0269\3\2\2\2\u0086\u026d\3\2\2\2\u0088\u0271\3\2\2\2\u008a"+
		"\u0275\3\2\2\2\u008c\u027a\3\2\2\2\u008e\u028a\3\2\2\2\u0090\u0297\3\2"+
		"\2\2\u0092\u029d\3\2\2\2\u0094\u0095\5\4\3\2\u0095\u009b\5\u0092J\2\u0096"+
		"\u0097\5\6\4\2\u0097\u0098\5\u0092J\2\u0098\u009a\3\2\2\2\u0099\u0096"+
		"\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c"+
		"\u00a7\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a2\5\26\f\2\u009f\u00a2\5"+
		"\30\r\2\u00a0\u00a2\5\f\7\2\u00a1\u009e\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1"+
		"\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\5\u0092J\2\u00a4\u00a6"+
		"\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7"+
		"\u00a8\3\2\2\2\u00a8\3\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7\n\2\2"+
		"\u00ab\u00ac\7\r\2\2\u00ac\5\3\2\2\2\u00ad\u00b9\7\13\2\2\u00ae\u00ba"+
		"\5\b\5\2\u00af\u00b5\7\30\2\2\u00b0\u00b1\5\b\5\2\u00b1\u00b2\5\u0092"+
		"J\2\u00b2\u00b4\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5"+
		"\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2"+
		"\2\2\u00b8\u00ba\7\31\2\2\u00b9\u00ae\3\2\2\2\u00b9\u00af\3\2\2\2\u00ba"+
		"\7\3\2\2\2\u00bb\u00bd\t\2\2\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2"+
		"\u00bd\u00be\3\2\2\2\u00be\u00bf\5\n\6\2\u00bf\t\3\2\2\2\u00c0\u00c1\5"+
		"\u0082B\2\u00c1\13\3\2\2\2\u00c2\u00c5\5\22\n\2\u00c3\u00c5\5\34\17\2"+
		"\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\r\3\2\2\2\u00c6\u00cb\7"+
		"\r\2\2\u00c7\u00c8\7\37\2\2\u00c8\u00ca\7\r\2\2\u00c9\u00c7\3\2\2\2\u00ca"+
		"\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\17\3\2\2"+
		"\2\u00cd\u00cb\3\2\2\2\u00ce\u00d3\5^\60\2\u00cf\u00d0\7\37\2\2\u00d0"+
		"\u00d2\5^\60\2\u00d1\u00cf\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2"+
		"\2\2\u00d3\u00d4\3\2\2\2\u00d4\21\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00e2"+
		"\7\t\2\2\u00d7\u00e3\5\24\13\2\u00d8\u00de\7\30\2\2\u00d9\u00da\5\24\13"+
		"\2\u00da\u00db\5\u0092J\2\u00db\u00dd\3\2\2\2\u00dc\u00d9\3\2\2\2\u00dd"+
		"\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2"+
		"\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e3\7\31\2\2\u00e2\u00d7\3\2\2\2\u00e2"+
		"\u00d8\3\2\2\2\u00e3\23\3\2\2\2\u00e4\u00e6\7\r\2\2\u00e5\u00e7\7\36\2"+
		"\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9"+
		"\5J&\2\u00e9\25\3\2\2\2\u00ea\u00eb\7\3\2\2\u00eb\u00ec\7\r\2\2\u00ec"+
		"\u00ee\5V,\2\u00ed\u00ef\5 \21\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2"+
		"\2\u00ef\27\3\2\2\2\u00f0\u00f1\7\3\2\2\u00f1\u00f2\5\32\16\2\u00f2\u00f3"+
		"\7\r\2\2\u00f3\u00f5\5V,\2\u00f4\u00f6\5 \21\2\u00f5\u00f4\3\2\2\2\u00f5"+
		"\u00f6\3\2\2\2\u00f6\31\3\2\2\2\u00f7\u00f8\5Z.\2\u00f8\33\3\2\2\2\u00f9"+
		"\u0105\5\36\20\2\u00fa\u0100\7\30\2\2\u00fb\u00fc\5\36\20\2\u00fc\u00fd"+
		"\5\u0092J\2\u00fd\u00ff\3\2\2\2\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2"+
		"\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0103\3\2\2\2\u0102\u0100"+
		"\3\2\2\2\u0103\u0105\7\31\2\2\u0104\u00f9\3\2\2\2\u0104\u00fa\3\2\2\2"+
		"\u0105\35\3\2\2\2\u0106\u0107\5J&\2\u0107\u0108\5\16\b\2\u0108\u0109\7"+
		"\36\2\2\u0109\u010a\5\20\t\2\u010a\37\3\2\2\2\u010b\u010d\7\32\2\2\u010c"+
		"\u010e\5\"\22\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3"+
		"\2\2\2\u010f\u0110\7\33\2\2\u0110!\3\2\2\2\u0111\u0112\5$\23\2\u0112\u0113"+
		"\5\u0092J\2\u0113\u0115\3\2\2\2\u0114\u0111\3\2\2\2\u0115\u0116\3\2\2"+
		"\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117#\3\2\2\2\u0118\u011f"+
		"\5\f\7\2\u0119\u011f\5\62\32\2\u011a\u011f\5&\24\2\u011b\u011f\5 \21\2"+
		"\u011c\u011f\5\64\33\2\u011d\u011f\5\66\34\2\u011e\u0118\3\2\2\2\u011e"+
		"\u0119\3\2\2\2\u011e\u011a\3\2\2\2\u011e\u011b\3\2\2\2\u011e\u011c\3\2"+
		"\2\2\u011e\u011d\3\2\2\2\u011f%\3\2\2\2\u0120\u0125\5(\25\2\u0121\u0125"+
		"\5*\26\2\u0122\u0125\5,\27\2\u0123\u0125\5\60\31\2\u0124\u0120\3\2\2\2"+
		"\u0124\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125\'\3"+
		"\2\2\2\u0126\u0127\5^\60\2\u0127)\3\2\2\2\u0128\u0129\5^\60\2\u0129\u012a"+
		"\t\3\2\2\u012a+\3\2\2\2\u012b\u012c\5\20\t\2\u012c\u012d\5.\30\2\u012d"+
		"\u012e\5\20\t\2\u012e-\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u012f\3\2\2\2"+
		"\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\7\36\2\2\u0133/\3"+
		"\2\2\2\u0134\u0135\7 \2\2\u0135\61\3\2\2\2\u0136\u0137\7\r\2\2\u0137\u0138"+
		"\7!\2\2\u0138\u0139\5$\23\2\u0139\63\3\2\2\2\u013a\u013e\7\7\2\2\u013b"+
		"\u013c\5&\24\2\u013c\u013d\7 \2\2\u013d\u013f\3\2\2\2\u013e\u013b\3\2"+
		"\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\5^\60\2\u0141"+
		"\u0147\5 \21\2\u0142\u0145\7\b\2\2\u0143\u0146\5\64\33\2\u0144\u0146\5"+
		" \21\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146\u0148\3\2\2\2\u0147"+
		"\u0142\3\2\2\2\u0147\u0148\3\2\2\2\u0148\65\3\2\2\2\u0149\u014c\58\35"+
		"\2\u014a\u014c\5> \2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c\67"+
		"\3\2\2\2\u014d\u0151\7\4\2\2\u014e\u014f\5&\24\2\u014f\u0150\7 \2\2\u0150"+
		"\u0152\3\2\2\2\u0151\u014e\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0154\3\2"+
		"\2\2\u0153\u0155\5^\60\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155"+
		"\u0156\3\2\2\2\u0156\u015a\7\32\2\2\u0157\u0159\5:\36\2\u0158\u0157\3"+
		"\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b"+
		"\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7\33\2\2\u015e9\3\2\2\2"+
		"\u015f\u0160\5<\37\2\u0160\u0162\7!\2\2\u0161\u0163\5\"\22\2\u0162\u0161"+
		"\3\2\2\2\u0162\u0163\3\2\2\2\u0163;\3\2\2\2\u0164\u0165\7\5\2\2\u0165"+
		"\u0168\5\20\t\2\u0166\u0168\7\6\2\2\u0167\u0164\3\2\2\2\u0167\u0166\3"+
		"\2\2\2\u0168=\3\2\2\2\u0169\u016d\7\4\2\2\u016a\u016b\5&\24\2\u016b\u016c"+
		"\7 \2\2\u016c\u016e\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016e\3\2\2\2\u016e"+
		"\u016f\3\2\2\2\u016f\u0170\5@!\2\u0170\u0174\7\32\2\2\u0171\u0173\5B\""+
		"\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175"+
		"\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7\33\2\2"+
		"\u0178?\3\2\2\2\u0179\u017a\5`\61\2\u017a\u017b\7\"\2\2\u017b\u017c\7"+
		"\30\2\2\u017c\u017d\7\t\2\2\u017d\u017e\7\31\2\2\u017eA\3\2\2\2\u017f"+
		"\u0180\5D#\2\u0180\u0182\7!\2\2\u0181\u0183\5\"\22\2\u0182\u0181\3\2\2"+
		"\2\u0182\u0183\3\2\2\2\u0183C\3\2\2\2\u0184\u0185\7\5\2\2\u0185\u0188"+
		"\5F$\2\u0186\u0188\7\6\2\2\u0187\u0184\3\2\2\2\u0187\u0186\3\2\2\2\u0188"+
		"E\3\2\2\2\u0189\u018c\5J&\2\u018a\u018c\7\f\2\2\u018b\u0189\3\2\2\2\u018b"+
		"\u018a\3\2\2\2\u018c\u0194\3\2\2\2\u018d\u0190\7\37\2\2\u018e\u0191\5"+
		"J&\2\u018f\u0191\7\f\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191"+
		"\u0193\3\2\2\2\u0192\u018d\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2"+
		"\2\2\u0194\u0195\3\2\2\2\u0195G\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0198"+
		"\5\20\t\2\u0198\u0199\7\36\2\2\u0199\u019b\3\2\2\2\u019a\u0197\3\2\2\2"+
		"\u019a\u019b\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\5^\60\2\u019dI\3"+
		"\2\2\2\u019e\u01a5\5L\'\2\u019f\u01a5\5N(\2\u01a0\u01a1\7\30\2\2\u01a1"+
		"\u01a2\5J&\2\u01a2\u01a3\7\31\2\2\u01a3\u01a5\3\2\2\2\u01a4\u019e\3\2"+
		"\2\2\u01a4\u019f\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a5K\3\2\2\2\u01a6\u01a9"+
		"\7\r\2\2\u01a7\u01a9\5p9\2\u01a8\u01a6\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9"+
		"M\3\2\2\2\u01aa\u01ab\5T+\2\u01abO\3\2\2\2\u01ac\u01ad\5J&\2\u01adQ\3"+
		"\2\2\2\u01ae\u01af\6*\2\2\u01af\u01b0\7\r\2\2\u01b0\u01b1\5Z.\2\u01b1"+
		"\u01b2\5X-\2\u01b2\u01b7\3\2\2\2\u01b3\u01b7\5L\'\2\u01b4\u01b5\7\r\2"+
		"\2\u01b5\u01b7\5Z.\2\u01b6\u01ae\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b6\u01b4"+
		"\3\2\2\2\u01b7S\3\2\2\2\u01b8\u01b9\7\3\2\2\u01b9\u01ba\5V,\2\u01baU\3"+
		"\2\2\2\u01bb\u01bc\6,\3\2\u01bc\u01bd\5Z.\2\u01bd\u01be\5X-\2\u01be\u01c1"+
		"\3\2\2\2\u01bf\u01c1\5Z.\2\u01c0\u01bb\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1"+
		"W\3\2\2\2\u01c2\u01c5\5Z.\2\u01c3\u01c5\5J&\2\u01c4\u01c2\3\2\2\2\u01c4"+
		"\u01c3\3\2\2\2\u01c5Y\3\2\2\2\u01c6\u01d2\7\30\2\2\u01c7\u01cc\5\\/\2"+
		"\u01c8\u01c9\7\37\2\2\u01c9\u01cb\5\\/\2\u01ca\u01c8\3\2\2\2\u01cb\u01ce"+
		"\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce"+
		"\u01cc\3\2\2\2\u01cf\u01d1\7\37\2\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3"+
		"\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01c7\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3"+
		"\u01d4\3\2\2\2\u01d4\u01d5\7\31\2\2\u01d5[\3\2\2\2\u01d6\u01d8\5\16\b"+
		"\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da"+
		"\5J&\2\u01da]\3\2\2\2\u01db\u01dc\b\60\1\2\u01dc\u01df\5`\61\2\u01dd\u01df"+
		"\5b\62\2\u01de\u01db\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01f1\3\2\2\2\u01e0"+
		"\u01e1\f\7\2\2\u01e1\u01e2\t\5\2\2\u01e2\u01f0\5^\60\b\u01e3\u01e4\f\6"+
		"\2\2\u01e4\u01e5\t\6\2\2\u01e5\u01f0\5^\60\7\u01e6\u01e7\f\5\2\2\u01e7"+
		"\u01e8\t\7\2\2\u01e8\u01f0\5^\60\6\u01e9\u01ea\f\4\2\2\u01ea\u01eb\7&"+
		"\2\2\u01eb\u01f0\5^\60\5\u01ec\u01ed\f\3\2\2\u01ed\u01ee\7%\2\2\u01ee"+
		"\u01f0\5^\60\4\u01ef\u01e0\3\2\2\2\u01ef\u01e3\3\2\2\2\u01ef\u01e6\3\2"+
		"\2\2\u01ef\u01e9\3\2\2\2\u01ef\u01ec\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1"+
		"\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2_\3\2\2\2\u01f3\u01f1\3\2\2\2"+
		"\u01f4\u01f5\b\61\1\2\u01f5\u01f8\5f\64\2\u01f6\u01f8\5d\63\2\u01f7\u01f4"+
		"\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8\u0203\3\2\2\2\u01f9\u01ff\f\3\2\2\u01fa"+
		"\u01fb\7\"\2\2\u01fb\u0200\7\r\2\2\u01fc\u0200\5\u0088E\2\u01fd\u0200"+
		"\5\u008aF\2\u01fe\u0200\5\u008cG\2\u01ff\u01fa\3\2\2\2\u01ff\u01fc\3\2"+
		"\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200\u0202\3\2\2\2\u0201"+
		"\u01f9\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3\2"+
		"\2\2\u0204a\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u020a\5`\61\2\u0207\u0208"+
		"\t\b\2\2\u0208\u020a\5^\60\2\u0209\u0206\3\2\2\2\u0209\u0207\3\2\2\2\u020a"+
		"c\3\2\2\2\u020b\u020c\5J&\2\u020c\u020d\7\30\2\2\u020d\u020f\5^\60\2\u020e"+
		"\u0210\7\37\2\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211\3"+
		"\2\2\2\u0211\u0212\7\31\2\2\u0212e\3\2\2\2\u0213\u021b\5h\65\2\u0214\u021b"+
		"\5n8\2\u0215\u021b\5\u008eH\2\u0216\u0217\7\30\2\2\u0217\u0218\5^\60\2"+
		"\u0218\u0219\7\31\2\2\u0219\u021b\3\2\2\2\u021a\u0213\3\2\2\2\u021a\u0214"+
		"\3\2\2\2\u021a\u0215\3\2\2\2\u021a\u0216\3\2\2\2\u021bg\3\2\2\2\u021c"+
		"\u0220\5j\66\2\u021d\u0220\5r:\2\u021e\u0220\5\u0086D\2\u021f\u021c\3"+
		"\2\2\2\u021f\u021d\3\2\2\2\u021f\u021e\3\2\2\2\u0220i\3\2\2\2\u0221\u0227"+
		"\7\f\2\2\u0222\u0227\5l\67\2\u0223\u0227\5\u0082B\2\u0224\u0227\7:\2\2"+
		"\u0225\u0227\7;\2\2\u0226\u0221\3\2\2\2\u0226\u0222\3\2\2\2\u0226\u0223"+
		"\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0225\3\2\2\2\u0227k\3\2\2\2\u0228"+
		"\u0229\t\t\2\2\u0229m\3\2\2\2\u022a\u022d\7\r\2\2\u022b\u022d\5p9\2\u022c"+
		"\u022a\3\2\2\2\u022c\u022b\3\2\2\2\u022do\3\2\2\2\u022e\u022f\7\r\2\2"+
		"\u022f\u0230\7\"\2\2\u0230\u0231\7\r\2\2\u0231q\3\2\2\2\u0232\u0233\5"+
		"t;\2\u0233\u0234\5v<\2\u0234s\3\2\2\2\u0235\u0236\7\34\2\2\u0236\u0237"+
		"\7\35\2\2\u0237\u023a\5P)\2\u0238\u023a\5L\'\2\u0239\u0235\3\2\2\2\u0239"+
		"\u0238\3\2\2\2\u023au\3\2\2\2\u023b\u0240\7\32\2\2\u023c\u023e\5x=\2\u023d"+
		"\u023f\7\37\2\2\u023e\u023d\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0241\3"+
		"\2\2\2\u0240\u023c\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242"+
		"\u0243\7\33\2\2\u0243w\3\2\2\2\u0244\u0249\5z>\2\u0245\u0246\7\37\2\2"+
		"\u0246\u0248\5z>\2\u0247\u0245\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247"+
		"\3\2\2\2\u0249\u024a\3\2\2\2\u024ay\3\2\2\2\u024b\u0249\3\2\2\2\u024c"+
		"\u024d\5|?\2\u024d\u024e\7!\2\2\u024e\u0250\3\2\2\2\u024f\u024c\3\2\2"+
		"\2\u024f\u0250\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252\5~@\2\u0252{\3"+
		"\2\2\2\u0253\u0257\7\r\2\2\u0254\u0257\5^\60\2\u0255\u0257\5v<\2\u0256"+
		"\u0253\3\2\2\2\u0256\u0254\3\2\2\2\u0256\u0255\3\2\2\2\u0257}\3\2\2\2"+
		"\u0258\u025b\5^\60\2\u0259\u025b\5v<\2\u025a\u0258\3\2\2\2\u025a\u0259"+
		"\3\2\2\2\u025b\177\3\2\2\2\u025c\u025d\6A\n\2\u025d\u025e\5\16\b\2\u025e"+
		"\u025f\5J&\2\u025f\u0262\3\2\2\2\u0260\u0262\5\u0084C\2\u0261\u025c\3"+
		"\2\2\2\u0261\u0260\3\2\2\2\u0262\u0264\3\2\2\2\u0263\u0265\5\u0082B\2"+
		"\u0264\u0263\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0081\3\2\2\2\u0266\u0267"+
		"\t\n\2\2\u0267\u0083\3\2\2\2\u0268\u026a\7\67\2\2\u0269\u0268\3\2\2\2"+
		"\u0269\u026a\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026c\5L\'\2\u026c\u0085"+
		"\3\2\2\2\u026d\u026e\7\3\2\2\u026e\u026f\5V,\2\u026f\u0270\5 \21\2\u0270"+
		"\u0087\3\2\2\2\u0271\u0272\7\34\2\2\u0272\u0273\5^\60\2\u0273\u0274\7"+
		"\35\2\2\u0274\u0089\3\2\2\2\u0275\u0276\7\"\2\2\u0276\u0277\7\30\2\2\u0277"+
		"\u0278\5J&\2\u0278\u0279\7\31\2\2\u0279\u008b\3\2\2\2\u027a\u0286\7\30"+
		"\2\2\u027b\u0282\5\20\t\2\u027c\u027f\5J&\2\u027d\u027e\7\37\2\2\u027e"+
		"\u0280\5\20\t\2\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0282\3"+
		"\2\2\2\u0281\u027b\3\2\2\2\u0281\u027c\3\2\2\2\u0282\u0284\3\2\2\2\u0283"+
		"\u0285\7\37\2\2\u0284\u0283\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0287\3"+
		"\2\2\2\u0286\u0281\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\3\2\2\2\u0288"+
		"\u0289\7\31\2\2\u0289\u008d\3\2\2\2\u028a\u028b\5\u0090I\2\u028b\u028c"+
		"\7\"\2\2\u028c\u028d\7\r\2\2\u028d\u008f\3\2\2\2\u028e\u0298\5L\'\2\u028f"+
		"\u0293\7\30\2\2\u0290\u0291\7\67\2\2\u0291\u0294\5L\'\2\u0292\u0294\5"+
		"\u0090I\2\u0293\u0290\3\2\2\2\u0293\u0292\3\2\2\2\u0294\u0295\3\2\2\2"+
		"\u0295\u0296\7\31\2\2\u0296\u0298\3\2\2\2\u0297\u028e\3\2\2\2\u0297\u028f"+
		"\3\2\2\2\u0298\u0091\3\2\2\2\u0299\u029e\7 \2\2\u029a\u029e\7\2\2\3\u029b"+
		"\u029e\6J\13\2\u029c\u029e\6J\f\2\u029d\u0299\3\2\2\2\u029d\u029a\3\2"+
		"\2\2\u029d\u029b\3\2\2\2\u029d\u029c\3\2\2\2\u029e\u0093\3\2\2\2N\u009b"+
		"\u00a1\u00a7\u00b5\u00b9\u00bc\u00c4\u00cb\u00d3\u00de\u00e2\u00e6\u00ee"+
		"\u00f5\u0100\u0104\u010d\u0116\u011e\u0124\u0130\u013e\u0145\u0147\u014b"+
		"\u0151\u0154\u015a\u0162\u0167\u016d\u0174\u0182\u0187\u018b\u0190\u0194"+
		"\u019a\u01a4\u01a8\u01b6\u01c0\u01c4\u01cc\u01d0\u01d2\u01d7\u01de\u01ef"+
		"\u01f1\u01f7\u01ff\u0203\u0209\u020f\u021a\u021f\u0226\u022c\u0239\u023e"+
		"\u0240\u0249\u024f\u0256\u025a\u0261\u0264\u0269\u027f\u0281\u0284\u0286"+
		"\u0293\u0297\u029d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}