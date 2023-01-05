.data
n: .long 8
v: .long 15,21,15,30,30,13,15,30
maxi: .long 0
ap: .long 0
format: .asciz "Maximul este %d si apare de %d ori in vector\n"

.text

.globl main
main:

lea v,%edi
mov $0,%ecx

et_loop1:
cmp %ecx,n
je et_for_exit

movl (%edi,%ecx,4),%ebx
cmp maxi,%ebx
jg maxim

et_loop2:
cmp maxi,%ebx
je aparitii

et_loop3:
add $1,%ecx
jmp et_loop1

maxim:
mov $0,%eax
mov %eax,ap
mov %ebx,maxi
jmp et_loop2

aparitii:
incl ap
jmp et_loop3

et_for_exit:
push ap
push maxi
push $format
call printf
pop %ebx
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
