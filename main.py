import sys
from antlr4 import *
from jsonLexer import jsonLexer
from jsonParser import jsonParser
from toYaml import toYaml
from jsonListener import jsonListener

def main(filename):
    input = FileStream(filename)
    lexer = jsonLexer(input)
    stream = CommonTokenStream(lexer)
    parser = jsonParser(stream)
    tree = parser.json()

    output = sys.stdout

    converter = toYaml(output)
    listener = jsonListener()
    walker = ParseTreeWalker()
    walker.walk(converter, tree)

if __name__ == '__main__':
    main(sys.argv[1])
