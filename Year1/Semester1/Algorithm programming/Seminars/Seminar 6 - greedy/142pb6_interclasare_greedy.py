"""
ls=[int(x) for x in input().split()]
nr=0
while(len(ls)>1):
    x=min(ls)
    ls.remove(x)
    y=min(ls)
    ls.remove(y)
    print(x,y)
    ls.append(x+y)
    nr+=x+y
print("deplasari:",nr)
"""

"""import heapq
ls=[4,9,8,11,10]

h=[]
for x in ls:
    heapq.heappush(h,x) #numemodul.operatie()
print(h)
"""
import heapq
ls=[int(x) for x in input().split()]
h=[]
for x in ls:
    heapq.heappush(h,x)
nr=0
while len(h)>1:
    x=heapq.heappop(h)
    y=heapq.heappop(h)
    print(x,y)
    heapq.heappush(h,x+y)
    nr+=x+y
print("nr de operatii:",nr)
"""x=heapq.heappop(h)
print(x)
print(h)
heapq.heappush(h,3)
print(h)
"""
