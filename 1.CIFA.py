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
             'int': "INTC",'CHARC_VAL': "CHAR_VAL",
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
    line=0
    def __init__(self,content):
        self.content=content

    def is_reserved(self,ch):
        return ch in self.reserved_words.keys()

    def scan(self,ch):
        if ch=='\n': self.line+=1
        result={}
        Len = ch.size()
        i = 0
        if ch[i].isalpha():                                    #如果字符是字母
            temp = ch[i]
            i += 1
            while ch[i].isalpha() or ch[i].isdigit():          #以该字母起始的字母或数字记录为标识符
                temp += ch[i]                                  #temp存放标识符
                if i==Len:
                    break                                      #结尾退出
            if self.is_reserved(temp):
                result['LEX']=self.reserved_words[temp]        #保留字的处理
                result['SEM']=temp
                result['LINE']=self.line
                return result
            result['LEX'] = 'ID'                               #标识符的处理
            result['SEM'] = temp
            result['LINE'] = self.line
            return result
        elif ch[i].isdigit():                                  #如果字符是数字
            temp = ch[i]
            i += 1
            while ch[i].isdigit():
                temp += ch[i]
                if i == Len:
                    break
            result['LEX'] = self.reserved_words['int']         # 数字的处理
            result['SEM'] = temp
            result['LINE'] = self.line
            return result


l=lex('a')
print(l.is_reserved('endwh'))