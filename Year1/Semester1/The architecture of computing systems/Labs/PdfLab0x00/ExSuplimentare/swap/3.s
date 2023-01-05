.data
x: .long 15
y: .long 27
afis: .asciz "Dupa executie x este %d si y este %d\n"
.text
.globl main
main:
mov x,%eax
mov y,%ebx

xor %ebx,%eax
xor %eax,%ebx
xor %ebx,%eax

mov %eax,x
mov %ebx,y

push y
push x
push $afis
call printf
pop %ebx
pop %ebx
pop %ebx

et_exit:
mov $1,%eax
mov $0,%ebx
int $0x80
