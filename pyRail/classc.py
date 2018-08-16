class event:
    touch = False
    def __init__(self,fun):
        self.triggerFunc = fun
        
    def touch(self):   self.touch = True
    def untouch(self): self.touch = False
    def 