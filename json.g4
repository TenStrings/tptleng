grammar json;

//PARSER RULES

json : value EOF;

collection :
  obj | arr ;

obj :
    '{}' |
    '{' pair (',' pair)* '}';

pair :
    pairFirst ':' value;

pairFirst :
    string;

arr :
    '[]' | '[' valueArray (',' valueArray)* ']';

valueArray :
    value;

value :
    collection | string | num | tr | fs | nil;

string :
    STRING;

num :
    NUMBER;

tr :
    'true';

fs :
    'false';

nil :
    'null';

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
