def di (a,x,y,n):
    if n>1:
        di(a,x,y+n//2,n//2)



n =int(input("n= "))
a=[[ 0 for x in range(n)] for y in range(n)]
print(a)

print(di(a,0,0,n))