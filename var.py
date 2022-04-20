# some global variable
from treelib import Tree

formula_path = 'rsc/formula.txt'
vt_path = 'rsc/vt.txt'
predict_path = 'rsc/predict.txt'
token_path = 'rsc/token.txt'
grammar_result_path = 'rsc/grammar_result.txt'
grammarTree_path = 'rsc/GrammarTree.html'

dic = {}  # 产生式
tokens = []  # token序列
vt = set()  # 非终极符
S = 'Program'  # 起始符

predictSet = {}  # predict集

gramTree = Tree()

class grammarError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return self.ErrorInfo