import os

from ofimport.errorDefine import *
from ofimport.constName   import *
from ofimport.control     import *
from ofimport.func        import *

#==============system test=================
if SYSTEM == 1: # Linux | Unix 
    pass
else:
    raise SystemUncompatibleError("This game may not work on your system.")
    
#==============prepare=====================
#隐藏光标
print("\033[?25l",end="")
os.system("clear")

#监听键盘
get = keyboardListen()
get.start()

#屏幕初始化
scr = scrControl()
scr.show()


#==============define======================
from playerDefine import *
