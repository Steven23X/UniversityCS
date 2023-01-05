.data
x: .long 0
.text
.globl main
main:
mov $0,%eax
mov $3,%ah
mov $8,%al
mov %eax,x

mov $1,%eax
mov $0,%ebx
int $0x80
