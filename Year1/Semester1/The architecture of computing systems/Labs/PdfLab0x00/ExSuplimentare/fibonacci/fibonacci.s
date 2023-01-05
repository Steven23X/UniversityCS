.data
n : .long 100
nu_intreg: .asciz "%d nu este intreg pozitiv\n"
afisare : .asciz "Termenul %d al sirului Fibonacci este %d\n"
f1 :.long 0
f2 :.long 1
f: .space 4
cn: .space 4
.text
.globl main

main:
movl n,%ebx
movl %ebx,cn
mov $0,%eax
cmp n,%eax
jg afis_negativ

cmp n,%eax
je afis_0

add $1,%eax
cmp n,%eax
je afis_1

subl $2,cn
movl $1,%ecx

et_loop:
cmp cn,%ecx
jg afis
mov $0,%eax
add f2,%eax
add f1,%eax
mov %eax,f

mov f2,%eax
mov %eax,f1

mov f,%eax
mov %eax,f2

add $1,%ecx
jmp et_loop

afis_0:
push f1
push n
push $afisare
call printf
pop %ebx
pop %ebx
jmp et_exit

afis_1:
push f2
push n
push $afisare
call printf
pop %ebx
pop %ebx
jmp et_exit

afis:
push f
push n
push $afisare
call printf
pop %ebx
pop %ebx
jmp et_exit

afis_negativ:
push n
push $nu_intreg
call printf
pop %ebx
pop %ebx
jmp et_exit

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
