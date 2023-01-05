.data
n: .long 13
d: .long 3
rest: .long 0
comp: .space 4
test: .space 4
cond: .space 4
prim: .asciz "Este prim\n"
neprim: .asciz "Nu este prim\n"
sum: .long 1
.text
.globl main
main:

//n<2
mov $2,%ebx
mov %ebx,comp
mov n,%eax
cmp comp,%eax
jl et_neprim

//n==2
cmp comp,%eax
je et_prim

//n%2==0
mov $0,%edx
mov comp,%ebx
idiv %ebx
mov %edx,rest
mov $0,%eax
cmp rest,%eax
je et_neprim

et_loop:

//d*d
mov d,%eax
mov d,%ebx
imul %ebx
mov %eax,cond

//d*d<=n
mov cond,%eax
cmp n,%eax
jg et_prim
mov n,%eax
mov d,%ebx
idiv %ebx
mov %edx,rest

//n%d==0
mov rest,%eax
mov $0,%ebx
mov %ebx,comp
cmp comp,%eax
je et_neprim
mov $1,%eax
add %eax,d
jmp et_loop

et_prim:
mov $4,%eax
mov $1,%ebx
mov $prim,%ecx
mov $11,%edx
int $0x80
jmp et_exit

et_neprim:
mov $4,%eax
mov $1,%ebx
mov $neprim,%ecx
mov $14,%edx
int $0x80
jmp et_exit

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
