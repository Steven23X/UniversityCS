.data
str: .space 51
format: .asciz "%s/n"
format_afis: .asciz "Nr. de vocale este %d\n"
nrvoc: .long 0
.text
.globl main
main:
push $str
push $format
call scanf
pop %ebx
pop %ebx
lea str,%edi
mov $0,%ecx

et_loop:
movb (%edi,%ecx,1),%ah

cmp $0,%ah
je afisare

cmp $'a',%ah
je inc_voc

cmp $'e',%ah
je inc_voc

cmp $'i',%ah
je inc_voc

cmp $'o',%ah
je inc_voc

cmp $'u',%ah
je inc_voc

et_loop2:
inc %ecx
jmp et_loop


inc_voc:
incl nrvoc
jmp et_loop2

afisare:
push nrvoc
push $format_afis
call printf
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
