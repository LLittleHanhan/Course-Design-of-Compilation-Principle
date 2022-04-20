from var import vt_path, formula_path, predict_path, token_path, grammar_result_path, grammarTree_path,gramTree
from ffp import generateFFTSet
from ll1 import ll1, grammarError
from visualization import visualization
import recursive_descent
import  os



def check_grammar(mode=0):
    '''
    mode = 0 为ll1
    mode = 1 为递归下降
    return 1 成功
    return 0 失败
    grammar_result_path = 'rsc/grammar_result.txt'
    grammarTree_path = 'rsc/GrammarTree.html'
    '''

    #删除两输出文件
    if os.path.exists(grammar_result_path):
        os.remove(grammar_result_path)
    if os.path.exists(grammarTree_path):
        os.remove(grammarTree_path)

    flag = 1
    result = ''
    generateFFTSet(vt_path, formula_path, predict_path)
    if mode == 0:
        try:
            ll1(token_path)
        except grammarError as e:
            flag = 0
            result = str(e)
        else:
            result = '语法无误，已输出语法树'
            visualization()
        finally:
            with open(grammar_result_path, 'w', encoding='utf-8') as fg:
                fg.write(result)
    return flag


if __name__ == '__main__':
    check_grammar()
