"""
varianta 1- cu comprehension
"""
#text = input()
ls = [f"{x}p{x.lower()}" if x.lower() in "aeiou" else x for x in input()]
ls = "".join(ls)
print(ls)

#varianta 2 - fara comprehension
text = input()
ls=[]
for x in text:
    if x.lower() in "aeiou":
        ls.append(x+"p"+x.lower()) #(sau f"{x}p{x.lower()}")
    else:
        ls.append(x)
print(ls)
ls="".join(ls)
print(ls)