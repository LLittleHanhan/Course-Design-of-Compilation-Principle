#张小北

class lex:
    #保留字
    reserved_words={"program": 'PROGRAM',"type": 'TYPE',
                    "var": 'VAR',"procedure": 'PROCEDURE',
                    "begin": 'BEGIN',"end": 'END',
                    "array": 'ARRAY',"of": 'OF',
                    "record": 'RECORD',"if": 'IF',
                    "then": 'THEN',"else": 'ELSE',
                    "fi": 'FI',"char": 'CHAR_T',
                    "while": 'WHILE',"do": 'DO',
                    "endwh": 'ENDWH',"read": 'READ',
                    "write": 'WRITE', "return": 'RETURN',
                    "integer": 'INTEGER_T'}
    lex_tag={'PROGRAM': "PROGRAM",'TYPE': "TYPE",
             'VAR': "VAR",'PROCEDURE': "PROCEDURE",
             'BEGIN': "BEGIN",'END': "END",
             'ARRAY': "ARRAY",'OF': 'OF',
             'RECORD': "RECORD",'IF': "IF",
             'THEN': "THEN",'ELSE': "ELSE",
             'FI': "FI",'WHILE': "WHILE",
             'DO': "DO",'ENDWH': "ENDWH",
             'READ': "READ",'WRITE': "WRITE",
             'RETURN': "RETURN",'INTEGER_T': "INTEGER",
             'CHAR_T': "CHAR",'ID': "ID",
             'INTC_VAL': "INTC_VAL",'CHARC_VAL': "CHAR_VAL",
             'ASSIGN': ":=",'EQ': "=",
             'LT': "<",'PLUS': "+",
             'MINUS': "-",'TIMES': "*",
             'DIVIDE': "/",'LPAREN': "(",
             'RPAREN': ")",'DOT': ".",
             'COLON': ":",'SEMI': ";",
             'COMMA': ",",'LMIDPAREN': "[",
             'RMIDPAREN': "]",'UNDERRANGE': "..",
             'ENDFILE': "EOF",'ERROR': "ERROR"}

    # 程序
    content=''

    def __init__(self,content):
        self.content=content

    def is_reserved(self,ch):
        return ch in self.reserved_words.keys()

    #def scan(self,ch):
        #if(ch.isalpha()):



l=lex('a')
print(l.is_reserved('endwh'))