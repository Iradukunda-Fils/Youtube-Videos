; =============================
; Hello World in x86 Assembly
; Target OS  : Linux (32-bit)
; Assembler  : NASM (Netwide Assembler)
; Run using  : int 0x80 syscall interface
; =============================


section .data
    msg db "Hello, World!", 0xA    ; Define a string message, ending with newline
    len equ $ - msg                ; Calculate length of the string at compile time

section .text
    global _start                  ; Declare entry point for the linker

_start:
    ; ---------------------------------
    ; Linux syscall: sys_write
    ; syscall number: 4
    ; signature:     write(fd, buf, count)
    ; ---------------------------------

    mov eax, 4       ; syscall number for sys_write
    mov ebx, 1       ; file descriptor 1 = STDOUT
    mov ecx, msg     ; pointer to the message string
    mov edx, len     ; length of the message
    int 0x80         ; call kernel interrupt to write

    ; ---------------------------------
    ; Linux syscall: sys_exit
    ; syscall number: 1
    ; signature:     exit(status) 
    ; ---------------------------------

    mov eax, 1       ; syscall number for sys_exit
    xor ebx, ebx     ; exit code 0 (zero out ebx)
    int 0x80         ; call kernel interrupt to exit

