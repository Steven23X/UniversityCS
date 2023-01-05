.data
n: .space 4
citire: .asciz "%d"
afisare: .asciz "%d biti de 1\n"
nr: .long 0
.text
.globl main
main:

push $n
push $citire
call scanf
pop %ebx
pop %ebx

mov $0,%ecx
cmp n,%ecx
jg pozitiv

et_loop:
cmp n,%ecx
je et_afisare

movl n,%eax
and $1,%eax

cmp $1,%eax
je increase

end_if:

movl n,%ebx
shr $1,%ebx
movl %ebx,n

jmp et_loop

increase:

incl nr
jmp end_if

pozitiv:

movl n,%eax
movl $-1,%ebx
imul %ebx
mov %eax,n
jmp et_loop

et_afisare:
push nr
push $afisare
call printf
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
