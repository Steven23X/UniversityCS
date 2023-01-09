.data
	;//declarare variabile
	m1: .space 40000
	m2: .space 40000
	mres: .long 0
	edgesVector: .space 400
	exercise: .space 4
	nodesNumber: .space 4
	pathLength: .space 4
	sourceNode: .space 4
	destinationNode: .space 4
	conditionMatrix: .space 4
	mmapLength: .space 4
	x: .space 4
	i: .space 4
	j: .space 4
	
	;//format pentru call
	formatScanf: .asciz "%ld"
	formatPrintf: .asciz "%ld "
	newLine: .asciz "\n"
.text
	;//procedura matrix_mult(m1, m2, mres, n)
matrix_mult:
	pushl %ebp
	mov %esp,%ebp
	
	;//variabile locale
	subl $24,%esp
	movl $0, -4(%ebp) ;//i
	movl $0, -8(%ebp) ;//j
	movl $0, -12(%ebp) ;//k
	movl $0, -16(%ebp) ;//i*n+j
	movl $0, -20(%ebp) ;//i*n+k
	movl $0, -24(%ebp) ;//k*n+j
	
	;//push la registrii care trebuie restaurati
	pushl %ebx
	pushl %esi
	pushl %edi
	
	;//echivalent in c:
	;//for(int i=0;i<n;i++)
    	;//	for(int j=0;j<n;j++)
        ;//		for(int k=0;k<n;k++)
        ;//    			mres[i*n+j]+=m1[i*n+k]*m2[k*n+j];
        
et_matrix_mult_for1:
	movl -4(%ebp),%ecx
	cmp 20(%ebp),%ecx
	je et_matrix_mult_exit
	
	et_matrix_mult_for2:
		movl -8(%ebp),%ecx
		cmp 20(%ebp),%ecx
		je et_matrix_for2_exit
		
		;//calculare i*n+j
		movl $0,%edx
		movl -4(%ebp),%eax
		mull 20(%ebp)
		addl -8(%ebp),%eax
		movl %eax,-16(%ebp)
			
		et_matrix_mult_for3:
			movl -12(%ebp),%ecx
			cmp 20(%ebp),%ecx
			je et_matrix_for3_exit
			
			;//calculare i*n+k
			movl $0,%edx
			movl -4(%ebp),%eax
			mull 20(%ebp)
			addl -12(%ebp),%eax
			movl %eax,-20(%ebp)
			
			;//calculare k*n+j
			movl $0,%edx
			movl -12(%ebp),%eax
			mull 20(%ebp)
			addl -8(%ebp),%eax
			movl %eax,-24(%ebp)
			
			;//m1[i*n+k]*m2[k*n+j]
			movl 8(%ebp),%edi
			movl -20(%ebp),%ecx
			movl (%edi,%ecx,4),%eax
			
			movl 12(%ebp),%edi
			movl -24(%ebp),%ecx
			movl (%edi,%ecx,4),%ebx
			
			movl $0,%edx
			mull %ebx
			
			;//mres[i*n+j]+=m1[i*n+k]*m2[k*n+j]
			movl  16(%ebp),%edi
			movl -16(%ebp),%ecx
			movl (%edi,%ecx,4),%ebx
			addl %eax,%ebx
			movl -16(%ebp),%ecx
			movl %ebx,(%edi,%ecx,4)
			
			incl -12(%ebp)
			jmp et_matrix_mult_for3
		
	et_matrix_for3_exit:
		movl $0,-12(%ebp)
		incl -8(%ebp)
		jmp et_matrix_mult_for2
		
et_matrix_for2_exit:
	movl $0,-8(%ebp)
	incl -4(%ebp)
	jmp et_matrix_mult_for1 
	
et_matrix_mult_exit:
	;//pop pentru a ajunge la adresa de retur
	popl %edi
	popl %esi
	popl %ebx
	addl $24,%esp	
	popl %ebp
	ret

.globl main
main:	
	;//citire numarul exercitiului si numarul de noduri
	pushl $exercise
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $nodesNumber
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx

	movl $0,i
	
	;//crearea unui vector de legaturi
	;//echivalent in c:
	;//for(int i=0;i<n;i++)
    	;//    {scanf("%ld", x);
    	;//	v[i]=x;}
    
et_for1:
	movl i,%ecx
	cmp nodesNumber,%ecx
	je et_exit_for1
	
	pushl $x
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	lea edgesVector,%edi
	movl i,%ecx
	movl x,%ebx
	movl %ebx,(%edi,%ecx,4)
	
	incl i
	jmp et_for1
		
et_exit_for1:
	;//verificare daca este cerinta 3
	movl exercise,%eax
	cmp $3,%eax
	je exercise3
	
	jmp et_exit

exercise3:
	;//cerinta 3
	movl $0,i
	
	;//construire m1 si m2
	;//echivalent in c:
	;//for(int i=0;i<n;i++)
    	;//	while(v[i])
        ;//	   {scanf("%ld",x);
        ;//	   m1[i*n+x]=1;
        ;//	   m2[i*n+x]=1;
	;//	   v[i]--;}
	
et_for2_c3:
	movl i,%ecx
	cmp nodesNumber,%ecx
	je et_exit_for2_c3
	
	lea edgesVector,%edi
	movl (%edi,%ecx,4),%edx
	movl %edx,j
	
	et_while_c3:
		movl j,%ecx
		cmp $0,%ecx
		je et_exit_while_c3
		
		pushl $x
		pushl $formatScanf
		call scanf
		popl %ebx
		popl %ebx
		
		movl $0,%edx
		movl i,%eax
		mull nodesNumber
		movl %eax,%ecx
		addl x,%ecx
		
		lea m1,%edi
		movl $1,(%edi,%ecx,4)
		
		lea m2,%esi
		movl $1,(%esi,%ecx,4)
		
		pushl $0
		call fflush
		popl %ebx
		
		decl j
		jmp et_while_c3
		
