.data
n: .long 5
v: .long 5,19,3,17,8
afisare: .asciz "Maximul este %d\n"
maxi: .long 0
.text
.globl main
main:
mov $v,%edi
mov $0,%ecx

et_for:
cmp n,%ecx
je et_exit_for
movl (%edi,%ecx,4),%ebx
cmp maxi,%ebx
jg maxim
incl %ecx
jmp et_for

maxim:
movl %ebx,maxi
incl %ecx
jmp et_for

et_exit_for:
push maxi
push $afisare
call printf
pop %ebx
pop %ebx


et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
