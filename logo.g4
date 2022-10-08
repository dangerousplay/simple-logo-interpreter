grammar logo;

/*
- FO <num> | FORWARD <num> : Moves the pen forward by a distance of <num> pixels.
- BK <num> | BACKWARD <num> : Moves the pen back by a distance of <num> pixels.
- RIGHT <angle> | RT <angle> : Rotates the pen <angle> degrees to the right.
- LEFT <angle> | LT <angle> : Rotates the pen <angle> degrees to the left.
- PENUP | PU : Does not draw while moving the pen.
- PENDOWN | PD : Draws while moving the pen.
- CLEARSCREEN | CS : Erases the screen and place the pen at the center position of the screen (0,0) and angle 0
- WIPECLEAN | WC : Erase the canvas
- SETXY <x> <y> : Positions the pen at the position (<x>,<y>)
- RANDOM : Returns a random integer number from 0 to 9.
- TO <id> <optional_ars> <body> END : Defines a new primitive.
*/

file_ : program EOF;

program
   : (invoke_command | function_declaration | invoke_function)+
   ;

invoke_function
   : IDENTIFIER (SCIENTIFIC_NUMBER*)
   ;

function_declaration
   : TO IDENTIFIER function_args_declaration function_body END
   ;

function_args_declaration
   : function_arg*
   ;

function_arg
   : (COLON IDENTIFIER | SCIENTIFIC_NUMBER)
   ;

function_body
   : (function_body_statement)*
   ;

function_body_statement
   : command_declare_invoke | function_declare_invoke
   ;

function_declare_invoke
   : IDENTIFIER (function_arg)*
   ;

command_declare_invoke
   : command
   ;

invoke_command
   : command
   ;

command
   : (forward | backward | left | right | penup | pendown | random | setxy | wipe_clean | clear_screen)
   ;

forward
   : FORWARD function_arg
   ;

backward
   : BACKWARD function_arg
   ;

left
   : LEFT function_arg
   ;

right
   : RIGHT function_arg
   ;

penup
   : PENUP
   ;

pendown
   : PENDOWN
   ;

setxy
   : SET_XY function_arg function_arg
   ;

random
   : RANDOM
   ;

wipe_clean
   : WIPE_CLEAN
   ;

clear_screen
   : CLEAR_SCREEN
   ;

RANDOM
   : R A N D O M
   ;

FORWARD
   : F O | F O R W A R D
   ;

BACKWARD
   : B K | B A C K W A R D
   ;

RIGHT
   : R T | R I G H T
   ;

LEFT
   : L T | L E F T
   ;

PENUP
   : P U | P E N U P
   ;

PENDOWN
   : P D | P E N D O W N
   ;

CLEAR_SCREEN
   : C S | C L E A R S C R E E N
   ;

WIPE_CLEAN
   : W C | W I P E C L E A N
   ;

SET_XY
   : S E T X Y
   ;

TO
   : T O
   ;

END
   : E N D
   ;

IDENTIFIER
   : VALID_ID_START VALID_ID_CHAR*
   ;

fragment VALID_ID_START
   : ('a' .. 'z') | ('A' .. 'Z') | '_'
   ;


fragment VALID_ID_CHAR
   : (('0' .. '9') | ('a' .. 'z') | ('A' .. 'Z') | '_' )
   ;

//The NUMBER part gets its potential sign from "(PLUS | MINUS)* atom" in the expression rule
SCIENTIFIC_NUMBER
   : NUMBER (E SIGN? UNSIGNED_INTEGER)?
   ;

fragment NUMBER
   : ('0' .. '9') + ('.' ('0' .. '9') +)?
   ;

fragment UNSIGNED_INTEGER
   : ('0' .. '9')+
   ;


fragment SIGN
   : ('+' | '-')
   ;

COMMA
   : ','
   ;

WS
   : [ \r\n\t] + -> skip
   ;


COLON            : ':' ;

fragment
A                : [Aa] ;

fragment
B                : [Bb] ;

fragment
C                : [Cc] ;

fragment
D                : [Dd] ;

fragment
E                : [Ee] ;

fragment
F                : [Ff] ;

fragment
G                : [Gg] ;

fragment
H                : [Hh] ;

fragment
I                : [Ii] ;

fragment
J                : [Jj] ;

fragment
K                : [Kk] ;

fragment
L                : [Ll] ;

fragment
M                : [Mm] ;

fragment
N                : [Nn] ;

fragment
O                : [Oo] ;

fragment
P                : [Pp] ;

fragment
Q                : [Qq] ;

fragment
R                : [Rr] ;

fragment
S                : [Ss] ;

fragment
T                : [Tt] ;

fragment
U                : [Uu] ;

fragment
V                : [Vv] ;

fragment
W                : [Ww] ;

fragment
X                : [Xx] ;

fragment
Y                : [Yy] ;

fragment
Z                : [Zz] ;
