from pyecharts import options as opts
from pyecharts.charts import Tree
from var import grammarTree_path


def visualization(width, height,gramTreeDic):
    c = (
        Tree(init_opts=opts.InitOpts(width=width,
                                     height=height,
                                     theme="vintage",
                                     page_title="grammarTree"))
            .add(
            "",
            [gramTreeDic],
            collapse_interval=0,
            orient="TB",
            initial_tree_depth=-1,
            is_roam=True,

            label_opts=opts.LabelOpts(
                rotate=0,
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="GrammarTree"))
            .render(grammarTree_path)
    )
    return
