from pyecharts import options as opts
from pyecharts.charts import Tree
from var import gramTree,grammarTree_path

def my_to_dict(self, nid=None):
    nid = self.root if (nid is None) else nid
    ntag = self[nid].tag
    tree_dict = {"name": ntag, "children": []}
    if self[nid].expanded:
        queue = [self[i] for i in self[nid].successors(self._identifier)]
        for elem in queue:
            tree_dict["children"].append(
                my_to_dict(self, elem.identifier))
        if len(tree_dict["children"]) == 0:
            tree_dict = {"name": ntag}
        return tree_dict

def visualization():
    gramTreeDic = my_to_dict(gramTree)
    c = (
        Tree()
            .add(
            "",
            [gramTreeDic],
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
            .render(grammarTree_path)
    )
    return
