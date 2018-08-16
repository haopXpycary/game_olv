from control import *
from constName import *

class baseThing:
    def __init__(self,ID,pic):
        self.ID = ID
        self.pic = pic
        
class layoutThing(baseThing):
    events = []
    # howGet = {thing:time}
    # willGet = {thing:number}
    def __init__(self,ID,pic,color,couldPass,howGet,willGet):
        super().__init__(ID,pic)
        self.howGet    = howGet
        self.color     = color
        self.couldPass = couldPass
        self.willGet   = willGet
        
    def addEvent(self,event):
        if not (event in self.events):
            self.events.append(event)
    
    def layout(self,x,y):
        pass
        
class utensilThing(baseThing):
    def  __init__(self,ID,pic,utensilType,durable,providedAttack,providedHealth,providedMagic,providedProtect,providedRestoreHealth,providedRestoreMagic):
        super().__init__(ID,pic)
        self.durable = durable
        self.utensilType = utensilType
        self.providedAttack  = providedAttack
        self.providedHealth  = providedHealth
        self.providedMagic   = providedMagic
        self.providedProtect = providedProtect
        self.porvidedRestoreHealth = providedRestoreHealth
        self.providedRestoreMagic  = providedRestoreMagic
        self.const = CalculatedConst(self.providedAttack,self.providedHealth,self.providedMagic,self.providedProtect,self.providedRestoreHealth,self.providedRestoreMagic)
        self.buyConst = int(self.const * AttachmentRate)
        
    def initlevel(self,level):
        self.level = level
        self.color = level # constName.color[int] = level
        self.levelUpConst = self.level * UpgradeCostIncreaseMultiple
        
    def levelUp(self):
        if self.level >= 6: return 0;
        self.level += 1
        self.providedAttack  = providedAttack * LevelUpGrowthRate
        self.providedHealth  = providedHealth * LevelUpGrowthRate
        self.providedMagic   = providedMagic * LevelUpGrowthRate
        self.providedProtect = providedProtect * LevelUpGrowthRate
        self.porvidedRestoreHealth = providedRestoreHealth * LevelUpGrowthRate
        self.providedRestoreMagic  = providedRestoreMagic * LevelUpGrowthRate
        self.const = CalculatedConst(self.providedAttack,self.providedHealth,self.providedMagic,self.providedProtect,self.providedRestoreHealth,self.providedRestoreMagic)
        self.buyConst = int(self.const * AttachmentRate)
        self.levelUpConst = self.level * UpgradeCostIncreaseMultiple
        
    def enchanting(self,buff,time):
        self.buff = buff
        self.buff.setTime(time)
        
    def mixIn(self,other):
        self.durable = self.durable + other.durable
        
class equippedThing(utensilThing):
    def  __init__(self,ID,pic,utensilType,durable,providedAttack,providedHealth,providedMagic,providedProtect,providedRestoreHealth,providedRestoreMagic):
        super().__init__(ID,pic,utensilType,durable,providedAttack,providedHealth,providedMagic,providedProtect,providedRestoreHealth,providedRestoreMagic)
        self.protectType = self.utensilType
        
class handheldThing(utensilThing):
    def __init__(self,ID,pic,utensilType,durable,providedAttack,providedMagic):
        super().__init__(ID,pic,utensilType,durable,providedAttack,0,providedMagic,0,0,0)

class gropThing(layoutThing):
    def  __init__(self,ID,pic,willGet,growTime):
        super().__init__(ID,pic,Green,True,{0:0},willGet)
        self.growTime = growTime

if __name__ == "__main__":
    sb = gropThing(0,'V',{},2)
    print(dir(sb))
    print(vars(sb))