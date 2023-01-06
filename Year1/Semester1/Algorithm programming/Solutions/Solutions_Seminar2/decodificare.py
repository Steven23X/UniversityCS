s="1v3a1c1a1n1t5a2 1m13a1r4e"
t=""

for i in range(len(s)):
    dup=0
    p10=1
    if s[i].isspace(): t=t+" "
    if s[i].isalpha():
        x=i-1
        while s[x].isdigit():
            dup+=int(s[x])*p10
            x-=1
            p10*=10
    t=t+s[i]*dup

print(t)
