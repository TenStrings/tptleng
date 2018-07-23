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

        tipo_regla = {
            'arr': 'arreglo',
            'obj': 'objeto',
            'value': 'valor',
            'pair': 'par',
            'string' : 'string'

        }

        print(  "Error de parseo en línea",
                line, ":", column)

        if offendingSymbol.text == "<EOF>":
            print("La entrada terminó de manera inesperada")

        print("Se estaba parseando un", tipo_regla[tipo])

        if tipo == "arr":
            if offendingSymbol.text == "<EOF>" :
                print("posiblemente falte agregar un ']'")
            else:
                print("los valores de un arreglo deben ir separados por ','")
        elif tipo == "obj":
            if offendingSymbol.text == "<EOF>" :
                print("posiblemente falte agregar un '}'")
            else:
                print("los pares deben ir separados por ','")
        elif tipo == "pair":
            if offendingSymbol.text == "<EOF>" :
                print("los pares deben ser de la forma 'clave: valor'")
        elif tipo == "string":        
            print("la clave debe ser un string")
        else:
            print("la clave debe ir seguida de ':' y el valor")

        exit()

class CustomLexerErrorListener(ErrorListener):
    def syntaxError(self, lexer, offendingSymbol, line, column, msg, e):
        token = msg.split("'")[1]
        print("Error: Token inválido", token)
        print("Línea",line,":", column)
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
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomLexerErrorListener())
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
