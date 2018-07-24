from antlr4.error.ErrorListener import ErrorListener

token_names = {}
lines = []
with open('json.tokens', 'r') as f:
    lines = f.readlines()

for line in lines[10:]:
    value, key = line.split("=")
    token_names[int(key)] = value


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

        print("Se esperaba un", tipo_regla[tipo])

        if tipo == "arr":
            if offendingSymbol.text == "<EOF>" :
                print("posiblemente falte agregar un ']'")
            else:
                print("los valores de un arreglo deben ir separados por ','")
        elif tipo == "obj":
            if offendingSymbol.text == "<EOF>" :
                print("posiblemente falte agregar un '}'")
            elif "getExpectedTokens" in dir(e):
                tokens = ["'" + token_names[token_num].lower() + "'" for token_num in
                    e.getExpectedTokens()]
                tokens = []
                for token_num in e.getExpectedTokens():
                    try:
                        tokens.append(
                            "'" +
                            token_names[token_num].lower().replace("'", "")
                            + "'")
                    except KeyError:
                        pass

                print("posiblemente falta:", " o ".join(tokens))
                print("se encontró:", "'"+ offendingSymbol.text + "'" )
            else:
                print("se esperaba un '}' o una ','",
                ", en cambio se encontró:", "'"+ offendingSymbol.text + "'" )
        elif tipo == "pair":
            if offendingSymbol.text == "<EOF>" :
                print("los pares deben ser de la forma 'clave: valor'")
        elif tipo == "string":
            print("en cambio se encontró:", "'"+ offendingSymbol.text + "'",
            "que no es un string válido")
        elif tipo == "value":
            if offendingSymbol.text != "<EOF>" :
                print("pero se encontró:", "'"+ offendingSymbol.text + "'" )
        else:
            pass

        exit()
