class baseThing:
    def __init__(self,ID,pic):
        self.ID = ID
        self.pic = pic
        
class placeableThing(baseThing):
    def __init__(self,ID,pic,howGet,timeSpent,willGet,number):
        super().__init__(self,ID,pic)
        self.howGet    = howGet
        self.timeSpent = timeSpent
        self.needTime  = needTime
        self.willGet   = willGet
        self.number    = number

class utensilThing(baseThing):
    def  __init__(self,ID,pic):
        super().__init__(self,ID,pic)
        self.providedAttack
        self.providedHealth
        self.providedMagic
        self.providedProtect
        self.porvidedRestoreHealth
        self.providedRestoreMagic
    def levelUp(self):
    def enchanting(self):
        
class equippedThing(utensilThing):
    def __init__(self): pass 
    def mixIn(self):
    
class handheldThing(utensilThing):
    def __init__(self):
