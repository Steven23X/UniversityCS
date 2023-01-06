f_puncte=open("puncte.in","r")
f_interogari=open("interogari.in","r")
g_interogari=open("interogari.out","w")
d_puncte={}
d_interogare={}
d_afisare={}
for s in f_puncte:
    s=s.strip()
    ls=s.split(" ",2)
    puncte=(int(ls[0]),int(ls[1]))
    eticheta=ls[2]
    d_puncte[puncte] = eticheta

for s in f_interogari:
    s = s.strip()
    ls = s.split(" ", 2)
    puncte=(int(ls[0]),int(ls[1]))
    if ls[-1]=='0':
        if puncte in d_puncte:
            d_puncte.pop(puncte)
    elif puncte in d_puncte:
        g_interogari.write(str(puncte) + d_puncte[puncte]+'\n')
    else:
        g_interogari.write(str(puncte)+"nu exista"+'\n')

g_interogari.write("puncte ramase"+'\n')
for p in d_puncte:
    g_interogari.write(str(p)+":"+d_puncte[p]+'\n')





