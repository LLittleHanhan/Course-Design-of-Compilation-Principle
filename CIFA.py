#张小北
import re
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
                    "integer": 'INTEGER'}
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
             'INT': "INTC","'": "CHAR_VAL",
             ':=': "ASSIGN",'=': "EQ",
             '<': "LT",'+': "PLUS",
             '-': "MINUS",'*': "TIMES",
             '/': "DIVIDE",'(': "LPAREN",
             ')': "RPAREN",'.': "DOT",
             ':': "COLON",';': "SEMI",
             ',': "COMMA",'[': "LMIDPAREN",
             ']': "RMIDPAREN",'..': "UNDERRANGE",
             'EOF': "ENDFILE",'ERROR': "ERROR"}

    singlesep=['+','-','*','/','(',')',';','[',']','=','<',',']

    # 程序

    def error(self,line):
        print("error in line "+str(line))
        #exit(1)
        return {'LINE':line,'LEX':'ERROR','SEM':'NONE'}




    def is_reserved(self,ch):
        return ch in self.reserved_words.keys()

    def is_single_sep(self,ch):
        return ch in self.singlesep

    def scan(self,ch,line):
        result = []
        Len = len(ch)
        if Len==0:
            return
        i = 0
        while i<Len :
            if ch[i].isalpha():                                    #如果字符是字母
                temp = ''
                while ch[i].isalpha()==True or ch[i].isdigit()==True:          #以该字母起始的字母或数字记录为标识符
                    temp += ch[i]                                   #temp存放标识符
                    i+=1
                    if i==Len:
                        break                                      #结尾退出
                re = {}
                re['LINE'] = line
                if self.is_reserved(temp):
                    re['LEX']=self.reserved_words[temp]            # 保留字的处理
                else:
                    re['LEX'] = 'ID'                               #标识符的处理
                re['SEM'] = temp
                result.append(re)
                #print(re)
                #print(re)

            elif ch[i].isdigit():                                  #如果字符是数字
                temp = ''
                while ch[i].isdigit():
                    temp += ch[i]
                    i+=1
                    if i == Len:
                        break
                re = {}
                re['LINE'] = line
                re['LEX'] = 'INTC'         # 数字的处理
                re['SEM'] = temp
                result.append(re)

            elif self.is_single_sep(ch[i]): #单分界符
                re = {}
                re['LINE'] = line
                re['LEX'] = self.lex_tag[ch[i]]
                re['SEM'] = ch[i]
                result.append(re)
                i+=1

            elif ch[i]==' ':
                i+=1
                continue

            elif ch[i]==':':
                i+=1
                if i==Len:
                    return self.error(line)
                if ch[i]=='=':
                    re = {}
                    re['LINE'] = line
                    re['LEX'] = self.lex_tag[':=']
                    re['SEM'] = ':='
                    result.append(re)
                    i += 1
                else:
                    return self.error(line)

            elif ch[i]=='.':
                i += 1
                re = {}
                re['LINE'] = line
                if i == Len or ch[i]!='.':
                    re['LEX'] = self.lex_tag['.']
                    re['SEM'] = '.'
                elif ch[i] == '.':
                    re['LEX'] = self.lex_tag['..']
                    re['SEM'] = '..'
                else:
                    return self.error(line)
                result.append(re)
                i += 1

            elif ch[i]=="'":
                i += 1
                if i == Len:
                    return self.error(line)
                #temp=''
                if ch[i].isalpha() == True or ch[i].isdigit() == True:
                    temp=ch[i]
                    i+=1
                    if i == Len:
                        return self.error(line)
                else:
                    return self.error(line)
                if ch[i]=="'":
                    re = {}
                    re['LINE'] = line
                    re['LEX'] = self.lex_tag["'"]
                    re['SEM'] = temp
                    result.append(re)
                    i += 1
                else:
                    return self.error(line)

            else:
                print('qwe')
                return self.error(line)
        return result

    def run(self,path):
        with open(path, "r",encoding='utf-8') as f:
            data = f.readlines()
        #print(data)
        token=[]
        for i,val in enumerate(data):
            val=val[0:-1]
            val=re.sub(r"{.*}",'',val)
            val=re.sub('\t',' ',val)
            #print(val)
            t=self.scan(val,i)
            token.append(t)
            #print(t)
        token = list(filter(None, token))
        with open("rsc/token.txt", "w") as f:
                for v in token:
                    for res in v:
                        c=str(res['LINE'])+' '+res['LEX']+' '+res['SEM']+'\n'
                        f.writelines(c)
        return token
'''
l=lex()
a=l.run('example/c5.txt')
for i,val in enumerate(a):
    print(val)

'''




