formula_path = './formula.txt'
token_path = './token.txt'
dic = {}
tokens = []
ll1_stack = []

ffirstSet = {}
cfirstSet = {}
followSet = {}
predictSet = {}
vt = {'+', '*', 'i', '(',')'}
S = 'E'



#生成cfirst集和ffirst集
def genFirstSet(key):
    # 对每一个产生式
    for formula in dic[key].split(' | '):
        ffirstSet[key + ' = ' + formula] = set()
        for v in formula.split(' '):
            flag = 0
            if v in vt:
                ffirstSet[key + ' = ' + formula].add(v)
                break
            elif v == '$':
                ffirstSet[key + ' = ' + formula].add("$")
                break
            else:
                #判断v的fist是否已经生成
                if cfirstSet[v]:
                    ffirstSet[key + ' = ' + formula] |= cfirstSet[v]
                else:
                    ffirstSet[key + ' = ' + formula] |= genFirstSet(v)
                if "$" not in ffirstSet[key + ' = ' + formula]:
                    break
                else:
                    ffirstSet[key + ' = ' + formula].remove('$')
                    flag = 1
        if flag == 1:
             ffirstSet[key + ' = ' + formula].add("$")
        cfirstSet[key] |= ffirstSet[key + ' = ' + formula]
    return cfirstSet[key]

#根据已生成的first集，寻找特定串的first集，用于follow集生成
def findFirstSet(vl):
    s = set()
    flag = 1
    for v in vl:
        flag = 0
        if v in vt:
            s.add(v)
            break
        else:
            s |= cfirstSet[v]
            if '$' not in s:
                break
            else:
                s.remove('$')
                flag = 1
    if flag == 1:
        s.add('$')
    return s

#生成follow集
def genFollowSet():
    maychange = []
    for key in dic.keys():
        for formula in dic[key].split(' | '):
            if formula == '$':
                continue
            else:
                vl = formula.split(' ')
                for v in range(len(vl)):
                    if vl[v] not in vt:
                        #这里取交集而不用‘=’
                        followSet[vl[v]] |= findFirstSet(vl[v+1:])
                        if '$' in followSet[vl[v]]:
                            followSet[vl[v]].remove('$')
                            followSet[vl[v]] |= followSet[key]
                            # 将vl[v],key记录下来，这是每次迭代可能发生变化的地方
                            if vl[v] != key:
                                maychange.append([vl[v],key])
    print(maychange)
    flag = 1
    while flag == 1:
        flag = 0
        for t in maychange:
            temp = followSet[t[0]]
            followSet[t[0]] |= followSet[t[1]]
            if temp != followSet[t[0]]:
                flag = 1
    return

#生成predict集
def genPredictSet():
    for key in dic.keys():
        for formula in dic[key].split(' | '):

            predictSet[key + ' = ' + formula] = ffirstSet[key + ' = ' + formula]
            if '$' in predictSet[key + ' = ' + formula]:
                predictSet[key + ' = ' + formula].remove('$')
                predictSet[key + ' = ' + formula] |= followSet[key]
    return



#主程序
#读取产生式
f = open(formula_path, 'r')
for line in f.readlines():
    temp = line.strip('\n').split(' = ')
    dic[temp[0]] = temp[1]
    # cfirst集初始化
    cfirstSet[temp[0]] = set()
    #follow集初始化
    followSet[temp[0]] = set()
f.close()
print(dic)

#生成first集
for key in dic.keys():
    genFirstSet(key)
print("first集")
print(ffirstSet)
print(cfirstSet)

#生成follow集
followSet[S].add('#')
genFollowSet()
print("folow集")
print(followSet)

#生成predict集
genPredictSet()
print("predect集")
print(predictSet)

#LL(1)
#读取token序列
ll1_stack.append(S)
f = open(token_path,'r')
tokens = f.read().strip().split(' ')
for token in tokens:
    while ll1_stack[-1] != token:
        #flag记录是否匹配成功
        flag = 0
        #VN的每一个产生式
        for formula in dic[ll1_stack[-1]].split(' | '):
            if token in predictSet[ll1_stack[-1] + ' = ' + formula]:
                flag = 1
                ll1_stack.pop()
                for v in formula.split(' ').reverse():
                    ll1_stack.append(v)
                break
    if flag == 0:
        #错误处理
    #弹出匹配上的token，匹配下一个token
    ll1_stack.pop()
#匹配成功
print('success!')



