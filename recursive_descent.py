# 递归下降
from var import dic, predictSet, tokens, vt, grammarError,S

index = 0


def begin(name, depth=1):
    global index
    if name == S:
        index = 0
    tree_dict = {"name": name, "children": []}
    match_formula = ''
    for formula in dic[name].split(' | '):
        if tokens[index]["lex"] in predictSet[name + ' = ' + formula]:
            match_formula = formula
            break
    if match_formula == '':
        cor_vt = set()
        for formula in dic[name].split(' | '):
            cor_vt |= predictSet[name + ' = ' + formula]
        err = '出现语法错误!错误位置：' + '\n' + 'line:' + tokens[index]["line"] + '\n' + 'lex:' + tokens[index]["lex"] + '\n' + 'sem:' + tokens[index]["sem"] + '\n' + '实际应匹配字符：' + str(cor_vt)
        raise grammarError(err)

    for v in match_formula.split(' '):
        if v == '$':
            tree_dict["children"].append({"name":v})
            break
        elif v in vt:
            if v == tokens[index]["lex"]:
                tree_dict["children"].append({"name":v})
                index += 1
                root_tag = depth == 1 and v == match_formula.split(' ')[-1]

                if root_tag and index < len(tokens):
                    err = '出现语法错误!' + '\n' + '语句多余，多余位置:' + '\n' + 'line:' + tokens[index]["line"] + '\n' + 'lex:' + tokens[index]["lex"] + '\n' + 'sem:' + tokens[index]["sem"]
                    raise grammarError(err)
                if not root_tag and index == len(tokens):
                    err = '出现语法错误!' + '\n' + '程序不完整'
                    raise grammarError(err)
            else:
                err = '出现语法错误!错误位置：' + '\n' + 'line:' + tokens[index]["line"] + '\n' + 'lex:' + tokens[index]["lex"] + '\n' + 'sem:' + tokens[index]["sem"]+ '实际应匹配字符：' + v
                raise grammarError(err)
        else:
            tree_dict["children"].append(begin(v, depth + 1))
    return tree_dict