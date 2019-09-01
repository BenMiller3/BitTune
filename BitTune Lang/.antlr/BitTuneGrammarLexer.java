// Generated from c:\Users\benja\Desktop\4TB3 Final Project\group-11-final-project\BitTune Lang\BitTuneGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BitTuneGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NOTE=1, END_NOTE=2, INT=3, CHAR=4, COMMENT=5, WS=6;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"NOTE", "END_NOTE", "INT", "CHAR", "COMMENT", "WS"
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


	public BitTuneGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BitTuneGrammar.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b:\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\5\2\22\n\2\3\2\5\2\25\n"+
		"\2\3\2\5\2\30\n\2\3\3\5\3\33\n\3\3\4\6\4\36\n\4\r\4\16\4\37\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\7\6(\n\6\f\6\16\6+\13\6\3\6\5\6.\n\6\3\6\3\6\3\6\3\6\3"+
		"\7\6\7\65\n\7\r\7\16\7\66\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\b"+
		"\6\2CITTcitt\4\3\f\f\"\"\3\2\62;\4\2C\\c|\4\2\f\f\17\17\4\2\13\13\17\17"+
		"\2@\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3"+
		"\2\2\2\3\17\3\2\2\2\5\32\3\2\2\2\7\35\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r"+
		"\64\3\2\2\2\17\21\t\2\2\2\20\22\t\2\2\2\21\20\3\2\2\2\21\22\3\2\2\2\22"+
		"\24\3\2\2\2\23\25\t\2\2\2\24\23\3\2\2\2\24\25\3\2\2\2\25\27\3\2\2\2\26"+
		"\30\t\2\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\4\3\2\2\2\31\33\t\3\2\2\32"+
		"\31\3\2\2\2\33\6\3\2\2\2\34\36\t\4\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37"+
		"\35\3\2\2\2\37 \3\2\2\2 \b\3\2\2\2!\"\t\5\2\2\"\n\3\2\2\2#$\7\61\2\2$"+
		"%\7\61\2\2%)\3\2\2\2&(\n\6\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2"+
		"\2*-\3\2\2\2+)\3\2\2\2,.\7\17\2\2-,\3\2\2\2-.\3\2\2\2./\3\2\2\2/\60\7"+
		"\f\2\2\60\61\3\2\2\2\61\62\b\6\2\2\62\f\3\2\2\2\63\65\t\7\2\2\64\63\3"+
		"\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\b\7\2\2"+
		"9\16\3\2\2\2\13\2\21\24\27\32\37)-\66\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}