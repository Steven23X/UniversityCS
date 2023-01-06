s=input()
for i in range(len(s)):
    if s[i] in "AEIOUaeiou":
        s=s[:i]+s[i+1:]
        break

print(s)
