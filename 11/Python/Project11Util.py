# The Tokenizer Module
import Project11IO as IO


#Like the parser modules from earlier Projects, the Tokenizer
# will advance one token at a time, and populate these global
# variables.
nextType=""
nextInt=""
nextString=""
nextSymbol=""
nextKW=""
nextID=""

#A function to check whether there are more tokens.
def hasMoreTokens():
    global line
    if line == "EOF":
        return False
    else:
        return True

#Consumes characters until 
# the next character in the stream is c.
#Returns a string containing all the characters
# that were consumed.
def eatUntil(c):
    s = ""
    while IO.peek() != c:
        s = s+IO.peek()
        IO.consume()
    return s

#This function should be called when
# the next token is a string. It consumes
# everything between the next two quotation marks, including the quotes.
# After the function is called, nextType should be STRING_CONST
# and nextSTring should be whatever was between the quotes.
def consumeString():
    global nextType, nextString
    s = ""
    IO.consume() #eat the first quote.
    while IO.peek() != '"':
        s = s+IO.peek()
        IO.consume()
    IO.consume() #eat the trailing quote.
    nextType = "STRING_CONST"
    nextString = s
    
#This function should be called when
# the next token is a integer. It consumes
# everything up to, but not including, the next non-numeric character.
# After the function is called, nextType should be INT_CONST
# and nextInt should be all the numbers that were consumed.  
def consumeInt():
    global nextType, nextInt
    s = ""
    while IO.peek().isdigit():
        s = s + IO.peek()
        IO.consume()
    nextType = "INT_CONST"
    nextInt = int(s)

#This function peeks at the next character to check whether the 
# next token is a Symbol. A symbol is any character that isn't 
# a number, letter, or underscore. The function returns True
# if the next token is a symbol, and False otherwise.
def isSymbol():
    s = IO.peek()
    if not IO.peek().isalnum() and s != "_":
        return True
    else:
        return False
    
#This function should be called when
# the next token is a symbol. It consumes only the next character.
# After the function is called, nextType should be SYMBOL
# and nextSymbol should be the consumed character.
def consumeSymbol():
    global nextSymbol, nextType
    nextType = "SYMBOL"
    nextSymbol = IO.peek()
    IO.consume()

#This function should be called when
# the next token is either a Keyword or an Identifier. It consumes 
# everything up to the next character that is not a letter, number or _.
# After the function is called, if the consumed characters form a keyword,
# nextType should be KEYWORD, and nextKW should be equal to the consumed 
# string. Otherwise, nextType should be IDENTIFIER, and nextID should be 
# equal to the consumed string.
def consumeKWorID():
    global nextID, nextType, nextKW
    s = ""
    while IO.peek().isalpha() or IO.peek().isdigit() or IO.peek() == "_":
        s = s + IO.peek()
        IO.consume()

    KWlist = ['class', 'constructor', 'function', 'method', 'field', 
              'static', 'var', 'int', 'char', 'boolean', 'void',
              'true', 'false', 'null', 'this', 'let', 'do', 'if', 
              'else', 'while', 'return']      
    if s in KWlist:
        nextKW = s
        nextType = "KEYWORD"
    else:
        nextID = s
        nextType = "IDENTIFIER"
    

#When this function is called any whitespace before the next token is consumed,
#and then the next token is consumed, and the global variables are populated 
# accordingly.
def advance():    
    #Eat any leading whitespace or comments
    IO.eatUntilNextToken()
    
    #Use the first charactor to decide what to consume next.
    firstChar = IO.peek()    
    if firstChar == '"':
        consumeString()
    elif firstChar.isdigit():
        consumeInt()
    elif isSymbol():
        consumeSymbol()
    else:
        consumeKWorID()

#The remaining functions simply provide a way to access
# the populated global variables, and print error messages
# if they are accessed improperly.
def tokenType():
    global nextType
    return nextType
    
