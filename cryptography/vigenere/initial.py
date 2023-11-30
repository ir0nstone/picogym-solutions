from string import ascii_uppercase, ascii_lowercase

def shift(chr, k):
    # get an integer shift from a letter
    k_int = ascii_lowercase.index(k.lower())

    if chr in ascii_uppercase:
        return ascii_uppercase[(ascii_uppercase.index(chr) - k_int) % 26]
    else:
        return ascii_lowercase[(ascii_lowercase.index(chr) - k_int) % 26]


message = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}'
key = 'CYLAB' * 10

dec = ''

for m, k in zip(message, key):
    if m in ascii_uppercase or m in ascii_lowercase:
        dec += shift(m, k)
    else:
        dec += m

print(dec)
