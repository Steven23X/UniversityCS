.data
afis: .asciz "%d\n"
.text
.globl main
main:
xor %eax,%eax

push %eax
push $afis
call printf
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
