from ofimport.player import player
from ofimport.constName import *
from skillDefine import *

PringPole = player()
PringPole.initBaseMsg("PringPole")
PringPole.initActivity()
PringPole.initAdditionalAttributes()
PringPole.initArmor()
PringPole.initBackpack()
PringPole.initBaseAttributes(baseHealth=20,baseProtect=4,baseAttack=10,baseMagic=10)
PringPole.initDevelopableAttributes(developableHealth=1,developableProtect=1,developableAttack=1,developableMagic=1)
PringPole.initLevel()
PringPole.initMoney()
PringPole.initPlace(0,0,Right,'i')
PringPole.initSkills([HealthAdd])