# ID
TYPES_ID = {
    "ノーマル": 0,
    "ほのお": 1,
    "みず": 2,
    "でんき": 3,
    "くさ": 4,
    "こおり": 5,
    "かくとう": 6,
    "どく": 7,
    "じめん": 8,
    "ひこう": 9,
    "エスパー": 10,
    "むし": 11,
    "いわ": 12,
    "ゴースト": 13,
    "ドラゴン": 14,
    "あく": 15,
    "はがね": 16,
    "フェアリー": 17,
    # "すべて等倍": 404
}

class Type(object):
    def __init__(self,
                 id,
                 name,
                 atkDoubleTypes,
                 atkHalfTypes,
                 atkZeroTypes,
                 defDoubleTypes,
                 defHalfTypes,
                 defZeroTypes):
        self.id = id
        self.name = name
        self.atkDoubleTypes = atkDoubleTypes
        self.atkHalfTypes = atkHalfTypes
        self.atkZeroTypes = atkZeroTypes
        self.defDoubleTypes = defDoubleTypes
        self.defHalfTypes = defHalfTypes
        self.defZeroTypes = defZeroTypes
        
    def checkDefMag(self, atkTypeId: int):
        if(atkTypeId in self.defDoubleTypes):
            return 2
        elif(atkTypeId in self.defHalfTypes):
            return 0.5
        elif(atkTypeId in self.atkZeroTypes):
            return 0
        else:
            return 1