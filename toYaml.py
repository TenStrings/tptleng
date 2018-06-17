from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsonParser import jsonParser
else:
    from jsonParser import jsonParser

from jsonListener import jsonListener

class toYaml(jsonListener):
    def __init__(self, output):
        self.output = output

    def enterJson(self, ctx:jsonParser.JsonContext):
        pass

    # Exit a parse tree produced by jsonParser#json.
    def exitJson(self, ctx:jsonParser.JsonContext):
        pass

    def enterObj(self, ctx:jsonParser.ObjContext):
        keys = [p.STRING().getText() for p in ctx.pair()]
        if len(keys) != len(set(keys)):
            raise Exception("Clave repetida")
    
    def exitObj(self, ctx:jsonParser.ObjContext):
        pass

    def enterPair(self, ctx:jsonParser.PairContext):
        pass

    def exitPair(self, ctx:jsonParser.PairContext):
        pass

    def enterArr(self, ctx:jsonParser.ArrContext):
        pass

    def exitArr(self, ctx:jsonParser.ArrContext):
        pass

    def enterValue(self, ctx:jsonParser.ValueContext):
        pass

    def exitValue(self, ctx:jsonParser.ValueContext):
        pass
