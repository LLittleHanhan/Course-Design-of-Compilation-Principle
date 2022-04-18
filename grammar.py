from var import vt_path, formula_path, predict_path, token_path,gramTree
from ffp import generateFFTSet
from ll1 import ll1, grammarError
from visualization import visualization
import recursive_descent


def check_grammar(mode=0):
    generateFFTSet(vt_path, formula_path, predict_path)
    if mode == 0:
        try:
            ll1(token_path)
        except grammarError as e:
            print(e)
        else:
            print('语法无误')
            visualization()
    return


if __name__ == '__main__':
    check_grammar()
