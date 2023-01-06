text=input("text:")

print("".join([x+'p'+x.lower() if x in "aeiouAEIOU" else x for x in list(text)]))