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
        
if __name__ == "__main__":
    s = skill()
    class py: pass
    def askill(self):
        self.it = 2
        
    s.initSkill(10,askill)
    s.lauch(py())
    print(dir(s))