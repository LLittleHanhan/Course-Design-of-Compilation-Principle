from symbol import *
import grammar
import var
from treelib import node
grammar.check_grammar()
#print(var.gramTree.children(0)[0].data.tokenInfo)


def analyze():
    initialize()
    travelsal(var.gramTree.get_node(0))

def initialize():
    intType = standardType("intType")
    charType = standardType("charType")
    boolType = standardType("boolType")

def travelsal(root):
    if(root.data.tokenInfo !=None):
        print(root.data.tokenInfo["lex"])
    temp = var.gramTree.children(root._identifier)
    for i in temp:
        travelsal(i)

#bbbbbb
analyze()