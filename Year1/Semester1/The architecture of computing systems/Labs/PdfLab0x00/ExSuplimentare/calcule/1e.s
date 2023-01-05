.data
afis: .asciz "%d\n"
x: .space 4
y: .space 4
.text
.globl main
main:
mov %ebx,x
mov %eax,y

and %eax,x
and %ebx,y

movl x,%ecx
or %ecx,y

mov y,%eax

push %eax
push $afis
call printf
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
