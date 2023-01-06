text="Vreau media aritmetica dintre 30,50;100,20"
sum=0
nr=0
rez=['(']
for x in "!?,;:. ":
    text = text.replace(x, " ")
ls=text.split()

for x in ls:
    if x.isdigit():
        sum+=int(x)
        nr+=1
        if nr==1:
            rez.append(x)
        else:
            rez.append('+')
            rez.append(x)

rez.append(f")\{nr}={sum/nr}")
print("".join(rez))
