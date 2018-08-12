from control import *

class baseThing:
    def __init__(self,ID,pic):
        self.ID = ID
        self.pic = pic
        
class placeableThing(baseThing):
    def __init__(self,ID,pic,couldPass,howGet,timeSpent,willGet,number):
        super().__init__(self,ID,pic)
        self.howGet    = howGet
		self.couldPass = couldPass
        self.timeSpent = timeSpent
        self.needTime  = needTime
        self.willGet   = willGet
        self.number    = number
		
class utensilThing(baseThing):
    def  __init__(self,ID,pic,utensilType,durable,providedAttack,providedHealth,providedMagic,providedProtect,providedRestoreHealth,providedRestoreMagic):
        super().__init__(self,ID,pic)
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
        super().__init__(self,ID,pic,utensilType,durable,providedAttack,providedHealth,providedMagic,providedProtect,providedRestoreHealth,providedRestoreMagic)
		self.protectType = self.utensilType
		
class handheldThing(utensilThing):
    def __init__(self):
		

class gropThing(baseThing):
