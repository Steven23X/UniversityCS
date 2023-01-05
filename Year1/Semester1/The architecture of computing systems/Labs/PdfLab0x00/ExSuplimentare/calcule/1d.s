.data
afis: .asciz "%d\n"
x: .space 4
.text
.globl main
main:
mov %eax,x
decl x
and x,%eax

push %eax
push $afis
call printf
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
