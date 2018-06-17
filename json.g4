grammar json;

//PARSER RULES

json : value EOF;

object : 
    '{}' |
    '{' members '}';

members :
    pair | pair ',' members;

pair :
    STRING ':' value;

array :
    '[]' | '[' elements ']';

elements :
    value
    value ',' elements;

value :
    STRING | NUMBER | object | array | 'true' | 'false' | 'null';

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

fragment CONTROL :
    ~ ["\u0000-\u001f\\]; 

fragment ESCAPED :
    '\\' ["\\/bfnrt];

fragment HEX :
    [0-9a-fA-F];

STRING :
    '"' ( CONTROL | ESCAPED )* '"';
