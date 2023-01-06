def f10to2(x):
    rez=0
    p10=1
    while x>0:
        a=x%2
        x=x//2
        rez=rez + p10*a
        p10*=10
    return rez

print(f10to2(10))


