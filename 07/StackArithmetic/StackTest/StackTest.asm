@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP0
D;JEQ
@SP
A=M
M=0
@JMP1
0;JMP
(JMP0)
@SP
A=M
M=-1
(JMP1)
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP2
D;JEQ
@SP
A=M
M=0
@JMP3
0;JMP
(JMP2)
@SP
A=M
M=-1
(JMP3)
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP4
D;JEQ
@SP
A=M
M=0
@JMP5
0;JMP
(JMP4)
@SP
A=M
M=-1
(JMP5)
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP6
D;JLT
@SP
A=M
M=0
@JMP7
0;JMP
(JMP6)
@SP
A=M
M=-1
(JMP7)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP8
D;JLT
@SP
A=M
M=0
@JMP9
0;JMP
(JMP8)
@SP
A=M
M=-1
(JMP9)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP10
D;JLT
@SP
A=M
M=0
@JMP11
0;JMP
(JMP10)
@SP
A=M
M=-1
(JMP11)
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP12
D;JGT
@SP
A=M
M=0
@JMP13
0;JMP
(JMP12)
@SP
A=M
M=-1
(JMP13)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP14
D;JGT
@SP
A=M
M=0
@JMP15
0;JMP
(JMP14)
@SP
A=M
M=-1
(JMP15)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
A=M
D=A-D
@JMP16
D;JGT
@SP
A=M
M=0
@JMP17
0;JMP
(JMP16)
@SP
A=M
M=-1
(JMP17)
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M+D
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M-D
@SP
A=M-1
M=-M
@SP
AM=M-1
D=M
A=A-1
M=M&D
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M|D
@SP
A=M-1
M=!M
