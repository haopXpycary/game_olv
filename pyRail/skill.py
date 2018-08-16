class skill:
    '''
    initSkill
        : consumedMagic(int)
        : skill_(void f(player))
    '''
    def initSkill(self,consumedMagic,_skill):
        self.consumedMagic = consumedMagic
        self._skill = _skill
        
    def lauch(self,other):
        self._skill(other)

class buff:
    def initBuff(self,_buff,time=0):
        self.buff = _buff
        self.time = time
        
    def setTime(self,time):
        self.time = time
    
    def buffing(self,other):
        self.buff(other)
        
if __name__ == "__main__":
    s = skill()
    class py: pass
    def askill(self):
        self.it = 2
        
    s.initSkill(10,askill)
    s.lauch(py())
    print(dir(s))