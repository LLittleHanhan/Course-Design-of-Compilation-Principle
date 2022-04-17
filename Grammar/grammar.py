from var import vt_path, formula_path, predict_path, token_path
import ffp
import ll1
import recursive_descent

# 生成ffp集
ffp.generateFFTSet(vt_path, formula_path, predict_path)

# ll1
data = ll1.ll1(token_path)

# 递归下降
# recursive_descent.Start(ffp.S)

# 可视化
from pyecharts import options as opts
from pyecharts.charts import Tree

c = (
    Tree()
        .add(
        "",
        [data],
        collapse_interval=2,
        orient="TB",
        label_opts=opts.LabelOpts(
            position="top",
            horizontal_align="right",
            vertical_align="middle",
            rotate=0,
        ),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="GrammarTree"))
        .render("GrammarTree.html")
)
