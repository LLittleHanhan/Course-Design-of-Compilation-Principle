from var import tokens, S, dic, predictSet, gramTree, grammarError, vt


def my_to_dict(self, nid=None):
    nid = self.root if (nid is None) else nid
    ntag = self[nid].tag
    tree_dict = {"name": ntag, "children": []}
    if self[nid].expanded:
        queue = [self[i] for i in self[nid].successors(self._identifier)]
        for elem in queue:
            tree_dict["children"].append(
                my_to_dict(self, elem.identifier))
        if len(tree_dict["children"]) == 0:
            tree_dict = {"name": ntag}
        return tree_dict


# 记录token信息
class infoNode:
    def __init__(self, nextBrotherId=-1, tokenInfo=None):
        self.nextBrotherId = nextBrotherId
        self.tokenInfo = tokenInfo


def ll1():
    id = 0  # 用于标志每一个树节点
    info = infoNode()
    gramTree.create_node(tag=S, identifier=id, data=info)
    cur_node = gramTree.get_node(id)
    id += 1

    i = 0
    tokensLen = len(tokens)
    while i < tokensLen:
        token = tokens[i]
        empty_tag = False
        while cur_node.tag != token["lex"] and cur_node.tag != '$':
            if cur_node.tag in vt:
                err = '1出现语法错误!错误位置：' + '\n' + 'line:' + token["line"] + '\n' + 'lex:' + token["lex"] + '\n' + 'sem:' + token["sem"] + '\n' + '实际应匹配字符：' + cur_node.tag
                raise grammarError(err)
            branch_tag = False
            empty_tag = False
            for formula in dic[cur_node.tag].split(' | '):
                if token["lex"] in predictSet[cur_node.tag + ' = ' + formula]:
                    branch_tag = True
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
                        empty_tag = True
                    break
            if not branch_tag:
                cor_vt = set()
                for formula in dic[cur_node.tag].split(' | '):
                    cor_vt |= predictSet[cur_node.tag + ' = ' + formula]
                err = '出现语法错误!错误位置：' + '\n' + 'line:' + token["line"] + '\n' + 'lex:' + token["lex"] + '\n' + 'sem:' + token["sem"] + '\n' + '实际应匹配字符：' + str(cor_vt)
                raise grammarError(err)
        # 匹配成功
        if not empty_tag:
            i += 1
            cur_node.data.tokenInfo = token
        # token序列前进

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
            err = '出现语法错误!' + '\n' + '语句多余，多余位置:' + '\n' + 'line:' + tokens[i]["line"] + '\n' + 'lex:' + tokens[i][
                "lex"] + '\n' + 'sem:' + tokens[i]["sem"]

            raise grammarError(err)
        if not root_tag and i == tokensLen:
            err = '出现语法错误!' + '\n' + '程序不完整。'
            raise grammarError(err)
    return my_to_dict(gramTree)
