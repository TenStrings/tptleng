antlr4 = java -jar /usr/local/lib/antlr-4.7.1-complete.jar
main: json.g4
	$(antlr4) $< && javac json*.java
