.data
afis_zero: .asciz "%d Este zero\n"
afis_pozitiv: .asciz "%d Este pozitiv\n"
afis_negativ: .asciz "%d Este negativ\n"
x: .long -27
comp: .space 4
.text
.globl main
main:
mov x,%eax

movl $0,comp

cmp comp,%eax
je afisare_zero

cmp comp,%eax
jl afisare_negativ

cmp comp,%eax
jg afisare_pozitiv

afisare_zero:
push %eax
push $afis_zero
call printf
pop %ebx
pop %ebx
jmp et_exit

afisare_pozitiv:
push %eax
push $afis_pozitiv
call printf
pop %ebx
pop %ebx
jmp et_exit

afisare_negativ:
push %eax
push $afis_negativ
call printf
pop %ebx
pop %ebx
jmp et_exit

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
