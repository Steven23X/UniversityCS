s=input()
t=s[len(s)::-1]
x=len(s)//2+1
if s[x:]==s[:x-1]: print(f"{s} este semipalindrom")
else:
    print(f"{s} nu este semipalindrom")
if s==t: print(f"{s} este palindrom")
else:
    print(f"{s} nu este palindrom")
