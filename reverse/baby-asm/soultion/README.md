# Baby asm

## Write-up 
We are giving a ciphertext and the assembly code responsible for the creation of it.

For better understanding, before checking the source, we must know the values of the syscalls. 

check this : [sycalls](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86_64-64_bit)

We start by writing to the stdout the prompt that has been decalared in the data section.

After that, there is a syscall to read user input and, since the prompt said `which file` we can assume that the user will enter the name of the file, which in our case will probably be `flag.txt`.

Once that is done, the application removes newline if existed then starts reading the content of the file and checking if it hasn't reached the end of the file yet.

```asm
		cmp rax, 0
		je end
```

For each character that the application reads, it will compare (using cmp) it to a value and then send it to a function if the comparison returns true (jle i.e., character less than the value), resulting in the following graph:
- c < 32            => func1
- 32 <= c < 64      => func2
- 64 <= c < 96      => func3 
- 96 <= c < 128     => func4

now let's check the content of the functions. 
func1 : 
```asm
			add al, 64
			jmp func
```
This will only add 64 to the ascii value of the character and the jumps to `func` which will continue the loop.
same behaviour for the other functions. The final graph will look like this: 
- c < 32            => c+=64
- 32 <= c < 64      => c-=32
- 64 <= c < 96      => c+=32 
- 96 <= c < 128     => c-=64

Basically, it split the characters into 4 sets `[i: i+32]` and shuffled the sets. Now we just need to do the reverse operation.

- c < 32            => plain = c+32
- 32 <= c < 64      => plain = c+64
- 64 <= c < 96      => plain = c-64
- 96 <= c < 128     => plain = c-32

## Flag

`shellmates{B4CK_T0_Th3_r0075!!}`