from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsonParser import jsonParser
else:
    from jsonParser import jsonParser

from jsonListener import jsonListener

class toYaml(jsonListener):

    def __init__(self, output):
        self.output = output

    # Enter a parse tree produced by jsonParser#json.
    def enterJson(self, ctx:jsonParser.JsonContext):
        pass

    # Exit a parse tree produced by jsonParser#json.
    def exitJson(self, ctx:jsonParser.JsonContext):
        self.output.write("\n") 


    # Enter a parse tree produced by jsonParser#obj.
    def enterObj(self, ctx:jsonParser.ObjContext):
        keys = [p.STRING().getText() for p in ctx.pair()]
        if len(keys) != len(set(keys)):
            raise Exception("Clave repetida")

    # Exit a parse tree produced by jsonParser#obj.
    def exitObj(self, ctx:jsonParser.ObjContext):
        pass


    # Enter a parse tree produced by jsonParser#pair.
    def enterPair(self, ctx:jsonParser.PairContext):
        pass

    # Exit a parse tree produced by jsonParser#pair.
    def exitPair(self, ctx:jsonParser.PairContext):
        pass


    # Enter a parse tree produced by jsonParser#arr.
    def enterArr(self, ctx:jsonParser.ArrContext):
        pass

    # Exit a parse tree produced by jsonParser#arr.
    def exitArr(self, ctx:jsonParser.ArrContext):
        pass


    # Enter a parse tree produced by jsonParser#value.
    def enterValue(self, ctx:jsonParser.ValueContext):
        pass

    # Exit a parse tree produced by jsonParser#value.
    def exitValue(self, ctx:jsonParser.ValueContext):
        pass


    # Enter a parse tree produced by jsonParser#string.
    def enterString(self, ctx:jsonParser.StringContext):
        pass

    # Exit a parse tree produced by jsonParser#string.
    def exitString(self, ctx:jsonParser.StringContext):
        pass


    # Enter a parse tree produced by jsonParser#num.
    def enterNum(self, ctx:jsonParser.NumContext):
        pass

    # Exit a parse tree produced by jsonParser#num.
    def exitNum(self, ctx:jsonParser.NumContext):
        pass

    # Enter a parse tree produced by jsonParser#tr.
    def enterTr(self, ctx:jsonParser.TrContext):
        self.output.write(ctx.getText()) 

    # Exit a parse tree produced by jsonParser#tr.
    def exitTr(self, ctx:jsonParser.TrContext):
        pass


    # Enter a parse tree produced by jsonParser#fs.
    def enterFs(self, ctx:jsonParser.FsContext):
        self.output.write(ctx.getText())

    # Exit a parse tree produced by jsonParser#fs.
    def exitFs(self, ctx:jsonParser.FsContext):
        pass


    # Enter a parse tree produced by jsonParser#nil.
    def enterNil(self, ctx:jsonParser.NilContext):
        self.output.write(ctx.getText()) 

    # Exit a parse tree produced by jsonParser#nil.
    def exitNil(self, ctx:jsonParser.NilContext):
        pass


