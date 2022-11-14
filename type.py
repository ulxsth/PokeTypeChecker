class Type(object):
    def __init__(self,
                 name,
                 atkSuperEffectiveTypes,
                 atkNotVeryEffectiveTypes,
                 atkNoEffectiveTypes,
                 defSuperEffectiveTypes,
                 defNotVeryEffectiveTypes,
                 defNoEffectiveTypes):
        self.name = name
        self.__atkSuperEffectiveTypes = atkSuperEffectiveTypes
        self.__atkNotVeryEffectiveTypes = atkNotVeryEffectiveTypes
        self.__atkNoEffectiveTypes = atkNoEffectiveTypes
        self.__defSuperEffectiveTypes = defSuperEffectiveTypes
        self.__defNotVeryEffectiveTypes = defNotVeryEffectiveTypes
        self.__defNoEffectiveTypes = defNoEffectiveTypes

    def isAtkSuperEffectiveTypes(type):
        return Type.__atkSuperEffectiveTypes.contains(type)
        
    def isAtkNotVeryEffectiveTypes(type):
        return Type.__atkNotVeryEffectiveTypes.contains(type)
        
    def isAtkNoEffectiveTypes(type):
        return Type.__atkNoEffectiveTypes.contains(type)
        
    def isDefSuperEffectiveTypes(type):
        return Type.__defSuperEffectiveTypes.contains(type)
        
    def isDefNotVeryEffectiveTypes(type):
        return Type.__defNotVeryEffectiveTypes.contains(type)
        
    def isDefNoEffectiveTypes(type):
        return Type.__defNoEffectiveTypes.contains(type)
        
        
    