import math
l1=int(input("l1="))
l2=int(input("l2="))

aria=l1*l2

while l2>0:
    r=l1%l2
    l1=l2
    l2=r

l_placa=l1

nr_placi=aria//(l_placa*l_placa)

print("Mesterul are nevoie de ",nr_placi,"placi de dimensiunea",l_placa)
