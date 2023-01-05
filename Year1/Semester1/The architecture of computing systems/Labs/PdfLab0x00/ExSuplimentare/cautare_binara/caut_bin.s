.data
m: .space 4
st: .space 4
dr: .space 4
poz: .long 0
x: .long 120
n: .long 13
v: .long 5,8,11,22,37,41,52,69,72,85,90,91,97
afis_da: .asciz " %d este in vector pe pozitia %d \n"
afis_nu: .asciz " %d nu se afla in vector \n"
.text
.globl main

main:
movl $0,st
mov n,%eax
mov %eax,dr

lea v,%edi
mov $0,%ecx

et_loop:

movl poz,%eax
cmp $0,%eax
jne afisare_gasit

movl dr,%eax
cmp st,%eax
jl afisare_negasit

movl $0,%edx
mov dr,%eax
add st,%eax
movl $2,%ebx
idiv %ebx

mov %eax,m

movl m,%ecx
movl (%edi,%ecx,4),%ebx

cmp x,%ebx
je gasit

cmp x,%ebx
jl stanga

cmp x,%ebx
jg dreapta

jmp et_loop


stanga:
mov %ecx,st
incl st
jmp et_loop

dreapta:
mov %ecx,dr
decl dr
jmp et_loop

gasit:
mov %ecx,poz
incl poz
jmp afisare_gasit

afisare_gasit:
push poz
push x
push $afis_da
call printf
pop %ebx
pop %ebx
pop %ebx
jmp et_exit

afisare_negasit:
push x
push $afis_nu
call printf
pop %ebx
pop %ebx
jmp et_exit

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
