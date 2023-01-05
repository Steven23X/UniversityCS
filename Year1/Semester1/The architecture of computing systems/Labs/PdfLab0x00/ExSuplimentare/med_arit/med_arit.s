.data
n: .long 8
v: .long 15,16,17,27,39,17,23,287
suma: .long 0
med_arit: .long 0
rest: .long 0
format: .asciz "Suma elementelor tabloului este %d ,iar media aritmetica este %d rest %d\n"
.text
.globl main

main:
lea v,%edi

mov $0,%ecx

et_loop:
cmp n,%ecx
je med_aritmetica

mov (%edi,%ecx,4),%ebx
add %ebx,suma
incl %ecx

jmp et_loop

med_aritmetica:
mov $0,%edx
mov suma,%eax
mov n,%ebx
idiv %ebx
mov %eax,med_arit
mov %edx,rest

afisare:
push rest
push med_arit
push suma
push $format
call printf
pop %ebx
pop %ebx
pop %ebx
pop %ebx


et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
