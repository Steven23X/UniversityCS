def citire_vector(nume_fisier):
    f=open(nume_fisier)
    ls=[int(x) for x in f.read().split()]
    return ls

def nr_inversiuni(v, p, u):
   if p==u:
	   return 0
   else:
        m = (p+u)//2
        n1 = nr_inversiuni(v, p, m)
        n2 = nr_inversiuni(v, m+1, u)
        return n1 + n2 + interclaseaza(v, p, m, u)



def interclaseaza(a, p, m, u):
	b = [None]*(u-p+1)
	nr = 0
	i = p;  j = m + 1; k = 0
	while (i<=m) and (j <= u):
			if a[i] <= a[j]:
				b[k] = a[i]; i += 1
			else:
				b[k] = a[j]; j += 1; nr += (m-i+1)
			k+=1

	while i<=m:
		b[k] = a[i]; k += 1; i += 1

	while j<=u:
		b[k] = a[j]; k += 1; j += 1

	for i in range(p,u+1):
		a[i] = b[i-p]

	return nr


def sortare(v):
	n=len(v)
	return nr_inversiuni(v,0,n-1)

def nr_inversiuni_n2(v):
	nr=0
	for i in range(len(v)):
		for j in range(i+1,len(v)):
			if v[i]>v[j]:
				nr+=1
	return nr

v=citire_vector("interclasare.in")
print(v)
print(nr_inversiuni_n2(v))
print(sortare(v))
print(v)

