from classes import *
import grammar
import var


def analyze():
    initialize()

def initialize():
    intType = standardType("intType")
    charType = standardType("charType")
    boolType = standardType("boolType")

def travelsal(root):
    if(root.data !=None):
        print(1)
    temp = root.children(root.identifier)
    for i in temp:
        travelsal(i)
