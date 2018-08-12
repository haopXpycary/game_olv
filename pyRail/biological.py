class biological:
	buffs = []
    def initAttributes(self,health,protect,magic,attack,restoreHealth,restoreMagic):
        self.health = health
        self.protect = protect
        self.magic = magic
        self.attack = attack
        self.restoreHealth = restoreHealth
        self.restoreMagic = restoreMagic
        
    def initPlace(self,x,y,pic):
        self.x = x
        self.y = y
        self.pic = pic
        
    def initDeathDrop(self,thing,number):
        # thing , number -> (,)
        self.dealthDropThing = thing
        self.dealthDropNumber = number
    
    def attack(self):
        return (self.attack,0,0)
	
    def update(self):
        self.addHealth(self,restoreHealth)
        self.addMagic(self,restoreMagic)
		for i in self.buffs: i(self)
		
class superiorBiological(biological):
    def initHandheld(self,thing):
        self.handheld = (thing,)
        
    def haveAttack(self):
        if self.handheld:
            return (self.attack,self.handheld[0].enchanting,self.handheld[0].buffTime)
        return (self.attack,0,0)
        
    def initSkills(self,skills):
        # :skills = (skill_1:skill,skill_2:skill,...,skill_5:skill)
        self.skills = skills
        
    def launchSkills(self,choice):
        if self.magic >= self.skills[choice].consumedMagic:
            self.magic -= self.skills[choice].consumedMagic
            self.skill[choice].launch(self)
            
if __name__ == "__main__":
    sb = superiorBiological()
    for i in dir(sb):
        if not i.startswith("_"):
            print(i)
    
    sb.initAttributes(1,1,1,1,1,1)
    sb.initDeathDrop(1,1)
    sb.initHandheld(1)
    sb.initPlace(1,1,'>')
    sb.initSkills([1,1,1,1,1])
    for i,j in zip(vars(sb).keys(),vars(sb).values()):
        print(i,':',j)