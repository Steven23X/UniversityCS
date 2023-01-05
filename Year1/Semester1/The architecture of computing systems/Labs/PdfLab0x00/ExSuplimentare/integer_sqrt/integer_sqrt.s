.data
n : .long 230512123
n0: .long 0
n1: .long 0
rez: .long 0
format1: .asciz "%d"
format: .asciz "[sqrt(%d)] este %d\n" 
.text
.globl main
main:
push n
push $format1
call scanf
pop %ebx
pop %ebx

mov $1,%eax
cmp n,%eax
jge afisare_n

movl $0,%edx
movl n,%eax
movl $2,%ebx
idiv %ebx
movl %eax,n0

movl $0,%edx
movl n,%eax
movl n0,%ebx
idiv %ebx

movl $0,%edx
addl n0,%eax
movl $2,%ebx
idiv %ebx
movl %eax,n1

et_loop:
movl n0,%eax
movl n1,%ebx
cmp %eax,%ebx
jge afisare

movl %ebx,n0

movl $0,%edx
movl n,%eax
movl n0,%ebx
idiv %ebx

movl $0,%edx
addl n0,%eax
movl $2,%ebx
idiv %ebx
movl %eax,n1
jmp et_loop

afisare:
push n0
push n
push $format
call printf
pop %ebx
pop %ebx
pop %ebx
jmp et_exit

afisare_n:
push n
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
