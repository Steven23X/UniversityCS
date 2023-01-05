.data
n: .long 7
v: .long 15,27,15,32,32,18,27
singular: .long 0
format: .asciz "Elementul singular este %d\n"
.text
.globl main
main:

lea v,%edi
mov $0,%ecx

et_loop:
cmp n,%ecx
je afisare

movl (%edi,%ecx,4),%ebx

xor %ebx,singular
incl %ecx
jmp et_loop

afisare:
push singular
push $format
call printf
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

