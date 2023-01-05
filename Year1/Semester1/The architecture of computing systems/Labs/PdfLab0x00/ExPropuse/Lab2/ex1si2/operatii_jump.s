.data
x: .long 64
y: .long 32
z: .long 16
rez1: .space 4
rez2: .space 4
text1: .asciz "PASS\n"
text2: .asciz "FAIL\n"
.text
.globl main
main:
//(x/z)+(x*z) mod 1
mov $0,%edx
mov x,%eax
mov z,%ebx
idiv %ebx
mov %eax,rez1

mov y,%eax
mov z,%ebx
imul %ebx
add %eax,rez1

//mod 2
mov x,%eax
divl z
mov %eax,rez2

mov y,%eax
mull z
add %eax,rez2

mov rez2,%eax
//add $1,%eax instr care rez1!=rez2 ==>Fail
cmp rez1,%eax
je egale 
mov $4,%eax
mov $1,%ebx
mov $text2,%ecx
mov $6,%edx
int $0x80
jmp et_exit

egale:
mov $4,%eax
mov $1,%ebx
mov $text1,%ecx
mov $6,%edx
int $0x80

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

