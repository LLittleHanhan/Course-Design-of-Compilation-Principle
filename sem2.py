class State():
    START="start"
    ASSIGN="assign"
    COMMENT="comment"
    NUM="num"
    ID="id"
    CHAR="char"
    RANGE="range"
    DONE="done"
class tokenType():
    PROGRAM = "PROGRAM"
    TYPE = "TYPE"
    VAR ="VAR"
    PROCEDURE = "PROCEDURE"
    BEGIN = "BEGIN"
    END = "END"
    ARRAY = "ARRAY"
    OF="OF"
    RECORD="RECORD"
    IF="IF"
    THEN="THEN"
    ELSE="ELSE"
    FI="FI"
    WHILE="WHILE"
    DO="DO"
    ENDWH="ENDWH"
    READ="READ"
    WRITE="WRITE"
    RETURN="RETURN"
    INTEGER="INTEGER"
    INTC = "INTC"
    CHAR="CHAR"
    ADD="+"
    SUB="-"
    MUL="*"
    DIV="/"
    LESS="<"
    EQUAL="="
    LEFT_PARENT="("
    RIGHT_PARENT=")"
    LEFT_BRACKET="{"
    RIGHT_BRACKET="}"
    DOT="."
    SEMICOLON=";"
    EOF="EOF"
    SPACE=" "
    COLON_EQUAL=":="
    LEFT_BRACES="["
    RIGHT_BRACES="]"
    APOSTROPHE="'"
    TWO_DOT=".."
    COMMA=","
    IDENTIFIERS="ID"
    KEYWORDS = ["repeat", "program", "type", "var", "procedure", "begin", "end", "array", "of", "record", "if", "then",
                "else", "fi", "while", "do", "endwh", "read", "write", "return", "integer", "char"]
    Types = ["repeat", "program", "type", "var", "procedure", "begin", "end", "array", "of", "record", "if", "then",
                "else", "fi", "while", "do", "endwh", "read", "write", "return", "integer", "char","intc",
             "+","-","*","/","<","=","(",")","{","}","[","]",".",";","EOF"," ",":=","'","..",",","ID"]

class Token():
    tokentype = ""
    value = ""
    line = 0
    def __init__(self,tokentype,value,line):
        self.tokentype = tokentype
        self.value = value
        self.line = line
import sys

def Scan(scanner):
    state = State.START
    tokenList = list()
    line = 1
    nxt = 0
    length = len(scanner)
    while nxt<length:
        if state == State.START:
            nxtChar = scanner[nxt]
            # print(nxtChar.isalpha())
            while nxt < length and (nxtChar == ' ' or nxtChar == '\n' or nxtChar == '\r' or nxtChar == '\t'):
                if nxtChar == '\n':
                    line += 1
                nxt += 1
                if nxt == length:
                    break
                nxtChar = scanner[nxt]
            if nxt == length:
                break
            if nxtChar.isalpha() or nxtChar == '_':
                state = State.ID
            elif nxtChar.isnumeric():
                state = State.NUM
            else:
                if nxtChar == '.' and scanner[nxt+1] == '.':
                    nxt += 1
                    nxtChar = ".."
                elif nxtChar == ":" and scanner[nxt+1] =='=':
                    nxt +=1
                    nxtChar = ":="
                elif nxtChar == "{":
                    while nxtChar != "}":
                        nxt += 1
                        nxtChar = scanner[nxt]
                    nxt += 1
                    nxtChar = scanner[nxt]
                    state = State.START
                    continue

                if nxtChar in tokenType.Types:
                    tokenList.append((nxtChar,nxtChar,line))
                    # print(tokenList)
                    nxt += 1
                    state = State.START
                else:
                    print(nxt,nxtChar,state,"error",line,scanner[nxt:])
                    break
        elif state == State.ID: # id
            currentId = ""
            nxtChar = scanner[nxt]
            while nxt < len(scanner) and (nxtChar.isalpha() or nxtChar.isnumeric() or nxtChar == '_'):
                currentId += nxtChar
                nxt += 1
                if nxt == length:
                    break
                nxtChar = scanner[nxt]
            if currentId.lower() in tokenType.KEYWORDS:
                tokenList.append((currentId.upper(),currentId,line))
            else:
                tokenList.append((tokenType.IDENTIFIERS,currentId,line))
            state = State.START
        elif state == State.NUM:
            currentNum = ""
            nxtChar = scanner[nxt]
            while nxt<len(scanner) and nxtChar.isnumeric():
                currentNum += nxtChar
                nxt += 1
                if nxt == length:
                    break
                nxtChar = scanner[nxt]
            tokenList.append((tokenType.INTC,int(currentNum),line))
            state = State.START
    return tokenList