// File name: projects/04/Fill.asm

(OFF)
@KBD
D=M
@OFF
D;JEQ

(ON)
@SCREEN
D=A
@0
M=D
(BLACK)
@0
A=M
M=-1

@0
D=M+1
M=M+1

@KBD
D=A-D

@BLACK
D;JGT

(WAIT)
@KBD
D=M
@WAIT
D;JNE

@SCREEN
D=A
@0
M=D
(WHITE)
@0
A=M
M=0

@0
D=M+1
M=M+1

@KBD
D=A-D

@WHITE
D;JGT
@OFF
0;JMP