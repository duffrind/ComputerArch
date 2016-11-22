import sys
inputsofar = []
inputfile = ""
currentFname = ""
nextidx = 0

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

def rewind():
    global nextidx
    nextidx = 0
    
def nextLine():
    global nextidx, inputsofar, inputfile
    if nextidx < len(inputsofar):
        nextidx = nextidx+1
        return inputsofar[nextidx-1]
    elif len(inputsofar) > 0 and inputsofar[-1] == "EOF":
        return "EOF"
    else:
        line = ""
        while True:
            if inputfile == "":
                line = input()
            else:
                line = inputfile.readline()
            if line.strip()[0:2] != "//" and (len(line) == 0 or line.strip()!="") :
                break
        if line == "":
            line = "EOF"
        if line.find("//") != -1:
            line = line[0:line.find("//")]
        line = line.strip()
        inputsofar.append(line.strip())
        nextidx = nextidx+1
        return line.strip()
        
def printAddress(s):
    print(bin(int(s))[2:].zfill(16))
        
def printCommand(f,c,d,j):
    print(f, end="")
    print(c, end="")
    print(d, end="")
    print(j)      

