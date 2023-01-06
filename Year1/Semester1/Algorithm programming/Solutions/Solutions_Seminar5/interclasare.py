

'''
a=0
while(len(l)>=2):
    min1=min(l)
    l.remove(min1)
    min2=min(l)
    l.remove(min2)
    s=min2+min1
    l.append(s)
    a+=s

print(a)
'''
import heapq

h=[]

with open("interclasare.in","r") as f:
    l=list(map(int,f.readline().split(", ")))

for i in range(len(l)):
    l[i] = (l[i],str(i+1))

heapq.heapify(l)
total=0
while len(l)>=2:
    min1 = heapq.heappop(l)
    min2 = heapq.heappop(l)
    heapq.heappush(l,(min1[0]+min2[0],f"interclasare({min1[1]},{min2[1]})"))
    total =total + min1[0]+min2[0]

print(total,"operatii")
print(l[0][1])