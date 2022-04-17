from var import tokens, S, dic, predictSet,gramTree

# 记录token信息
class infoNode:
    def __init__(self, nextBrotherId=-1):
        self.nextBrotherId = nextBrotherId

def ll1(token_path):
    # 读取token序列
    ft = open(token_path, 'r')
    for line in ft.readlines():
        for token in line.strip('\n').strip('').split(' '):
            tokens.append(token)

    id = 0  # 用于标志每一个树节点
    info = infoNode()
    gramTree.create_node(tag=S, identifier=id, data=info)
    cur_node = gramTree.get_node(id)
    id += 1
    for token in tokens:
        while cur_node.tag != token:
            match_tag = False
            for formula in dic[cur_node.tag].split(' | '):
                if token in predictSet[cur_node.tag + ' = ' + formula]:
                    match_tag = True
                    # 创建结点
                    vl = formula.split(' ')
                    cur_id = 0
                    for v in range(len(vl)):
                        if v == 0:  # 更新当前结点
                            cur_id = id
                        nextBrotherId = id + 1 if v != len(vl) - 1 else -1
                        info = infoNode(nextBrotherId=nextBrotherId)
                        gramTree.create_node(tag=vl[v], identifier=id, parent=cur_node.identifier, data=info)
                        id += 1
                    cur_node = gramTree.get_node(cur_id)
                    if cur_node.tag == '$':
                        while cur_node.data.nextBrotherId == -1:
                            cur_node = gramTree.parent(cur_node.identifier)
                        cur_node = gramTree.get_node(cur_node.data.nextBrotherId)
                    break
        if token == tokens[-1]:
            break
        while cur_node.data.nextBrotherId == -1:
            cur_node = gramTree.parent(cur_node.identifier)
        cur_node = gramTree.get_node(cur_node.data.nextBrotherId)
    gramTree.show()
    return


'''
#
root = Node(S)
cur_node = root
for token in tokens:
    while cur_node.name != token:
        match_tag = False
        for formula in dic[cur_node.name].split(' | '):
            if token in predictSet[cur_node.name + ' = ' + formula]:
                match_tag = True
                # 创建结点
                cur_son = None
                for v in formula.split(' '):
                    if cur_node.son is None:
                        cur_node.son = Node(v)
                        cur_son = cur_node.son
                    else:
                        cur_son.brother = Node(v)
                        cur_son = cur_son.brother
                    cur_son.father = cur_node
                cur_node = cur_node.son
                if cur_node.name == '$':
                    while cur_node.brother is None:
                        cur_node = cur_node.father
                    cur_node = cur_node.brother
                break
    #当前token匹配成功
    if token == tokens[-1]:
        break
    while cur_node.brother is None:
        cur_node = cur_node.father
    cur_node = cur_node.brother
'''

'''
#ll1分析栈
ll1_stack.append(S)
for token in tokens:
    while ll1_stack[-1] != token:
        #flag记录是否匹配成功
        flag = 0
        #VN的每一个产生式
        for formula in dic[ll1_stack[-1]].split(' | '):
            if token in predictSet[ll1_stack[-1] + ' = ' + formula]:
                flag = 1
                print(ll1_stack[-1] + ' ::= ' + formula)
                ll1_stack.pop()
                temp = formula.split(' ')
                temp.reverse()
                for v in temp:
                    if v != '$':
                        ll1_stack.append(v)
                break
    if flag == 0:
        print('failed')
    #弹出匹配上的token，匹配下一个token
    ll1_stack.pop()
#匹配成功
print(ll1_stack)
print('success!')
'''
