grammar BitTuneGrammar ;

program: statement+ ;

statement : noteSequence | multiNoteSequence | shapeSequence | commentSequence ;

noteSequence : note ;
multiNoteSequence : number note ;
shapeSequence : shapeName (noteSequence | multiNoteSequence)+ endShape ;

number : INT ;
note : NOTE ;

shapeName : RECT | OVAL | LINE | DOTS ;
endShape : CLOSE_BRACKET ;

commentSequence : COMMENT ;

NOTE : [a-gA-GrR][a-gA-GrR]?[a-gA-GrR]?[a-gA-GrR]? ; // Note can be up to 4 instances of a-g or r for rest

RECT : 'rect(' ;
OVAL : 'oval(' ;
LINE : 'line(' ;
DOTS : 'dots(' ;

CLOSE_BRACKET : ')' ;

COMMENT : '//' ~[\r\n]* '\r'? '\n' -> skip ;

INT : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ; // skip tabs, spaces, and new lines