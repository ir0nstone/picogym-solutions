from string import ascii_uppercase, ascii_lowercase

def shift(chr, k):
    # get an integer shift from a letter
    k_int = ascii_lowercase.index(k.lower())

    if chr in ascii_uppercase:
        return ascii_uppercase[(ascii_uppercase.index(chr) - k_int) % 26]
    else:
        return ascii_lowercase[(ascii_lowercase.index(chr) - k_int) % 26]


message = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}'
key = 'CYLAB'

dec = ''

i = 0
for m in message:
    if m in ascii_uppercase or m in ascii_lowercase:
        dec += shift(m, key[i])
        i = (i+1) % 5
    else:
        dec += m

print(dec)

# picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}
