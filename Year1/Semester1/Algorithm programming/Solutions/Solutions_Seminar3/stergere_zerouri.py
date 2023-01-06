
ls=[1,0,0,2,0,0,3]

for x in range(len(ls)):
    if ls[x]=='0':
        del ls[x]

print(ls)
