.data
text1: .asciz "1\n"
text2: .asciz "2\n"
text3: .asciz "3\n"
.text
.globl main
main:
jmp afis3

afis1:
mov $4,%eax
mov $1,%ebx
mov $text1,%ecx
mov $3,%edx
int $0x80
jmp afis2

afis2:
mov $4,%eax
mov $1,%ebx
mov $text2,%ecx
mov $3,%edx
int $0x80
jmp et_exit

afis3:
mov $4,%eax
mov $1,%ebx
mov $text3,%ecx
mov $3,%edx
int $0x80
jmp afis1

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

