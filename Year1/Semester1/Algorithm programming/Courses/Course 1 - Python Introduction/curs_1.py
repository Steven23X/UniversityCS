'''
i = 1
while i<10:
    print(i,end=" ") #linie noua
    i = i+1 #i+=1
print("gata", "programul", sep="+")
print(type(i))
i="abc"
print(type(i))
i=input("introduceti numar ")
#=>str, sirul introdus pana la sfarsitul de linie
i=int(i)
print(i, type(i))
x=int(input())
print(x)
'''
m=1000000
print(m,id(m))
m=m+1
print(m,id(m))
x=m
print(x,id(x))

x=1+1000000
print(x,id(x))