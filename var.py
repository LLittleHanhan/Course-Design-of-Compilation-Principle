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

ffirstSet = {}  # 产生式右端的first集
cfirstSet = {}  # 产生式左端vt的first集
followSet = {}  # follow集
predictSet = {}  # predict集

gramTree = Tree()

# 记录token信息
class infoNode:
    def __init__(self, nextBrotherId=-1, tokenInfo=None):
        self.nextBrotherId = nextBrotherId
        self.tokenInfo = tokenInfo


