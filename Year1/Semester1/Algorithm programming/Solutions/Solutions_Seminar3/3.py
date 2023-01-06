import string
l_litere=list(string.ascii_lowercase)
nr_litere=(len(l_litere))
text=input("text=")
k=int(input("cheie="))
prop_cezar="".join([chr((ord(c)-ord('a')+k)%nr_litere+ord('a')) if "a"<=c<="z" else c for c in text]) #c.isalpha()
print(prop_cezar)
