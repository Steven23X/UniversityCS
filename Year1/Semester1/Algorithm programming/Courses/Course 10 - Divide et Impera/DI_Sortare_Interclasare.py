def citire_vector(nume_fisier):
    f=open(nume_fisier)
    ls=[int(x) for x in f.read().split()]
    return ls

def sort_interclasare(v, p, u):
   if p==u:
	   pass
   else:
        m = (p+u)//2
        sort_interclasare(v, p, m)
        sort_interclasare(v, m+1, u)
        interclaseaza(v, p, m, u)



def interclaseaza(a, p, m, u):
	b = [0]*(u-p+1)
	i = p;  j = m + 1; k = 0
	while (i<=m) and (j <= u):
			if a[i] <= a[j]:
				b[k] = a[i]; i += 1
			else:
				b[k] = a[j]; j+= 1
			k+=1

	while i<=m:
		b[k] = a[i]; k += 1; i += 1

	while j<=u:
		b[k] = a[j]; k += 1; j += 1

	for i in range(p,u+1):
		a[i] = b[i-p]




def sortare(v):
	n=len(v)
	sort_interclasare(v,0,n-1)

v=citire_vector("interclasare.in")
sortare(v)
print(v)