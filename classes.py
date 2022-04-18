class AtrributeIR:
    def __init__(self):
        self.idtype = None
        self.kind = None
        self.moreinfo = None

class varIR:
    def __init__(self):
        self.access = None
        self.level = None
        self.off = None

class procIR:
    def __init__(self):
        self.level = None
        self.pram = []
        self.code = None    #目标代码地址
        self.size = None

class standardType:
    def __init__(self,t):
        self.size = 1
        self.kind = t

class arrType:
    def __init__(self):
        self.size = None
        self.kind = "arrayTy"
        self.indexTy= None
        self.elemTy = None

class recType:
    def __init__(self):
        self.size = None
        self.kind = "recordTy"
        self.elem = []

class structType:
    def __init__(self):
        self.size = None
        self.kind = None
        self.elemType = None
        self.elem = None

class fieldChain:
    def __init__(self):
        self.idname = None
        self.unitType = None
        self.offset = None
        self.next = None

class typeIR:
    def __init__(self):
        self.size = None
        self.kind = None  #base or structure
        self.elem = None

