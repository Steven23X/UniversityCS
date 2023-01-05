.data
s: .asciz "abcde"
n: .long 5
t: .space 6
.text
.globl main
main:

lea s,%edi   
lea t,%esi

mov n,%ecx
mov $0,%eax

et_for:
cmp $-1,%ecx 
je et_for_exit

movl (%edi,%ecx,1),%ebx  
movl  %ebx,(%esi,%eax,1)

dec %ecx
inc %eax

jmp et_for

et_for_exit:
mov $4,%eax
mov $1,%ebx
mov $t,%ecx
mov $6,%edx
int $0x80

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80