et_exit_while_c3:
	incl i
	jmp et_for2_c3

	
et_exit_for2_c3:

	;//citire lungimea drumului,nod sursa,nod destinatie
	pushl $pathLength
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $sourceNode
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $destinationNode
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	movl nodesNumber,%eax
	mull nodesNumber
	movl %eax,conditionMatrix
	
	movl $4,%ebx
	mull %ebx
	movl %eax,mmapLength
	
	;//alocare dinaminca mres
	;//void *mmap(void *addr(%ebx), size_t length(%ecx), int prot(%edx), int flags(%esi),int fd(%edi), off_t offset(%ebp));
	
	mov $192,%eax    		;// 192 este codul apelului de sistem mmap2
    	xor %ebx,%ebx    		;// addr = NULL ==> kernelul alege adresa la care va fi creat map-ul
    	mov $mmapLength,%ecx   		;// length = dimensiunea matricei in functie de numarul de noduri ==> mmapLength=nodesNumber*nodesNumber*4 (dimensiune in B)
    	
    	;//in documentatia <sys.mman.h> am gasit valorile pentru prot si flags cu mentiunea : "Protections (and flags) are chosen from these bits, OR'd together."
    	
    	;//pentru arg prot sunt necesare PROT_READ(page can be read) si PROT_WRITE(page can be written) cu valorile 0x1 ,respectiv 0x2 
    	mov $3,%edx     		;// prot = PROT_READ|PROT_WRITE ==> prot = (0x1)|(0x2) = 3 in baza 10
    	
    	;//pentru arg flags sunt necesare MAP_PRIVATE(updateurile la mapare nu sunt vizibile pentru alte procese care mapeaza acelasi *fisier*) si 
    	;//MAP_ANONYMOUS(programul nu foloseste un fisier) cu valorile 0x02 ,respectiv 0x20
    	mov $34,%esi     		;// flags = MAP_PRIVATE|MAP_ANONYMOUS ==> flags=(0x02)|(0x20)= 34 in baza 10
    	
    	;//flag-ul MAP_ANONYMOUS este precizat deci fd este ignorat ,dar trebuie sa pun -1 (conform documentatiei de pe man7.org)
    	mov $-1,%edi     		;// fd = -1
    	
    	;//flag-ul MAP_ANONYMOUS este precizat deci offset este 0 (conform documentatiei de pe man7.org)
    	xor %ebp,%ebp    		;// offset = 0
    	int $0x80        		;// syscall
    	
  	;//in %eax se regaseste pointer-ul catre zona mapata
    	movl %eax,mres
    	
    	
	;//echivalent in c:
	;//pathLength--;
	;//while(pathLength)
    	;//	{matrix_mult(m1,m2,mres,n);
     	;//	for(int i=0;i<n*n;i++)
        ;// 		{m1[i]=mres[i];
        ;// 		mres[i]=0;}
	;//	pathLength--;}
	
	decl pathLength
et_while_pathLength_c3:
	movl pathLength,%ecx
	cmp $0,%ecx
	je et_exit_while_pathLength_c3
	
	pushl nodesNumber
	pushl mres ;//fara $ deoarece valoarea lui mres reprezinta adresa
	pushl $m2
	pushl $m1
	call matrix_mult
	popl %ebx
	popl %ebx
	popl %ebx
	popl %ebx
	
	movl $0,i
	movl $0,%edx
	
	et_for_exchange_c3:
		movl i,%ecx
		cmp conditionMatrix,%ecx
		je et_exit_for_exchange_c3
		
		movl mres,%edi ;//;//fara $ deoarece valoarea lui mres reprezinta adresa
		movl (%edi,%ecx,4),%ebx
		movl $0,(%edi,%ecx,4)
		
		lea m1,%esi
		movl %ebx,(%esi,%ecx,4)
		
		incl i
		jmp et_for_exchange_c3
et_exit_for_exchange_c3:
	decl pathLength
	jmp et_while_pathLength_c3
	

et_exit_while_pathLength_c3:
    	;//dealocare memorie mres
    	;//int munmap(void *addr(%ebx), size_t length(%ecx));
    	
	mov $91,%eax  		  ;//91 este codul apelului de sistem munmap2
    	mov mres,%ebx 		  ;//addr=mres
    	mov $mmapLength,%ecx 	  ;//length=mmapLength=nodesNumber*nodesNumber*4
    	int $0x80		  ;//syscall
    	
	;//numarul de drumuri de lungime k dintre nodul sursa si nodul destinatie
	;//echivalent in c:
	;//printf("%ld",m1[n*sourceNode+destinationNode]) (matricea finala ramane stocata in m1)
	
	movl nodesNumber,%eax
	mull sourceNode
	addl destinationNode,%eax
	mov %eax,%ecx	
	lea m1,%edi
	movl (%edi,%ecx,4),%ebx
	
	push %ebx
	push $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
	push $0
	call fflush
	popl %ebx
	
	movl $4,%eax
	movl $1,%ebx
	movl $newLine,%ecx
	movl $2,%edx
	int $0x80
et_exit:
	mov $1,%eax
	xor %ebx,%ebx
	int $0x80
