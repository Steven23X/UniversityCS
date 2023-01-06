f=open("intervale.in","r")
g=open("date.txt","w")
# intervale=[tuple(x[1:len(x)-1].split(",")) for x in f.readline().strip().split(", ")]4
poz=1
intervale = sorted([(int(x), int(y)) for (x, y) in [tuple(x[1:len(x)-1].split(",")) for x in f.readline().strip().split(", ")]],key = lambda x : x[0])
print(intervale)