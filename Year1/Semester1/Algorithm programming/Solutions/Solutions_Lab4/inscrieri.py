f_elevi=open("inscrieri.in","r")
f_locuri=open("max_locuri.in","r")

def scrie(ls):
    d={}
    x=int(f_locuri.readline())
    for linie in f_locuri:
        l=linie.split(" - ")
        d[l[0]]=x*int(l[1])

    for elev in ls:
        for profil in elev[4:]:
            if d[profil]>0:
                g=open(profil+".out","a")
                g.write(" ".join(elev[:3])+'\n')
                g.close()
                d[profil]-=1
                break


d={}
ls=[]
for linie in f_elevi:
    ls.append(linie.split())

ls=sorted(ls,key = lambda x : -float(x[3]))
scrie(ls)



