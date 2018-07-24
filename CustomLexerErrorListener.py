from antlr4.error.ErrorListener import ErrorListener

class CustomLexerErrorListener(ErrorListener):
    def syntaxError(self, lexer, offendingSymbol, line, column, msg, e):
        token = msg.split("'")[1]
        print("Error: Token inválido", token)
        print("Línea",line,":", column)
        exit()
