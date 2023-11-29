import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def unshift(p, k):
    t1 = ord(p) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def b16_decode(enc):
    enc = [enc[x:x + 2] for x in range(0, len(enc), 2)]
    dec = ''

    for pair in enc:
        bin1 = ALPHABET.index(pair[0])
        bin2 = ALPHABET.index(pair[1])
        combined = int(bin(bin1)[2:].zfill(4) + bin(bin2)[2:].zfill(4), 2)
        dec += chr(combined)

    return dec


enc_flag = 'apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna'

for key in ALPHABET:
    shifted_flag = ''

    for i, p in enumerate(enc_flag):
        shifted_flag += unshift(p, key)

    d = b16_decode(shifted_flag)

    print(d)

# et_tu?_23217b54456fb10e908b5e87c6e89156
