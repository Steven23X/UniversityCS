.data
x: .long 89
y: .long 109
nu:.space 4
si:.space 4
a:.space 4
sau: .space 4
sauex: .space 4
.text
.globl main
main:
mov x,%eax
not %eax
mov %eax,nu

mov x,%eax
mov y,%ebx
and %eax,%ebx
mov %ebx,si

mov x,%eax
mov y,%ebx
test %eax,%ebx
mov %ebx,a

mov x,%eax
mov y,%ebx
or %eax,%ebx
mov %ebx,sau

mov x,%eax
mov y,%ebx
xor %eax,%ebx
mov %ebx,sauex

mov $1,%eax
mov $0,%ebx
int $0x80
