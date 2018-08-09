from constName import *
from control import *
from func import dict

class basePlayer:
    def initPlace(self,x,y,headfor,pic):
        self.x = x
        self.y = y
        self.headfor = headfor
        self.pic = pic
        
    def initBaseAttributes(self,baseHealth,baseProtect,baseAttack,baseMagic):
        self.baseHealth  = baseHealth
        self.baseProtect = baseProtect
        self.baseAttack  = baseAttack
        self.baseMagic   = baseMagic
        
    def initLevel(self,level=1,experience=0):
        self.level = level
        self.exp = experience
        
    def initDevelopableAttributes(self,developableHealth,developableProtect,developableAttack,developableMagic):
        self.developableHealth  = developableHealth
        self.developableProtect = developableProtect
        self.developableAttack  = developableAttack
        self.developableMagic   = developableMagic
        
class behavingPlayer_moveMixIn(basePlayer):
    def walk(self,headfor):
        self.headfor = headfor
        if headfor == Right:
            self.x += 1
        elif headfor == Left and self.x >= 1:
            self.x -= 1
        elif headfor == Down:
            self.y += 1
        elif headfor == Up and self.y >= 1:
            self.y -= 1
    def move(self,x,y):
        self.x,self.y = x,y
    
class behavingPlayer_levelMixIn(basePlayer):
    def addExp(self,experience):
        self.experience += experience
        while self.experience >= levelUpNeedExp(self.level):
            self.level += 1
            self.baseHealth  += self.developableHealth
            self.baseProtect += self.developableProtect
            self.baseAttack  += self.developableAttack
            self.baseMagic   += self.developableMagic

class behavingPlayer_attackMixIn(basePlayer):
    def attack(self):
        if self.handheld:
            self.handheld.durable -= 1
            return (self.attack,self.handheld[0].enchanting,self.handheld[0].buffTime)
        return (self.attack,0,0)
        
    def initSkills(self,*skills):
        # :skills = (skill_1:skill,skill_2:skill,...,skill_5:skill)
        self.skills = skills
        
    def launchSkills(self,choice):
        if self.magic >= self.skills[choice].consumedMagic:
            self.magic -= self.skills[choice].consumedMagic
            self.skill[choice].launch(self)
    
class behavingPlayer_articleMixIn(basePlayer):
    def initBackpack(self):
        self.backpack = dict()
        
    def addThing(self,thing,number=1):
        if thing.ID in self.backpack.keys():
            self.backpack[self.backpack.key.index(thing)] += number
        else:
            self.backpack[thing] = number
    
    def removeThing(self,thing,number=1):
        if self.haveThing(thing,number):
            self.backpack[self.backpack.key.index(thing)] -= number
            
    def haveThing(self,thing,number=1):
        if thing in self.backpack.keys():
            if self.backpack[self.backpack.key.index(thing)] >= number:
                return True
        return False
        
class behavingPlayer_armorMixIn(basePlayer):
    def initArmor(self):
        # self.equipmentBar = [headbar,necklacebar,breastplateBar,pantsBar,shoeBar]
        self.equipmentBar = [0,0,0,0,0]
        self.handheld = [0]
        self.equipmentProvidedAttack  = 0
        self.equipmentProvidedHealth  = 0
        self.equipmentProvidedMagic   = 0
        self.equipmentProvidedProtect = 0
        self.equipmentProvidedRestoreHealth = 0
        self.equipmentProvidedRestoreMagic  = 0
        
    def wearThing(self,armor):
        # armor.protectionType
        if self.equipmentBar[armor.protectionType]:
            self.addThing(self.equipmentBar[armor.protectionType])
        self.removeThing(armor)
        self.equipmentBar[armor.protectionType] = armor
        
    def handheldThing(self,weaponry):
        if self.handheld[0]:
            self.addThing(self.handheld[0])
        self.removeThing(weaponry)
        self.equipmentBar[0] = weaponry
        
    def statisticsEquipmentProvided(self):
        # utensilThing.providedAttack
        # utensilThing.providedHealth
        # utensilThing.providedMagic
        # utensilThing.providedProtect
        # utensilThing.porvidedRestoreHealth
        # utensilThing.providedRestoreMagic
        for i in self.equipmentBar + self.handheld:
            if not i: continue;
            self.equipmentProvidedAttack  = i.providedAttack
            self.equipmentProvidedHealth  = i.providedHealth
            self.equipmentProvidedMagic   = i.providedMagic
            self.equipmentProvidedProtect = i.providedProtect
            self.equipmentProvidedRestoreHealth = i.porvidedRestoreHealth
            self.equipmentProvidedRestoreMagic  = i.providedRestoreMagic
        
