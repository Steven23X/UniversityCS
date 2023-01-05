.data
x: .long 2
y: .long 5
text1: .asciz "x>=y"
text2: .asciz "x<y"
.text
.globl main

main:
mov x,%eax
cmp y,%eax
jl afis1

mov $4,%eax
mov $1,%ebx
mov $text1,%ecx
mov $5,%edx
int $0x80
jmp et_exit

afis1:
mov $4,%eax
mov $1,%ebx
mov $text2,%ecx
mov $4,%edx
int $0x80
jmp et_exit

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

