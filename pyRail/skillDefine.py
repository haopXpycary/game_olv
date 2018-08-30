from ofimport.skill import *

def HealthAdd_(sb):
    sb.health = sb.maxHealth
    
HealthAdd = skill()
HealthAdd.initSkill(1,HealthAdd_)