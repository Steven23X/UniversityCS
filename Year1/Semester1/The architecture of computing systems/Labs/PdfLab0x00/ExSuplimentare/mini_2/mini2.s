.data
n: .long 8
v: .long 5,7,25,1,4,-2,4,10
mini1: .long 100
mini2: .long 100
format: .asciz "Minim1 este %d si minim2 este %d\n"
.text
.globl main
main:

lea v,%edi
mov $0,%ecx

et_loop:
cmp n,%ecx
je afisare

movl (%edi,%ecx,4),%ebx

cmp mini1,%ebx
jl minim_1

cmp mini2,%ebx
jl minim_2

after_if:
incl %ecx
jmp et_loop


minim_2:
movl %ebx,mini2
jmp after_if

minim_1:
movl %ebx,mini1
jmp after_if

afisare:
push mini2
push mini1
push $format
call printf
pop %ebx
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