class behavingPlayer_activityMixIn(basePlayer):
    def initActivity(self):
        self.satisfaction = 100
        
    def addSatisfaction(self,number):
        self.satisfaction += number
    def lowerSatisfaction(self,number):
        self.satisfaction -= number
        
    def addHealth(self,number):
        if self.health + number <= self.maxHealth:
            self.health += number
        else:
            self.health = self.maxHealth
    def lowerHealth(self,number):
        self.health -= number
        
    def addMagic(self,number):
        if self.health + number <= self.maxMagic:
            self.magic += number
        else:
            self.magic = self.maxMagic
    def lowerMagic(self,number):
        self.magic -= number
    
class behavingPlayer_additionalMixIn(basePlayer):
    def initAdditionalAttributes(self):
        self.additionalHealth  = 0
        self.additionalMagic   = 0
        self.additionalProtect = 0
        self.additionalAttack  = 0
        self.additionalRestoreHealth = 0
        self.additionalRestoreMagic  = 0
        
    def increaseHealth(self,number):  self.additionalHealth += number
    def decreaseHealth(self,number):  self.additionalHealth -= number
    def increaseMagic(self,number):   self.additionalMagic  += number
    def decreaseMagic(self,number):   self.additionalMagic  -= number
    def increaseAttack(self,number):  self.additionalAttack += number
    def decreaseAttack(self,number):  self.additionalAttack -= number
    def increaseProtect(self,number): self.additionalProtect += number
    def decreaseProtect(self,number): self.additionalProtect -= number
    def increaseRestoreHealth(self,number): self.additionalRestoreHealth += number
    def decreaseRestoreHealth(self,number): self.additionalRestoreHealth -= number
    def increaseRestoreMagic(self,number):  self.additionalRestoreMagic += number
    def decreaseRestoreMagic(self,number):  self.additionalRestoreMagic -= number

class behavingPlayer_moneyMixIn(basePlayer):
    def initMoney(self):
        self.money = 0
    
    def addMoney(self,number): self.money += number
    def lowerMoney(self,number): self.money -= number
    
class player(     
    behavingPlayer_armorMixIn,
    behavingPlayer_articleMixIn,
    behavingPlayer_attackMixIn,
    behavingPlayer_levelMixIn,
    behavingPlayer_moveMixIn,
    behavingPlayer_activityMixIn,
    behavingPlayer_additionalMixIn,
    behavingPlayer_moneyMixIn):
    def statisticsAttributes(self):
        self.maxHealth = self.baseHealth  + self.equipmentProvidedHealth + self.additionalHealth
        self.health    = self.maxHealth
        self.maxMagic  = self.baseMagic   + self.equipmentProvidedMagic + self.additionalMagic
        self.magic     = self.maxMagic
        self.protect   = self.baseProtect + self.equipmentProvidedProtect + self.additionalProtect
        self.attack    = self.baseAttack  + self.equipmentProvidedAttack + self.additionalAttack
        self.restoreHealth = self.equipmentProvidedRestoreHealth + self.additionalRestoreHealth
        self.restoreMagic  = self.equipmentProvidedRestoreMagic  + self.additionalRestoreMagic
    def update(self):
        self.lowerSatisfaction(HUNGRY_DAILY_LOWER)
        self.addHealth(self,restoreHealth)
        self.addMagic(self,restoreMagic)
        
if __name__ == "__main__":
    sb = player()
    for i in dir(sb):
        if not i.startswith("__"): 
            print(i)
            print(help(eval("sb."+i)))
    
    sb.initPlace(0,0,Right,">")
    sb.initBaseAttributes(20,5,10,10)
    sb.initDevelopableAttributes(5,3,3,3)
    sb.initAdditionalAttributes()
    sb.initLevel()
    sb.initSkills([0,0,0,0,0])
    sb.initBackpack()
    sb.initArmor()
    sb.initActivity()
    sb.initMoney()
    
    for i,j in vars(sb).items():
        print("%32s" %i,":",j)
    input("Input [Enter] To Exit.")