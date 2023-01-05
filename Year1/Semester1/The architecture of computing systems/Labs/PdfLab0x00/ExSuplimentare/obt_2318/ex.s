.data
formatn : .asciz "Daca ah este %d si al este %d , atunci ax este %d\n"
rez1: .space 4
rez2: .space 4
rez3: .space 4
.text
.globl main
main:
mov $9,%ah
mov $14,%al

mov %ah,rez3
mov %al,rez2
mov %ax,rez1

push rez1
push rez2
push rez3
push $formatn
call printf
pop %ebx
pop %ebx
pop %ebx
pop %ebx


et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
