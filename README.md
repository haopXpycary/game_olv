## 帮助文档

### [ 运行文件 ]
环境要求: <br />
系统:  GNU/Linux | Unix <br />
语言:  python3 [ 测试环境为3.7.0 ]
```bash
$ cd game_olv/pyRail/
$ chmod +x main.py
$ python3 main.py
```

### [ 完成程度 ]

- [x] player
- [ ] playerDefine
- [x] biological
- [ ] biologicalDefine
- [x] skill & buff
- [ ] skillDefine
- [ ] buffDefine
- [x] thing
- [ ] thingDefine
- [x] inscription
- [ ] inscriptionDefine
- [ ] event & eventDefine
- [x] keybroadListen
- [x] screenOutput
- [ ] main & before

### [ 功能浏览 ]

```
装备
魔法
附魔
铭文
药水
buff
```

### [ 项目结构 ]

```
pyRail/       存放python脚本文件及外部库[ py ]
   tests/     测试文件
   ofimport/  内部库[ py ]
uml/          对于pyRail的项目规划[ uml ]
```

详情请查阅uml/


###  [ 目录列表 ]
/pyRail
```
- player         # 玩家行为及属性定义
- biological     # 生物定义
- thing          # 物品定义
- skill          # 技能及buff定义
- skillDefine    # 技能及buff
- func           # 常用函数
- classc
- control        # 控制变量定义
- constName      # 特殊变量l定义
- screenOutput   # 控制屏幕输出
- before         # 游戏初始化及定义
- errorDefine    # Error定义
- main           # 游戏运行
```

/uml
```
- MAIN
- player
- skill
- thing
- biological
```


###  [ 命名规范 ]
<smart>
  
| 命名类型 | 范例 |
| ------ | ------ |
| 类名       | className     |
| 类变量     | class.valName |
| 函数名     | funcName      |
| 特殊变量名 | ValName       |
| 控制变量   | ConValName    |
| 常函数     | FuncName      |
| 常量       | CONST_NAME    |

</smart>


### [ 作者列表 ]
- haopXpycary


### [ 联系方式 ]
e-mail: *haopxpycary@foxmail.com*

### [ biu~ ]
[一个神奇的地方](https://www.bilibili.com/bangumi/play/ep12514)
