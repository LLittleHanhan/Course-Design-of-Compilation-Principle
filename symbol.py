class Symbol(object):
    def __init__(self,name=None,kind=None,type=None,value=None,access=None,level=None,offset=None,param=None,Class=None,code=None,Size=None,forward=None):
        self.name = name
        self.decKind = kind  #标识符类型
        self.typePtr = type  #数据类型
        self.value = value
        self.access = access
        self.level = level
        self.offset = offset
        self.param = param
        self.Class = Class
        self.code = code
        self.Size = Size
        self.forward = forward

    def __repr__(self):
        return "%s %s %s "%(self.name,self.decKind,self.typePtr)
    def info(self):
        return "%s %s %s "%(self.name,self.decKind,self.typePtr)
class SymbolTable(object):
    def __init__(self,level):
        self.table = []
        self.level =level

    def add(self,symbol):
        self.table.append(symbol)

    def __contains__(self, item):
        for sym in self.table:
            if item == sym.name:
                return True
        return False

    def pop(self,pos):
        self.table.pop(pos)

    def remove(self,name):
        length = len(self.table)
        for i in range(length):
            if self.table[i].name == name:
                self.table.pop(i)
                break

    def top(self):
        return self.table[-1]

    def get(self,name):
        length = len(self.table)
        for i in range(length):
            if self.table[i].name == name:
                return self.table[i]
        return None

    def __repr__(self):
        return "\n".join([str(i) for i in self.table])

    def __len__(self):
        return len(self.table)

    def __getitem__(self, item):
        return self.table[item]


class BaseType(object):
    def __init__(self,sz=1,kind=None):
        self.sz = sz
        self.type = kind

    def __repr__(self):
        return self.type

class ArrayType(object):
    def __init__(self,sz=None,low=None,top=None,element=None):
        self.sz = sz
        self.type = "arrayType"
        self.low = low
        self.top = top
        self.element = element
    def __repr__(self):
        return "array[%d .. %d] of %s"%(self.low,self.top,self.element)

class RecordType(object):
    def __init__(self,sz=None,fieldList=None):
        self.type = "recordType"
        self.sz = sz
        self.fieldList = fieldList

    def __repr__(self):
        return "record %s"%(self.fieldList)




import json
import sys

class nc():
    def __init__(self):
        self.nc= (x for x in range(100000))
    def reset(self):
        del self.nc
        self.nc=(x for x in range(100000))
nc = nc()
class AstNode(object):
    def __init__(self,tokenType,tokenVal="",father=None):
        self.tokenType = tokenType
        self.tokenVal = tokenVal
        self.father = father
        self.child = []
        self.brother = []
        self.id = next(nc.nc)
    def reset(self):
        nc.reset()
    def isTokenType(self,tokenType):
        return self.tokenType == tokenType

    def getTokenType(self):
        return self.tokenType

    def getTokenVal(self):
        return self.tokenVal

    def isTokenVal(self,tokenVal):
        return self.tokenVal == tokenVal

    def getId(self):
        return self.id

    def getFather(self):
        return self.father

    def isEmpty(self):
        return len(self.child) == 0

    def firstChild(self):
        if self.isEmpty():
            raise ValueError("node has no child\n")
        else:
            return self.child[0]

    def __repr__(self):
        return "astNode %d %s\n"%(self.id,self.tokenType)

    def insertChild(self,node):
        """ add a ast node to current node"""
        if node and not isinstance(node,AstNode):
            raise ValueError("child node must be an astNode")
        self.child.append(node)
        node.brother = self.child
        node.father = self

    def step(self):
        cur = self
        while cur.id != 0 and cur.brother[::-1].index(cur) == 0:
            cur = cur.father
        if cur.id != 0:
            cur = cur.brother[cur.brother.index(cur)+1]
        return cur




    def __len__(self):
        return len(self.child)

    def dump(self,depth=0,file=sys.stdout):
        tab = '     '*(depth-1)+" |- " if depth>0 else ""
        print("%s%s  %s"%(tab,self.tokenType,self.tokenVal),file=file)
        for child in self.child:
            child.dump(depth+1,file=file)




class AstNodeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,AstNode):
            return {
                "TokenType":obj.tokenType,
                "child":[{"TokenType": child.tokenType,"child": child.child} for child in obj.child]
            }
        return json.JSONEncoder.default(self,obj)

class AstNodeDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self,obj):
        if isinstance(obj, dict) and "TokenType" in obj:
            node = AstNode(obj["TokenType"])
            for childNode in obj.get("child"):
                node.insertChild(AstNodeDecoder.object_hook(self,childNode))
            return node

        return obj



