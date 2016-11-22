import sys
import io
inputsofar = []
inputfile = ""
currentFname = ""
nextidx = 0
peekchar = ""
peekchar2 = ""

def setFile(fname):
    global inputfile, nextidx, inputsofar, currentFname
    inputfile = open(fname, "r")
    nextidx = 0
    inputsofar = []
    currentFname = fname.split("/")[-1]

def getFilename():
	global currentFname
	return currentFname
	
def setSaveFile(path):
    sys.stdout.close()
    sys.stdout = open(path,"w")

    
def peek():
    global inputfile, peekchar
    if peekchar == "":
        peekchar = inputfile.read(1)
    return peekchar

def consume():
    global inputfile, peekchar, peekchar2
    if peekchar == "":
        peekchar = inputfile.read(1)
    rval = peekchar
    peekchar = peekchar2
    peekchar2 = ""
    return rval


def eatUntilNextToken():
    global inputfile, peekchar, peekchar2
    if peekchar == "":
        peekchar = inputfile.read(1)
    if peekchar2 == "":
        peekchar2 = inputfile.read(1)
    while (peekchar == "/" and (peekchar2 == "/" or peekchar2 == "*")) or peekchar.isspace():
        if peekchar == "/" and peekchar2 == "/":
            while peekchar != "\n":
                consume()
                peek()
            consume()
        elif peekchar == "/" and peekchar2 == "*":
            while not (peekchar == "*" and peekchar2 == "/"):
                consume()
                peekchar2 = inputfile.read(1)
            consume()
            consume()
        else:
            while peekchar.isspace():
                consume()
        if peekchar == "":
            peekchar = inputfile.read(1)
        if peekchar2 == "":
            peekchar2 = inputfile.read(1)
        
    