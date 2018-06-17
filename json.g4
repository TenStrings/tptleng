grammar json;

//PARSER RULES

json : value EOF;

object : 
    '{}' |
    '{' pair (',' pair)* '}';

pair :
    STRING ':' value;

array :
    '[]' | '[' value (',' value)* ']';

value :
    STRING | NUMBER | object | array | 'true' | 'false' | 'null';

//LEXER RULES

fragment DIGIT : [0-9];

WHITESPACE : [ \n\t\r]+ -> skip;

NUMBER :
        INT FRAC? EXP?;

INT :
    '-'? DIGIT |
    '-'? [1-9][0-9]*;

FRAC :
    '.' DIGIT*;

EXP :
    [eE][+\-]? DIGIT*;

fragment INVALID :
    ~ ["\u0000-\u001f\\]; 

fragment ESCAPED :
    '\\' ["\\/bfnrt];

fragment HEX :
    [0-9a-fA-F];

fragment STRINGUNICODE:
    '\\u' HEX HEX HEX HEX;

STRING :
    '"' ( INVALID | ESCAPED | STRINGUNICODE )* '"';
