from var import tokens, S, dic, predictSet, gramTree,infoNode


# 异常处理
class grammarError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return self.ErrorInfo


def ll1(token_path):
    # 读取token序列
    ft = open(token_path, 'r')
    for line in ft.readlines():
        info = line.strip('\n').strip('').split(' ')
        token = {"line": info[0], "lex": info[1], "sem": info[2]}
        tokens.append(token)

    id = 0  # 用于标志每一个树节点
    info = infoNode()
    gramTree.create_node(tag=S, identifier=id, data=info)
    cur_node = gramTree.get_node(id)
    id += 1

    i = 0
    tokensLen = len(tokens)
    while i < tokensLen:
        token = tokens[i]
        while cur_node.tag != token["lex"] and cur_node.tag != '$':
            match_tag = False
            empty_tag = False
            for formula in dic[cur_node.tag].split(' | '):
                if token["lex"] in predictSet[cur_node.tag + ' = ' + formula]:
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
                        i -= 1
                        empty_tag = True
                    break
            if not match_tag:
                err = '出现语法错误!' + '\n' + 'line:' + token["line"] +'\n' + 'lex:' + token["lex"] + '\n' + 'sem:' + token["sem"]
                raise grammarError(err)
        # 匹配成功
        if not empty_tag:
            cur_node.data.tokenInfo = token
        # token序列前进
        i += 1
        # grammarTree回溯
        root_tag = False
        while cur_node.data.nextBrotherId == -1:
            cur_node = gramTree.parent(cur_node.identifier)
            if cur_node.is_root():
                root_tag = True
                break;
        # 正常情况
        if not root_tag and i < tokensLen:
            cur_node = gramTree.get_node(cur_node.data.nextBrotherId)
        # 异常处理
        if root_tag and i < tokensLen:
            err = '出现语法错误!' + '\n' + '语句多余，多余位置:' + '\n' + 'line:' + tokens[i]["line"] + '\n' + 'lex:' + tokens[i]["lex"] + '\n' + 'sem:' + tokens[i]["sem"]

            raise grammarError(err)
        if not root_tag and i == tokensLen:
            err = '出现语法错误!' + '\n' + '语句残缺'
            raise grammarError(err)
        # if root_tag and i == tokensLen:
    gramTree.show()
    return
