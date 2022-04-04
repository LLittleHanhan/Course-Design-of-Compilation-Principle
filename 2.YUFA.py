test

path = './test.txt'
dic = {}
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

    for key in dic.keys():
        for formula in dic[key].split(' | '):
            if formula == '$':
                continue
            else:
                vl = formula.split(' ')
                for v in range(len(vl)):
                    if vl[v] not in vt:
                        #这里取交集而不用‘=’，S={’#‘}影响
                        followSet[vl[v]] |= findFirstSet(vl[v+1:])
                        if '$' in followSet[vl[v]]:
                            followSet[vl[v]].remove('$')
                            followSet[vl[v]] |= followSet[key]
                            # 将vl[v]记录下来，这是每次迭代可能发生变化的地方

    return



#生成predict集
def genPredictSet():
    return



#主程序
#读取产生式
f = open(path, 'r')
for line in f.readlines():
    temp = line.strip('\n').split(' = ')
    dic[temp[0]] = temp[1]
    # cfirst集初始化
    cfirstSet[temp[0]] = set()
    #follow集初始化
    followSet[temp[0]] = set()
print(dic)

#生成first集
for key in dic.keys():
    genFirstSet(key)
print(ffirstSet)
print(cfirstSet)

#生成follow集
followSet[S].add('#')
genFollowSet()
print(followSet)

# #生成predict集
# genPredictSet()


