from pwn import *
p = process("./ret2the-unknown",env = {"LD_PRELOAD" : "./ld-2.28.so", "./libc-2.28.so"})
gdb.attach("ret2the-unknown")
p.sendline("A")
p.interactive()
