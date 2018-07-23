from jsonParser import jsonParser
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys
from antlr4.error.Errors import RecognitionException, NoViableAltException, InputMismatchException, \
FailedPredicateException, ParseCancellationException


class CustomHandler ( DefaultErrorStrategy ):

    def reportError(self, recognizer:Parser, e:RecognitionException):

        self.beginErrorCondition(recognizer)

        if isinstance( e, NoViableAltException ):
            self.reportNoViableAlternative(recognizer, e)
        elif isinstance( e, InputMismatchException ):
            self.reportInputMismatch(recognizer, e)
        elif isinstance( e, FailedPredicateException ):
            self.reportFailedPredicate(recognizer, e)
        else:
            print("unknown recognition error type: " + type(e).__name__)
            recognizer.notifyErrorListeners(e.message, e.offendingToken, e)

    def reportInputMismatch(self, recognizer:Parser, e:InputMismatchException):

        offendingToken = e.offendingToken
        if offendingToken is None:
            offendingToken = recognizer.getCurrentToken()
    

        msg = "Error al parsear linea " + str(offendingToken.line) + ' columna ' + str(offendingToken.column) + " se esperaba un valor del siguiente tipo: " + e.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
        print(msg)
        exit()
        #recognizer.notifyErrorListeners(msg, e.offendingToken, e)


class JsonParserCustomError ( jsonParser ):

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self._errHandler = CustomHandler()
