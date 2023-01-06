s=input()
ls=s.split(" ")
sum=0
for x in ls:
    if x.isdigit():
        sum+=int(x)

print(sum)
