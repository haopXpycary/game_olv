#系统
# 0: Windows
# 1: Linux | Unix
# 3: Mac
# 4: Other
SYSTEM = 1

# 升级所需经验
LevelUpNeedExp = lambda level: 2 * level ** 2
# 日常饥饿
HungryDailyLower = 1
# 价值计算
CalculatedConst = lambda attack,health,magic,protect,restoreHealth,restoreMagic: attack + health + magic + protect*5 + restoreHealth*10 + restoreMagic*10
# 价值附加率
AttachmentURate = 1.3
# 装备升级成长率
LevelUpGrowthRate = 1.7
# 升级花费增长倍数
UpgradeCostIncreaseMultiple = 20
# 屏幕大小
MaxScrX,MaxScrY = 10,10