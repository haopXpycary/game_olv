### Program

```flow
start=>start: Start
constName=>condition: constName & control 
msg=>operation: # Not allowed to import anything
func=>operation: function & class
define=>operation: define
before=>operation: before
main=>operation: main
callBack=>operation: callBack
end=>end: End

start->constName
constName(no)->func->define->before->main->callBack->end
constName(yes)->msg
```

![main_uml](https://github.com/haopXpycary/game_olv/blob/master/uml/main_uml.svg)
