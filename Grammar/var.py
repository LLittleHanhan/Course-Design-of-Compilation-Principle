# some global variable

formula_path = 'rsc/formula.txt'
vt_path = 'rsc/vt.txt'
predict_path = 'rsc/predict.txt'
token_path = 'rsc/token.txt'

dic = {}  # 产生式
tokens = []  # token序列
vt = set()  # 非终极符
S = 'Program'  # 起始符

ffirstSet = {}  # 产生式右端的first集
cfirstSet = {}  # 产生式左端vt的first集
followSet = {}  # follow集
predictSet = {}  # predict集

