s=input()
semne=";.,!?"
d="".maketrans(semne,"     ","aeiouAEIOU")
print(s.translate(d))
