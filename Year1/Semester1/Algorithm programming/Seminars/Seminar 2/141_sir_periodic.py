"""
Se da un sir s. Sa se verifice daca este periodic
(exista un sir t si un numar k>1 astfel incat s=t+..+t de k ori (s = t*k)
Daca exista mai multe astfel de siruri t, se va afisa cel mai mare.
s = abbaabbaabbaabba => t=abbaabba
"""
s=input()
#obs: len(t)|len(d)
#varianta 1: consideram pe rand t = prefix de lungime divizor al lui len(s)
# in ordine descrescatoare dupa len(t) si verificam daca t este perioada
len_s =len(s)
for d in range (len(s)//2, 0, -1):
    if len_s % d == 0:
        rez=len_s//d
        if s[:d]*rez==s:
            print(rez)
            print(s[:d])
            break
else:
    print("sirul nu este periodic")

len_s =len(s)
for d in range (len(s)//2, 0, -1):
    if len_s % d == 0:
        rez=len_s//d
        for x in range(d,len_s-d,d):
            if s[:d]!=s[x:x+d]:
                break
        else:
            print(rez)
            print(s[:d])
            break
else:
    print("sirul nu este periodic")
