s="abccabcababcc"
t="abc"
print(f'''sirul t="{t}" apare ca subsir in sirul "{s}" incepand cu pozitiile :''',end=" ")
poz=s.find(t)
print(poz,end=" ")
while s!=None:
    poz=s.find(t,poz+len(t))
    if poz==-1:
        break
    print(poz,end=" ")

