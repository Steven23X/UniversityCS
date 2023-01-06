def f2tof10(x):
    rez=0
    p2=1
    while x>0:
        c=x%10
        x=x//10
        rez=rez+c*p2
        p2*=2
    return rez

print(f2tof10(1111))
