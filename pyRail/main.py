from ofimport.errorDefine import *
from ofimport.constName   import *
from ofimport.control     import *

from before import *

while True:
    pressKey = get.ch
    get.ch = Null
    
    while True:
        print(pressKey)