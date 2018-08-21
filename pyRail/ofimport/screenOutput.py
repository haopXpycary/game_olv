from control import *
from constName import *
from func import cprint

from copy import deepcopy

class screenOutput:
    def __init__(self):
        self.x = MaxScrX
        self.y = MaxScrY
        
        self.screen = []
        for i in range(self.y):
            self.screen.append([])
            for j in range(self.x):
                self.screen[i].append([' ',Black,Unflush])
                
        self.nscreen = deepcopy(self.screen)
        
    def update(self,x,y,pic,color=White,flag=Unflush):
        self.nscreen[y][x] = [pic,color,flag]
        
    def show(self):
        for i in range(len(self.nscreen)):
            for j in range(len(self.nscreen[i])):
                cprint(j,i,,self.nscreen[i][j][0],self.nscreen[i][j][1],Black)
                if self.nscreen[i][j][2] == Flush: self.nscreen[i][j] = [' ', White, Unflush]
        self.screen = deepcopy(self.nscreen)
        
    def updateShow(self):
        for i in range(len(self.screen)):
            for j in range(len(self.screen[i])):
                if self.screen[i][j] == self.nscreen[i][j]:
                    cprint(j,i,self.nscreen[i][j][0],self.nscreen[i][j][1],Black)
                if self.nscreen[i][j][2] == Flush: self.nscreen[i][j] = [' ', White, Unflush]
        self.screen = deepcopy(self.nscreen)
		
if __name__ == "__main__":
	sb = screenOutput()
	sb.show()
	sb.update(1,2,'1',White,Flush)
	sb.updateShow()
	sb.updateShow()