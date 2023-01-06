s=input()

x=len(s)//2+1
for i in range(1,x):
    t=s[i:len(s)-i]
    while i:
        print(" ",end="")
        i-=1
    print(t)


