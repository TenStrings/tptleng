#!/usr/bin/env python3
import sys
from antlr4 import *
from jsonLexer import jsonLexer
from jsonParser import jsonParser
from toYaml import toYaml
from jsonListener import jsonListener
from CustomErrorListener import CustomErrorListener
from CustomLexerErrorListener import CustomLexerErrorListener
import codecs

import sys

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
    try:
        walker.walk(converter, tree)
    except Exception as error:
        print("Error de traducción:", error)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
