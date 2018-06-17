antlr4 = java -jar /usr/local/lib/antlr-4.7.1-complete.jar
grammar = ./json.g4
main: $(grammar) 
	$(antlr4) $< && javac json*.java

test:
	java org.antlr.v4.gui.TestRig json value -tokens

.PHONY: clean

clean:
	rm -f *.java *.class *.interp *.tokens
