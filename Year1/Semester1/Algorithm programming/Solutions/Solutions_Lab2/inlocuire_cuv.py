sir="ana, are! mere, ana?"
s="ana"
cuv="pere"
cs=s
ccuv=cuv
for x in ",.!?: ":
    ccuv=ccuv+x
    cs=cs+x
    sir=sir.replace(s,cuv)
    cs=s
    ccuv=cuv

print(sir)
