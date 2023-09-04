#
# Intro to pwntools
#
# Requirements:
#
# pwntools
#
# Installation:
#
# pip install pwntools
#
# More information at https://docs.pwntools.com

from pwn import *

print(cyclic(50))

# Results: 
# b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama'

print(cyclic_find("laaa"))

# In the above command it found the string "laaa" at position 44
# Results:
# b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama'
# 44

print("- - - - -")

print(shellcraft.sh())

# Results:
#    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
#    /* push b'/bin///sh\x00' */
#    push 0x68
#    push 0x732f2f2f
#    push 0x6e69622f
#    mov ebx, esp
#    /* push argument array ['sh\x00'] */
#    /* push 'sh\x00\x00' */
#    push 0x1010101
#    xor dword ptr [esp], 0x1016972
#    xor ecx, ecx
#    push ecx /* null terminate */
#    push 4
#    pop ecx
#    add ecx, esp
#    push ecx /* 'sh\x00' */
#    mov ecx, esp
#    xor edx, edx
#    /* call execve() */
#    push SYS_execve /* 0xb */
#    pop eax
#    int 0x80

print("- - - - -")

print(hexdump(asm(shellcraft.sh())))

# Results:
# 00000000  6a 68 68 2f  2f 2f 73 68  2f 62 69 6e  89 e3 68 01  │jhh/│//sh│/bin│··h·│
# 00000010  01 01 01 81  34 24 72 69  01 01 31 c9  51 6a 04 59  │····│4$ri│··1·│Qj·Y│
# 00000020  01 e1 51 89  e1 31 d2 6a  0b 58 cd 80               │··Q·│·1·j│·X··│
# 0000002c

print("- - - - -")

p = process("/bin/sh")
p.sendline("echo hello;")
# p.interactive()

# Commented out p.interactive() to prevent this from running in while testing other parameters.

# Results:
# [+] Starting local process '/bin/sh': pid 13374
# /home/kali/Intro-to-pwntools.py:56: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   p.sendline("echo hello;")
# [*] Switching to interactive mode
# hello
# $ <command window>
#
# Used Control + C to exit the command window
# Was able to execute commands from the window (ls | touch)

print("- - - - -")

# Commenting Out ** Start **
# r = remote("127.0.0.1", 1234)
# r.sendline("hello!")
# r.interactive()
# r.close()
# Commenting Out ** End **

# In a 2nd command window I ran a netcat command to listen on the local port 1234
# nc-lp 1234
#
# Results in 2nd command window
# hello!
# interactive session

# Additional results:
#
# [+] Opening connection to 127.0.0.1 on port 1234: Done
# /home/kali/Intro-to-pwntools.py:75: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   r.sendline("hello!")
# [*] Switching to interactive mode
# $ interactive session
# $ 
# [*] Interrupted
# [*] Closed connection to 127.0.0.1 port 1234
# [*] Stopped process '/bin/sh' (pid 17789)

print("- - - - -")

print(p32(0x13371337))
print(hex(u32(p32(0x13371337))))
l = ELF('/bin/bash')
print(hex(l.address))
print(hex(l.entry))
print(hex(l.got['write']))
print(hex(l.plt['write']))

for address in l.search(b'/bin/sh\x00'):
	print(hex(address))

# Example Results:
# b'7\x137\x13'
# 0x13371337
# [*] '/bin/bash'
#     Arch:     amd64-64-little
#     RELRO:    Full RELRO
#     Stack:    Canary found
#     NX:       NX enabled
#     PIE:      PIE enabled
#     FORTIFY:  Enabled
# 0x0
# 0x31750
# 0x12b930
# 0x2f290
# 0x31e32
# 0x31ed1

print("- - - - -")

print(next(l.search(asm('jmp esp'))))
print(hex(next(l.search(asm('jmp esp')))))

# Results:
# 245250
# 0x3be02

print("- - - - -")

r = ROP(l)
print(r.rbx)

# Results:
# [*] Loading gadgets for '/bin/bash'
# Gadget(0x31d58, ['pop rbx', 'ret'], ['rbx'], 0x8)

print("- - - - -")

print(xor("A","B"))
print(xor(xor("A","B"),"A"))

# Base 64 Encoding & Decoding
print(b64e(b"test"))
print(b64d("dGVzdA=="))

# MD5 / SHA1 Hash

print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))

# Printing / UnPrinting the bits that make the letter a
print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))

# Results of the last few commands:
# /home/kali/.local/lib/python3.11/site-packages/pwnlib/util/fiddling.py:327: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
#   strs = [packing.flat(s, word_size = 8, sign = False, endianness = 'little') for s in args]
# b'\x03'
# b'B'
# dGVzdA==
# b'test'
# 5d41402abc4b2a76b9719d911017c592
# aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
# [0, 1, 1, 0, 0, 0, 0, 1]
# b'a'
