from pwn import *

KEY_LEN = 50000

p = remote("mercury.picoctf.net", 11188)

p.recvuntil(b"flag!\n")
enc_flag = p.recvline().strip()
enc_flag_len = len(enc_flag) // 2       # 32

to_enc = b"A" * (KEY_LEN-enc_flag_len)
p.sendlineafter(b"encrypt? ", to_enc)

# now enc flag...
p.sendlineafter(b"encrypt? ", bytes.fromhex(enc_flag.decode()))
p.recvline()
flag = p.recvline().strip()

print(b"picoCTF{" + bytes.fromhex(flag.decode()) + b"}")

# picoCTF{7904ff830f1c5bba8f763707247ba3e1}