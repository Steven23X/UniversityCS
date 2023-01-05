//suma de la 0 la n
.data
n: .long 6
s: .space 5
.text
.globl main
main:
mov n,%ecx
//sub $1,%ecx daca vrem suma de la 0 la n-1

sum:
add %ecx,s
loop sum
jmp etexit

etexit:
mov $1,%eax
mov $0,%ebx
int $0x80

