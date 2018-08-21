class inscription:
    def __init__(self,level,addintionType,addintionValue):
        self.level = level
        self.addintionType = addintionType
        sel.addintionValue = addintionValue
    
    def mixIn(self,other1,other2):
        if self.level == other1.level == other2.level:
            if self.addintionType == other1.addintionType == other2.addintionType:
                return inscription(self.level+1,self.addintionType,(self.addintionValue+other1.addintionValue+other2.addintionValue)*1.2)
