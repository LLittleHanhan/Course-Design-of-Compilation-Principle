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
    def __init__(self):
        self.size = 1
        self.kind = None

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
        self.body

class fieldChain:
    def __init__(self):
        self.idname
        self.unitType
        self.offset
        self.next

class typeIR:
    def __init__(self):
        self.size
        self.