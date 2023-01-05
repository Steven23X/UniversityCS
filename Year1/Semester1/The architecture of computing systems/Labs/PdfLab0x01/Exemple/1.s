.data
	x: .long 2
	y: .long 1
	z: .long 3
	rez: .space 4
	formatPrintf: .asciz "%ld\n"
.text
.globl main
main:
	;//((x+y)*(x-y)*(x+z))/(y+z)
	movl z,%eax  ;//y+z
	addl y,%eax
	pushl %eax
	
	movl x,%eax ;//x+z,y+z
	addl z,%eax
	pushl %eax
	
	movl x,%eax ;//x-y,x+z,y+z
	subl y,%eax
	pushl %eax
	
	movl x,%eax ;//x+y,x-y,x+z,y+z
	addl y,%eax
	pushl %eax
	
	popl %eax
	popl %ebx
	mull %ebx
	pushl %eax ;//(x+y)*(x-y),x+z,y+z
	
	popl %eax
	popl %ebx
	mull %ebx
	pushl %eax ;//(x+y)*(x-y)*(x+z),y+z
	
	xor %edx,%edx
	pushl %eax
	pushl %ebx
	divl %ebx
	
	pushl %eax ;//((x+y)*(x-y)*(x+z))/y+z
	popl rez
	
	pushl rez
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
et_exit:
mov $1,%eax
xor %ebx,%ebx
int $0x80
