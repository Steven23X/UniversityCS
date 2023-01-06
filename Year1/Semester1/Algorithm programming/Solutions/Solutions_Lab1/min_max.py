n=int(input("n="))
a=int(input())
mini=maxi=a
n-=1
while n>0:
    b=int(input())
    if b>a : maxi=b
    elif b<a: mini=b
    a=b
    n-=1

print("Maximul este",maxi,"si Minimul este",mini)