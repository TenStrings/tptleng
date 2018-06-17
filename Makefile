antlr4 = java -jar /usr/local/lib/antlr-4.7.1-complete.jar
grammar = ./json.g4

main: $(grammar) 
	$(antlr4) -Dlanguage=Python3 $<

.PHONY: clean

clean:
	rm -f jsonLexer.* jsonParser.py json.interp json.tokens jsonListener.py 
