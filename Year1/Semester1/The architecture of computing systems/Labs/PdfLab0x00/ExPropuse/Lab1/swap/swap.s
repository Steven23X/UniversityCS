.data
x: .long 20
y: .long 5
.text
.globl main
main:
mov x,%eax
mov y,%ebx
mov %ebx,x
mov %eax,y

mov $1,%eax
mov $0,%ebx
int $0x80
