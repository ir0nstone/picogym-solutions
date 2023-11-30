from string import ascii_uppercase, ascii_lowercase

enc = 'krxlXGU{zgyzhs_xizxp_8z0uvwwx}'
dec = ''

for c in enc:
    if c in ascii_uppercase:
        dec += ascii_uppercase[-(ascii_uppercase.index(c)+1)]       # so index 0 transposes to -1, index 1 to -2, etc
    elif c in ascii_lowercase:
        dec += ascii_lowercase[-(ascii_lowercase.index(c)+1)]
    else:
        dec += c

print(dec)

# picoCTF{atbash_crack_8a0feddc}