def keyword():
    global nextType, nextKW
    if nextType == "KEYWORD":
        return nextKW
    else:
        raise("Value error! Called keyWord() on line: " +IO.currentLine())

def symbol():
    global nextSymbol, nextType
    if nextType == "SYMBOL":
        return nextSymbol
    else:
        raise("Value error! Called symbol() on line: " +IO.currentLine())


def identifier():
    global nextID, nextType
    if nextType == "IDENTIFIER":
        return nextID
    else:
        raise("Value error! Called identifier() on line: " +IO.currentLine())


def intVal():
    global nextInt, nextType
    if nextType == "INT_CONST":
        return str(nextInt)
    else:
        raise("Value error! Called intVal() on line: " +IO.currentLine())


def stringVal():
    global nextString, nextType
    if nextType == "STRING_CONST":
        return nextString
    else:
        raise("Value error! Called stringVal() on line: " +IO.currentLine())

                             
#Utilities Module
#This module contains a number of functions that will
# be exceedingly useful when we write the Parser.
#These functions do not need to be modified, and only the top four will 
# be directly used in the next section. Make sure you understand what 
# the top four do though, and how to use them.

#verifyToken accepts two arguments, ttype and token.
# If the next token is of type ttype, and has exactly 
# the same value as the token argument, then the token is
# consumed, and printed using the printTerminal command.
# Otherwise, the program halts by calling compileError.
# The type is not case sensitive. 
# Example: verifyToken("SYMBOL", ";")
# Example: verifyToken("keyword", "while")
def verifyToken(ttype, token="", peek=False):
    result = ""
    if tokenType() != ttype.upper() or (getNextToken() != token and token != ""):
        if not peek:
            compileError(ttype,token)
        return False
    else:
        if not peek:
            rval = getNextToken()
            advance()
            return rval
        return True

#peekToken returns true if the next token matches the 
# type and value of the passed arguments. The token type
# is not case sensitive.
# Example: if peekToken("symbol", ";"):
#              //do something if the next token is ';'.
#          else
#              //do something if the next token is not ';'.
def peekToken(ttype, tvalue):
    return verifyToken(ttype, tvalue, peek=True)
    
#Like verifyToken, but tokenList should be a list of possible
# token values, and the program will halt with an error if 
# the next token is _none_ of the listed values.
# Example: verifyTokenList("keyword", ["let", "do", "if", "while", "return"])
def verifyTokenList(ttype, tokenList, peek=False):
    for t in tokenList:
        if peekToken(ttype, t):
            if not peek:
                rval=getNextToken()
                advance()
                return rval
            return True
    if not peek:
        compileError(ttype, tokenList)
    return False

#List peekToken, but returns true if _any_ of the values in
# tvalueList match the next token, and the next token is of the
# listed type.
def peekTokenList(ttype, tvalueList):
    return verifyTokenList(ttype, tvalueList, peek=True)


#Returns the next token, whatever it is.
def getNextToken():
    if tokenType() == "STRING_CONST":
        return stringVal()
    if tokenType() == "INT_CONST":
         return intVal()
    if tokenType() == "IDENTIFIER":
        return identifier()
    if tokenType() == "SYMBOL":
        return symbol()    
    if tokenType() == "KEYWORD":
        return keyword()
    return "ERROR!!!"

#Halts the program and prints an error message.
def compileError( ttype, token):
    s = "Compilation error. Expected token \"" + token + "\" of type \"" + ttype + "\"\n"
    s = s + "Found token type \""+tokenType() + "\" with value \""
    s = s + getNextToken() + "\""
    raise ValueError(s)   

#Prints a terminal value in the correct format
# <type> value </type>
def printTerminal(ttype, token):
    if token == "<":
        token = "&lt;"
    if token == ">":
        token = "&gt;"
    if token == "&":
        token = "&amp;"
    if ttype == "string_const":
        ttype = "stringConstant"
    if ttype == "int_const":
        ttype = "integerConstant"
    print("<"+ttype+"> "+token+" </"+ttype+">")
    
