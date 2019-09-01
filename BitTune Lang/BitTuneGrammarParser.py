# Generated from BitTuneGrammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\3\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\6\6*\n\6\r\6\16\6+\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22")
        buf.write("\24\2\3\3\2\4\7\2\65\2\27\3\2\2\2\4\37\3\2\2\2\6!\3\2")
        buf.write("\2\2\b#\3\2\2\2\n&\3\2\2\2\f/\3\2\2\2\16\61\3\2\2\2\20")
        buf.write("\63\3\2\2\2\22\65\3\2\2\2\24\67\3\2\2\2\26\30\5\4\3\2")
        buf.write("\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2")
        buf.write("\2\32\3\3\2\2\2\33 \5\6\4\2\34 \5\b\5\2\35 \5\n\6\2\36")
        buf.write(" \5\24\13\2\37\33\3\2\2\2\37\34\3\2\2\2\37\35\3\2\2\2")
        buf.write("\37\36\3\2\2\2 \5\3\2\2\2!\"\5\16\b\2\"\7\3\2\2\2#$\5")
        buf.write("\f\7\2$%\5\16\b\2%\t\3\2\2\2&)\5\20\t\2\'*\5\6\4\2(*\5")
        buf.write("\b\5\2)\'\3\2\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,-\3\2\2\2-.\5\22\n\2.\13\3\2\2\2/\60\7\n\2\2\60\r")
        buf.write("\3\2\2\2\61\62\7\3\2\2\62\17\3\2\2\2\63\64\t\2\2\2\64")
        buf.write("\21\3\2\2\2\65\66\7\b\2\2\66\23\3\2\2\2\678\7\t\2\28\25")
        buf.write("\3\2\2\2\6\31\37)+")
        return buf.getvalue()


class BitTuneGrammarParser ( Parser ):

    grammarFileName = "BitTuneGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'rect('", "'oval('", "'line('", 
                     "'dots('", "')'" ]

    symbolicNames = [ "<INVALID>", "NOTE", "RECT", "OVAL", "LINE", "DOTS", 
                      "CLOSE_BRACKET", "COMMENT", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_noteSequence = 2
    RULE_multiNoteSequence = 3
    RULE_shapeSequence = 4
    RULE_number = 5
    RULE_note = 6
    RULE_shapeName = 7
    RULE_endShape = 8
    RULE_commentSequence = 9

    ruleNames =  [ "program", "statement", "noteSequence", "multiNoteSequence", 
                   "shapeSequence", "number", "note", "shapeName", "endShape", 
                   "commentSequence" ]

    EOF = Token.EOF
    NOTE=1
    RECT=2
    OVAL=3
    LINE=4
    DOTS=5
    CLOSE_BRACKET=6
    COMMENT=7
    INT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BitTuneGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(BitTuneGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BitTuneGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BitTuneGrammarParser.NOTE) | (1 << BitTuneGrammarParser.RECT) | (1 << BitTuneGrammarParser.OVAL) | (1 << BitTuneGrammarParser.LINE) | (1 << BitTuneGrammarParser.DOTS) | (1 << BitTuneGrammarParser.COMMENT) | (1 << BitTuneGrammarParser.INT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noteSequence(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.NoteSequenceContext,0)


        def multiNoteSequence(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.MultiNoteSequenceContext,0)


        def shapeSequence(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.ShapeSequenceContext,0)


        def commentSequence(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.CommentSequenceContext,0)


        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BitTuneGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BitTuneGrammarParser.NOTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.noteSequence()
                pass
            elif token in [BitTuneGrammarParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.multiNoteSequence()
                pass
            elif token in [BitTuneGrammarParser.RECT, BitTuneGrammarParser.OVAL, BitTuneGrammarParser.LINE, BitTuneGrammarParser.DOTS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.shapeSequence()
                pass
            elif token in [BitTuneGrammarParser.COMMENT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.commentSequence()
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


    class NoteSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.NoteContext,0)


        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_noteSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoteSequence" ):
                listener.enterNoteSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoteSequence" ):
                listener.exitNoteSequence(self)




    def noteSequence(self):

        localctx = BitTuneGrammarParser.NoteSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_noteSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.note()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiNoteSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.NumberContext,0)


        def note(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.NoteContext,0)


        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_multiNoteSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiNoteSequence" ):
                listener.enterMultiNoteSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiNoteSequence" ):
                listener.exitMultiNoteSequence(self)




    def multiNoteSequence(self):

        localctx = BitTuneGrammarParser.MultiNoteSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_multiNoteSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.number()
            self.state = 34
            self.note()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shapeName(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.ShapeNameContext,0)


        def endShape(self):
            return self.getTypedRuleContext(BitTuneGrammarParser.EndShapeContext,0)


        def noteSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BitTuneGrammarParser.NoteSequenceContext)
            else:
                return self.getTypedRuleContext(BitTuneGrammarParser.NoteSequenceContext,i)


        def multiNoteSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BitTuneGrammarParser.MultiNoteSequenceContext)
            else:
                return self.getTypedRuleContext(BitTuneGrammarParser.MultiNoteSequenceContext,i)


        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_shapeSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeSequence" ):
                listener.enterShapeSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeSequence" ):
                listener.exitShapeSequence(self)




    def shapeSequence(self):

        localctx = BitTuneGrammarParser.ShapeSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shapeSequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.shapeName()
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BitTuneGrammarParser.NOTE]:
                    self.state = 37
                    self.noteSequence()
                    pass
                elif token in [BitTuneGrammarParser.INT]:
                    self.state = 38
                    self.multiNoteSequence()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BitTuneGrammarParser.NOTE or _la==BitTuneGrammarParser.INT):
                    break

            self.state = 43
            self.endShape()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BitTuneGrammarParser.INT, 0)

        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = BitTuneGrammarParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(BitTuneGrammarParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTE(self):
            return self.getToken(BitTuneGrammarParser.NOTE, 0)

        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = BitTuneGrammarParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BitTuneGrammarParser.NOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECT(self):
            return self.getToken(BitTuneGrammarParser.RECT, 0)

        def OVAL(self):
            return self.getToken(BitTuneGrammarParser.OVAL, 0)

        def LINE(self):
            return self.getToken(BitTuneGrammarParser.LINE, 0)

        def DOTS(self):
            return self.getToken(BitTuneGrammarParser.DOTS, 0)

        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_shapeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeName" ):
                listener.enterShapeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeName" ):
                listener.exitShapeName(self)




    def shapeName(self):

        localctx = BitTuneGrammarParser.ShapeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_shapeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BitTuneGrammarParser.RECT) | (1 << BitTuneGrammarParser.OVAL) | (1 << BitTuneGrammarParser.LINE) | (1 << BitTuneGrammarParser.DOTS))) != 0)):
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


    class EndShapeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE_BRACKET(self):
            return self.getToken(BitTuneGrammarParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_endShape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndShape" ):
                listener.enterEndShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndShape" ):
                listener.exitEndShape(self)




    def endShape(self):

        localctx = BitTuneGrammarParser.EndShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_endShape)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(BitTuneGrammarParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(BitTuneGrammarParser.COMMENT, 0)

        def getRuleIndex(self):
            return BitTuneGrammarParser.RULE_commentSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentSequence" ):
                listener.enterCommentSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentSequence" ):
                listener.exitCommentSequence(self)




    def commentSequence(self):

        localctx = BitTuneGrammarParser.CommentSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_commentSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(BitTuneGrammarParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





