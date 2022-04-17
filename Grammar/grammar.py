from var import vt_path, formula_path, predict_path, token_path
from ffp import generateFFTSet
from ll1 import ll1
from visualization import visualization
import recursive_descent

# 生成ffp集
generateFFTSet(vt_path, formula_path, predict_path)

# ll1
ll1(token_path)

# 递归下降
# recursive_descent.Start(ffp.S)

visualization()