from random import randint


def citire_vector(nume_fisier):
    f = open(nume_fisier)
    ls = [int(x) for x in f.read().split()]
    k = int(input("k="))
    return k, ls


def poz_rand(v, p, u):
    r = randint(p, u)
    v[r], v[p] = v[p], v[r]
    return poz(v, p, u)


def poz(v, p, u):
    i = p;
    j = u
    depli = 0;
    deplj = -1
    while i < j:
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]
            # depli, deplj = -deplj, -depli
            aux = depli;
            depli = -deplj;
            deplj = -aux;
        i += depli;
        j += deplj

    return i


def sel_k_min(v, k, p, u):
    m = poz_rand(v, p, u)

    if m == k - 1:
        return v[m]
    if m < k - 1:
        return sel_k_min(v, k, m + 1, u)
    return sel_k_min(v, k, p, m - 1)


def sel_k_min_di(v, k):
    return sel_k_min(v, k, 0, len(v) - 1)


k, v = citire_vector("interclasare.in")
print(k, v)
print(sel_k_min_di(v, k))
