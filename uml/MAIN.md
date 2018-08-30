### Program

<p style="color: #B0C4DE">
st=>start:     Text
op=>operation: Text
co=>condition: Text
ed=>end:       Text
st->op->cond
cond(yes)->ed
cond(no)->op
</p>

```flow
start=>start: Start
before=>operation: before
main=>operation: main
callBack=>operation: callBack
end=>end: End

start->before->main->callBack->end
```