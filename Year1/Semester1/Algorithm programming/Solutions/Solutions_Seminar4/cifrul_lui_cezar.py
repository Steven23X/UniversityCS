import string

s=input("text=")
k=int(input("k="))
alfabet=string.ascii_lowercase
print(alfabet)
d="".maketrans(alfabet,alfabet[k:]+alfabet[:k])
print(d)
print(s.translate(d))
