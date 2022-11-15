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

DOUBLE_ATK2DEF = {
    0: [], # ノーマル
    1: [4, 5, 11, 16], # ほのお
    2: [1, 8, 12], # みず
    3: [2, 9], # でんき
    4: [2, 8, 12], # くさ
    5: [4, 8, 9, 14], # こおり
    6: [0, 5, 12, 15, 16], # かくとう
    7: [4, 17], # どく
    8: [1, 3, 7, 12, 16], # じめん
    9: [4, 6, 11], # ひこう
    10: [6, 7], # エスパー
    11: [4, 10, 15], # むし
    12: [1, 5, 9, 11], # いわ
    13: [10, 13], # ゴースト
    14: [14], # ドラゴン
    15: [10, 13], # あく
    16: [5, 12, 17], # はがね
    17: [6, 14, 15], # フェアリー
    404: []
}

HALF_ATK2DEF = {
    0: [12, 16], # ノーマル
    1: [1, 4, 5, 11, 16], # ほのお
    2: [1, 2, 8, 12], # みず
    3: [3, 2, 9], # でんき
    4: [2, 3, 4, 8], # くさ
    5: [5], # こおり
    6: [11, 12, 15], # かくとう
    7: [4, 6, 7, 11, 17], # どく
    8: [7, 12], # じめん
    9: [4, 6, 11], # ひこう
    10: [6, 10], # エスパー
    11: [4, 6, 8], # むし
    12: [0, 1, 7, 9], # いわ
    13: [7, 11], # ゴースト
    14: [1, 2, 3, 4], # ドラゴン
    15: [13, 15], # あく
    16: [0, 4, 5, 9, 10, 11, 12, 14, 16, 17], # はがね
    17: [6, 11, 15], # フェアリー
    404: []
}

ZERO_ATK2DEF = {
    0: [13], # ノーマル
    1: [], # ほのお
    2: [], # みず
    3: [8], # でんき
    4: [], # くさ
    5: [], # こおり
    6: [13], # かくとう
    7: [16], # どく
    8: [9], # じめん
    9: [], # ひこう
    10: [15], # エスパー
    11: [], # むし
    12: [], # いわ
    13: [0], # ゴースト
    14: [17], # ドラゴン
    15: [], # あく
    16: [], # はがね
    17: [], # フェアリー
    404: []
}


def isExistTypes(typeName, isAllowVoid):
    if(isAllowVoid):
        return (typeName in TYPES_ID) or (typeName == "")
    else:
        return typeName in TYPES_ID

def checkSingleTypeCon(atkTypeID: int, defTypeID: int):
    if(defTypeID in DOUBLE_ATK2DEF[atkTypeID]):
        return 2
    elif(defTypeID in HALF_ATK2DEF[atkTypeID]):
        return 0.5
    elif(defTypeID in ZERO_ATK2DEF[atkTypeID]):
        return 0
    else:
        return 1

def checkMultiTypeCon(atkTypeID: int, defTypeID1: int, defTypeID2: int):
    return checkSingleTypeCon(atkTypeID, defTypeID1) * checkSingleTypeCon(atkTypeID, defTypeID2)
    

def main():
    atkType = input("こうげきわざのタイプ：")
    if(not isExistTypes(atkType, False)):
        print("そのタイプは　そんざいしないみたいだ...")
        return
        
    defType1 = input("こうげきをうけるポケモンのタイプ１：")
    if(not isExistTypes(defType1, False)):
        print("そのタイプは　そんざいしないみたいだ...")
        return
    
    defType2 = input("こうげきをうけるポケモンのタイプ２（単タイプの場合はEnter）：")
    if(not isExistTypes(defType2, True)):
        print("そのタイプは　そんざいしないみたいだ...")
        return
    
    atkTypeID = TYPES_ID[atkType]
    defTypeID1 = TYPES_ID[defType1]
    defTypeID2 = TYPES_ID[defType2] if defType2 != "" else 404
    mag = checkMultiTypeCon(atkTypeID, defTypeID1, defTypeID2)
    
    if(mag == 0):
        print("こうかは　ないようだ...")
    elif(mag in (0.25, 0.5)):
        print("こうかは　いまひとつだ...")
    elif(mag == 1):
        print("こうかは　ふつうだ！")
    else:
        print("こうかは　ばつぐんだ！")

    print(f"（倍率：　{mag}倍）")


if __name__ == '__main__':
    main()
    