# Generated from BitTuneGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\5\2\30\n\2\3\2\5\2\33")
        buf.write("\n\2\3\2\5\2\36\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\7\b>\n\b\f\b\16\bA\13")
        buf.write("\b\3\b\5\bD\n\b\3\b\3\b\3\b\3\b\3\t\6\tK\n\t\r\t\16\t")
        buf.write("L\3\n\6\nP\n\n\r\n\16\nQ\3\n\3\n\2\2\13\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\3\2\6\6\2CITTcitt\4\2\f\f")
        buf.write("\17\17\3\2\62;\5\2\13\f\17\17\"\"\2[\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2")
        buf.write("\5\37\3\2\2\2\7%\3\2\2\2\t+\3\2\2\2\13\61\3\2\2\2\r\67")
        buf.write("\3\2\2\2\179\3\2\2\2\21J\3\2\2\2\23O\3\2\2\2\25\27\t\2")
        buf.write("\2\2\26\30\t\2\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\32\3")
        buf.write("\2\2\2\31\33\t\2\2\2\32\31\3\2\2\2\32\33\3\2\2\2\33\35")
        buf.write("\3\2\2\2\34\36\t\2\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36")
        buf.write("\4\3\2\2\2\37 \7t\2\2 !\7g\2\2!\"\7e\2\2\"#\7v\2\2#$\7")
        buf.write("*\2\2$\6\3\2\2\2%&\7q\2\2&\'\7x\2\2\'(\7c\2\2()\7n\2\2")
        buf.write(")*\7*\2\2*\b\3\2\2\2+,\7n\2\2,-\7k\2\2-.\7p\2\2./\7g\2")
        buf.write("\2/\60\7*\2\2\60\n\3\2\2\2\61\62\7f\2\2\62\63\7q\2\2\63")
        buf.write("\64\7v\2\2\64\65\7u\2\2\65\66\7*\2\2\66\f\3\2\2\2\678")
        buf.write("\7+\2\28\16\3\2\2\29:\7\61\2\2:;\7\61\2\2;?\3\2\2\2<>")
        buf.write("\n\3\2\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@C\3\2")
        buf.write("\2\2A?\3\2\2\2BD\7\17\2\2CB\3\2\2\2CD\3\2\2\2DE\3\2\2")
        buf.write("\2EF\7\f\2\2FG\3\2\2\2GH\b\b\2\2H\20\3\2\2\2IK\t\4\2\2")
        buf.write("JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\22\3\2\2\2N")
        buf.write("P\t\5\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RS\3")
        buf.write("\2\2\2ST\b\n\2\2T\24\3\2\2\2\n\2\27\32\35?CLQ\3\b\2\2")
        return buf.getvalue()


class BitTuneGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NOTE = 1
    RECT = 2
    OVAL = 3
    LINE = 4
    DOTS = 5
    CLOSE_BRACKET = 6
    COMMENT = 7
    INT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'rect('", "'oval('", "'line('", "'dots('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NOTE", "RECT", "OVAL", "LINE", "DOTS", "CLOSE_BRACKET", "COMMENT", 
            "INT", "WS" ]

    ruleNames = [ "NOTE", "RECT", "OVAL", "LINE", "DOTS", "CLOSE_BRACKET", 
                  "COMMENT", "INT", "WS" ]

    grammarFileName = "BitTuneGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


