# Simple logo parser assignment

Given a programming language, based on a subset of the Logo language, with the following commands:
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

When defining a new primitive with the 'TO' command, <id> which accepts the parameters defined in <optional_args>.
- The commands executed by the new primitive are defined in <body>. Each parameter is defined by ':<id>' (a colon followed by an identifier).
- Parameter values are accessed with ':<id>', the same format as the parameter declaration.


For example, the following program in Logo draws a square with edges of size 30 at position (20, 20):

```soon
TO SQUARE :length
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
END


SETXY 20 20
SQUARE 30
```

Write the production rules of a grammar, for the presented language, with the associated code for the execution of the parser, to implement an interpreter for the language.
For the graphic treatment, use the "Turtle" object, which has the following methods.
- set_position(X, Y): Positions the object at position (X, Y)
- draw_segment(angle, length): Draws a line segment with an angle (angle) with respect to the X axis.
- set_draw(state): If state is True, draw when moving, if False, move without drawing.
- clear(): Clears the entire drawn area.

- Grammar rule example:

```soon
program: { angle = 0 } statement other_statement
other_statement: statement other_statement | &
statement:
    FO num | FORWARD num { Turtle.draw_segment(angle, $num.value) }
```

## Grammar

The grammar was created using ANTLR4. The [logo.g4](./logo.g4) file contains all the grammar for the language.

## Running the interpreter

Install the required dependencies:

```shell
pip install -r requirements.txt
```

Run the interpreter:

```shell
python3 ./main.py
```