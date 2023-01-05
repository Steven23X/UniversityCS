.data
n: .long 7
factorial: .long 1
format : .asciz "%d! factorial este %d\n"
.text
.globl main
main:
movl $1,%ebx
et_loop:
cmp n,%ebx
jg afis

mov factorial,%eax
imul %ebx

mov %eax,factorial

incl %ebx
jmp et_loop


afis:
push factorial
push n
push $format
call printf
pop %ebx
pop %ebx
pop %ebx

et_exit:

mov $1,%eax
mov $0,%ebx
int $0x80

