
bits 64

section .data
	prompt: db 'Which file you want to encrypt : ', 10, 0

section .text
	global _start
_start:
	sub rsp, 64
	mov rax, 1
	mov rdi, 1
	mov rsi, prompt
	mov rdx, 34
	syscall
	xor rax, rax
	xor rdi, rdi
	mov rsi, rsp
	mov rdx, 64
	syscall
	cmp byte[rsp+rax-1],0xa
	jne no_nl
		mov byte[rsp+rax-1],0
	no_nl:
	mov rax, 2
	mov rdi, rsp
	xor rsi, rsi
	xor rdx, rdx
	syscall
	mov r8, rax 
	loop:
		xor rax, rax
		mov rdi, r8
		mov rsi, rsp
		mov rdx, 1
		syscall
		cmp rax, 0
		je end
		mov al, byte[rsp]
		cmp al, 32
		jl func1 
		cmp al, 64
		jl func2	
		cmp al, 96
		jl func3    
		jmp func4 
		func1:
			add al, 64
			jmp func
		func2:
			sub al, 32
			jmp func
		func3:
			add al, 32
			jmp func
		func4:
			sub al, 64
			jmp func
		func:
			mov byte[rsp], al
			mov rax, 1
			mov rdi, 1
			mov rsi, rsp
			mov rdx, 1
			syscall
			jmp loop
		
	end:
	mov rax, 0x3c
	xor rdi, rdi
	syscall
