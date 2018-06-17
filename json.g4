grammar json;

//PARSER RULES

text : NUMBER (' ' | EOF);
//LEXER RULES

fragment DIGIT : [0-9];

WHITESPACE : [\n\t\r]+ -> skip;

NUMBER :
        INT FRAC? EXP?;

INT :
    '-'? DIGIT |
    '-'? [1-9][0-9]*;

FRAC :
    '.' DIGIT*;

EXP :
    [eE][+-]? DIGIT*;
