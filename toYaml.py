from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsonParser import jsonParser
else:
    from jsonParser import jsonParser

from jsonListener import jsonListener

class toYaml(jsonListener):

    def __init__(self, output):
        self.output = output
        self.counter = 0
        self.first = True
        self.firstPair = True
        self.firstArrayValue = True

    # Enter a parse tree produced by jsonParser#json.
    def enterJson(self, ctx:jsonParser.JsonContext):
        pass

    # Exit a parse tree produced by jsonParser#json.
    def exitJson(self, ctx:jsonParser.JsonContext):
        self.output.write("\n")

    # Enter a parse tree produced by jsonParser#obj.
    def enterObj(self, ctx:jsonParser.ObjContext):
        keys = [p.pairFirst().getText() for p in ctx.pair()]

        if len(keys) != len(set(keys)):
            raise Exception("Clave repetida")
        else:
            self.firstPair = True

    # Exit a parse tree produced by jsonParser#obj.
    def exitObj(self, ctx:jsonParser.ObjContext):
        pass

    def enterCollection(self, ctx:jsonParser.CollectionContext):
        empty = None
        collectionValues = None
        if ctx.obj():
            collectionValues = [p for p in ctx.obj().pair()]
            empty = '{}'
        elif ctx.arr():
            collectionValues = [p for p in ctx.arr().valueArray()]
            empty = '[]'

        if collectionValues == []:
            self.output.write(empty)
        else:
            if not self.first:
                self.output.write('\n')
                self.counter = self.counter + 2
            else:
                self.first = False

    def exitCollection(self, ctx:jsonParser.CollectionContext):
        self.counter = self.counter - 2

    # Enter a parse tree produced by jsonParser#pair.
    def enterPair(self, ctx:jsonParser.PairContext):
        if self.firstPair:
            self.firstPair = False
        else:
            self.output.write('\n')

        self.output.write(' ' * self.counter)

    def enterValueArray(self, ctx:jsonParser.ValueArrayContext):
        if self.firstArrayValue:
            self.firstArrayValue = False
        else:
            self.output.write('\n')

        self.output.write(' ' * self.counter +  '-')

    def exitValueArray(self, ctx:jsonParser.ValueArrayContext):
        pass
    # Exit a parse tree produced by jsonParser#pair.
    def exitPair(self, ctx:jsonParser.PairContext):
        pass

     # Exit a parse tree produced by jsonParser#pair.
    def exitPairFirst(self, ctx:jsonParser.PairContext):
        self.output.write(': ')

    # Enter a parse tree produced by jsonParser#arr.
    def enterArr(self, ctx:jsonParser.ArrContext):
        self.firstArrayValue = True

    # Exit a parse tree produced by jsonParser#arr.
    def exitArr(self, ctx:jsonParser.ArrContext):
        pass

    # Enter a parse tree produced by jsonParser#value.
    def enterValue(self, ctx:jsonParser.ValueContext):
        pass

    # Exit a parse tree produced by jsonParser#value.
    def exitValue(self, ctx:jsonParser.ValueContext):
        #self.output.write("\n")
        pass


    # Enter a parse tree produced by jsonParser#string.
    def enterString(self, ctx:jsonParser.StringContext):
        str = ctx.STRING().getText()
        if not ('-' in str or '\\n' in str):
            str = str.replace('"','')
        self.output.write(str)

    # Exit a parse tree produced by jsonParser#string.
    def exitString(self, ctx:jsonParser.StringContext):
        pass

    # Enter a parse tree produced by jsonParser#num.
    def enterNum(self, ctx:jsonParser.NumContext):
        self.output.write(ctx.NUMBER().getText())


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
        self.output.write('')

    # Exit a parse tree produced by jsonParser#nil.
    def exitNil(self, ctx:jsonParser.NilContext):
        pass
