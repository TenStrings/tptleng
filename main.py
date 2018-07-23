#!/usr/bin/env python3
import sys
from antlr4 import *
from jsonLexer import jsonLexer
from jsonParser import jsonParser
from toYaml import toYaml
from jsonListener import jsonListener
from JsonParserCustomError import *
from antlr4.error.ErrorListener import ErrorListener
import codecs

import sys

class CustomErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        lista = recognizer.getRuleInvocationStack()
        tipo = lista[0]
        print(lista)
        print(  "Error de parseo en línea",
                line, ":", column)

        if offendingSymbol.text == "<EOF>":
            print("La entrada terminó de manera inesperada")

        print("Se estaba parseando un:", tipo)

        if(tipo == "arr"):
            print("posiblemente falte agregar un ']'")

        exit()

class StdinStream(InputStream):

    def __init__(self, encoding='utf-8', errors='strict'):
        bytes = sys.stdin.read()
        super().__init__(bytes)


def main(filename = None):
    if filename:
        input = FileStream(filename)
    else:
        input = StdinStream()
    lexer = jsonLexer(input)
    stream = CommonTokenStream(lexer)
    parser = jsonParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    tree = parser.json()

    output = sys.stdout

    converter = toYaml(output)
    walker = ParseTreeWalker()
    walker.walk(converter, tree)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
