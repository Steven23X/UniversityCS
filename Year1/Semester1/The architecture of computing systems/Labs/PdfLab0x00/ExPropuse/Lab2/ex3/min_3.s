.data
a: .long 4
b: .long 9
c: .long 1
min: .space 4
.text
.globl main

main:
mov a,%eax
cmp b,%eax
jl caz1
jmp caz2

caz1:
mov a,%eax
cmp c,%eax
jl caz3
mov c,%eax
mov %eax,min
jmp et_exit

caz2:
mov b,%eax
cmp c,%eax
jl caz4
mov c,%eax
mov %eax,min
jmp et_exit

caz3:
mov a,%eax
mov %eax,min
jmp et_exit

caz4:
mov b,%eax
mov %eax,min
jmp et_exit

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80 
 
