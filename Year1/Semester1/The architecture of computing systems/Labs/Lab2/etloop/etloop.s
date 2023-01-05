//suma de la 0 la n-1
.data
s: .space 5
n: .int 7
.text
.globl main
main:
mov $0,%ecx

etloop:
cmp n,%ecx
je et_exit
add %ecx,s
inc %ecx
jmp etloop

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

