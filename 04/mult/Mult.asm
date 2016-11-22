// projects/04/Mult.asm

@2
M=0

@0
D=M
@END
D;JEQ

(LOOP)
@1
D=M
@2
M=M+D
@0
M=M-1
D=M
@LOOP
D;JGT

@END
(END)
0; JMP