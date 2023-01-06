#1
s=input("propozitie:")
ls=[x for x in s.split() if x[0] in "aeiouAEIOU"]
print(ls)

