// Generated from c:\Users\benja\Desktop\4TB3 Final Project\group-11-final-project\BitTune Lang\BitTuneGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BitTuneGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NOTE=1, END_NOTE=2, INT=3, CHAR=4, COMMENT=5, WS=6;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_multiNoteSequence = 2, RULE_noteSequence = 3, 
		RULE_commentSequence = 4;
	public static final String[] ruleNames = {
		"prog", "statement", "multiNoteSequence", "noteSequence", "commentSequence"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "NOTE", "END_NOTE", "INT", "CHAR", "COMMENT", "WS"
	};
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
	public String getGrammarFileName() { return "BitTuneGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BitTuneGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				statement();
				}
				}
				setState(13); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NOTE) | (1L << INT) | (1L << COMMENT))) != 0) );
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
		public NoteSequenceContext noteSequence() {
			return getRuleContext(NoteSequenceContext.class,0);
		}
		public MultiNoteSequenceContext multiNoteSequence() {
			return getRuleContext(MultiNoteSequenceContext.class,0);
		}
		public CommentSequenceContext commentSequence() {
			return getRuleContext(CommentSequenceContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(18);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOTE:
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				noteSequence();
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(16);
				multiNoteSequence();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(17);
				commentSequence();
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

	public static class MultiNoteSequenceContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BitTuneGrammarParser.INT, 0); }
		public TerminalNode NOTE() { return getToken(BitTuneGrammarParser.NOTE, 0); }
		public TerminalNode END_NOTE() { return getToken(BitTuneGrammarParser.END_NOTE, 0); }
		public TerminalNode EOF() { return getToken(BitTuneGrammarParser.EOF, 0); }
		public MultiNoteSequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiNoteSequence; }
	}

	public final MultiNoteSequenceContext multiNoteSequence() throws RecognitionException {
		MultiNoteSequenceContext _localctx = new MultiNoteSequenceContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_multiNoteSequence);
		try {
			setState(26);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(20);
				match(INT);
				setState(21);
				match(NOTE);
				setState(22);
				match(END_NOTE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(23);
				match(INT);
				setState(24);
				match(NOTE);
				setState(25);
				match(EOF);
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

	public static class NoteSequenceContext extends ParserRuleContext {
		public TerminalNode NOTE() { return getToken(BitTuneGrammarParser.NOTE, 0); }
		public TerminalNode END_NOTE() { return getToken(BitTuneGrammarParser.END_NOTE, 0); }
		public TerminalNode EOF() { return getToken(BitTuneGrammarParser.EOF, 0); }
		public NoteSequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noteSequence; }
	}

	public final NoteSequenceContext noteSequence() throws RecognitionException {
		NoteSequenceContext _localctx = new NoteSequenceContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_noteSequence);
		try {
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				match(NOTE);
				setState(29);
				match(END_NOTE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(30);
				match(NOTE);
				setState(31);
				match(EOF);
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

	public static class CommentSequenceContext extends ParserRuleContext {
		public TerminalNode COMMENT() { return getToken(BitTuneGrammarParser.COMMENT, 0); }
		public CommentSequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commentSequence; }
	}

	public final CommentSequenceContext commentSequence() throws RecognitionException {
		CommentSequenceContext _localctx = new CommentSequenceContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_commentSequence);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(COMMENT);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b\'\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n\2\r\2\16\2\17\3\3\3\3\3\3\5\3"+
		"\25\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\35\n\4\3\5\3\5\3\5\3\5\5\5#\n\5\3"+
		"\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2&\2\r\3\2\2\2\4\24\3\2\2\2\6\34\3\2\2"+
		"\2\b\"\3\2\2\2\n$\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r"+
		"\3\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21\25\5\b\5\2\22\25\5\6\4\2\23\25"+
		"\5\n\6\2\24\21\3\2\2\2\24\22\3\2\2\2\24\23\3\2\2\2\25\5\3\2\2\2\26\27"+
		"\7\5\2\2\27\30\7\3\2\2\30\35\7\4\2\2\31\32\7\5\2\2\32\33\7\3\2\2\33\35"+
		"\7\2\2\3\34\26\3\2\2\2\34\31\3\2\2\2\35\7\3\2\2\2\36\37\7\3\2\2\37#\7"+
		"\4\2\2 !\7\3\2\2!#\7\2\2\3\"\36\3\2\2\2\" \3\2\2\2#\t\3\2\2\2$%\7\7\2"+
		"\2%\13\3\2\2\2\6\17\24\34\"";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}