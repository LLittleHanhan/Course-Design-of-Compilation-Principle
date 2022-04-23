from var import token_path, grammar_result_path, grammarTree_path, gramTree, tokens, predictSet,S
from ffp import generateFFTSet
from ll1 import ll1, grammarError
from visualization import visualization
from recursive_descent import begin
import os


def init():
    if os.path.exists(grammar_result_path):
        os.remove(grammar_result_path)

    if os.path.exists(grammarTree_path):
        os.remove(grammarTree_path)

    if gramTree.get_node(0) is not None:
        gramTree.remove_node(0)

    if not predictSet:
        generateFFTSet()

    tokens.clear()
    ft = open(token_path, 'r')
    for line in ft.readlines():
        info = line.strip('\n').strip(' ').split(' ')
        token = {"line": info[0], "lex": info[1], "sem": info[2]}
        tokens.append(token)
    ft.close()


def check_grammar(mode=0, width="1000px", height="1000px"):
    '''
    mode = 0 为ll1
    mode = 1 为递归下降
    width,height设置画布长宽
    return 1 成功
    return 0 失败
    grammar_result_path = 'rsc/grammar_result.txt'
    grammarTree_path = 'rsc/GrammarTree.html'
    '''

    init()
    flag = 1
    result = ''
    gramTreeDic = {}
    try:
        if mode == 0:
            gramTreeDic = ll1()
        if mode == 1:
            gramTreeDic = begin(S)
    except grammarError as e:
        flag = 0
        result = str(e)
    else:
        result = '语法无误，已输出语法树'
        visualization(width, height, gramTreeDic)
    finally:
        with open(grammar_result_path, 'w', encoding='utf-8') as fg:
            fg.write(result)
    print(result)
    return flag


if __name__ == '__main__':
    check_grammar(mode=1)



