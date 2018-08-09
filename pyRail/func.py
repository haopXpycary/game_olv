from control import SYSTEM
from errorDefine import SystemUncompatibleError
from constName import *

class dict():
    def __init__(self):
        self.key = []
        self.value = []
    
    def __setitem__(self,key,value):
        self.key.append(key)
        self.value.append(value)
    
    def __getitem__(self,name):
        return self.value[self.key.index(name)]
                
    def __delitem__(self,name):
        del self.value[self.key.index(name)]
        del self.key[self.key.index(name)]
        
    def clear(self):
        del self.key
        del self.value
        self.key = []
        self.value = []
    
    def values(self):
        return self.value
    
    def keys(self):
        return self.key

if SYSTEM == 0: # winsows
    from os import system
    
    def cprint(color,bgcolor,*other):
        if color == Black: con = "0"
        elif color == Red: con = "4"
        elif color == Green: con = "A"
        elif color == Orange: con = "6"
        elif color == Blue: con = "1"
        elif color == Purple: con = "5"
        elif color == DarkGreen: con = "2"
        elif color == White: con = "F"
        
        
        if bgcolor == Black: bgcon = "0"
        elif bgcolor == Red: bgcon = "4"
        elif bgcolor == Green: bgcon = "A"
        elif bgcolor == Orange: bgcon = "6"
        elif bgcolor == Blue: bgcon = "1"
        elif bgcolor == Purple: bgcon = "5"
        elif bgcolor == DarkGreen: bgcon = "2"
        elif bgcolor == White: bgcon = "F"
        
		# It may con't work.
        system("color "+bgcon+con)
        print(*other,end="")
        
        system("color 0F")
        
elif SYSTEM == 1: # Linux | Unix
    def cprint(color,bgcolor,*other):
        if not other: return;
        
        if color == Black: con = "\033[30m"
        elif color == Red: con = "\033[31m"
        elif color == Green: con = "\033[32m"
        elif color == Orange: con = "\033[33m"
        elif color == Blue: con = "\033[34m"
        elif color == Purple: con = "\033[35m"
        elif color == DarkGreen: con = "\033[36m"
        elif color == White: con = "\033[37m"
        
        
        if bgcolor == Black: bgcon = "\033[40m"
        elif bgcolor == Red: bgcon = "\033[41m"
        elif bgcolor == Green: bgcon = "\033[42m"
        elif bgcolor == Orange: bgcon = "\033[43m"
        elif bgcolor == Blue: bgcon = "\033[44m"
        elif bgcolor == Purple: bgcon = "\033[45m"
        elif bgcolor == DarkGreen: bgcon = "\033[46m"
        elif bgcolor == White: bgcon = "\033[47m"
        
        print(con+bgcon,"\b"+other[0],*other[1:],"\b\033[0m",end="")
        
else:
    raise SystemUncompatibleError("This game may not work on your system.")
    
if __name__ == "__main__":
    dic = dict()
    dic['he'] = 3
    dic[2]    = 4
    print(dic.values())
    print(dic.keys())
    cprint(Blue,White,"Hello World!")