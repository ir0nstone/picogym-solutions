from Crypto.Util.number import long_to_bytes
from pwn import *

conn = remote('jupiter.challenges.picoctf.org', 18821)

p, q, n, d, e, phi, plaintext, ciphertext = 0, 0, 0, 0, 0, 0, 0, 0


def get_answer(to_calc):
    global p, q, n, d, e, phi, plaintext, ciphertext

    for i in range(5):
        if p and q:
            n = p*q
            phi = (p-1)*(q-1)
        if p and n:
            q = n // p
        if q and n:
            p = n // q
        if phi and e:
            d = pow(e, -1, phi)
        if phi and d:
            e = pow(d, -1, phi)
        if plaintext and e and n:
            ciphertext = pow(plaintext, e, n)
        if ciphertext and d and n:
            plaintext = pow(ciphertext, d, n)

    return globals()[to_calc] != 0, globals()[to_calc]


conn.recvline()

while True:
    conn.recvlines(3)

    # flag is given
    if b'last plaintext' in conn.recvline():
        break

    p, q, n, d, e, phi, plaintext, ciphertext = 0, 0, 0, 0, 0, 0, 0, 0

    variables = conn.recvuntil(b'####\n').split(b'\n')[:-1]
    print(variables)

    for v in variables:
        var, val = v.split(b' : ')
        var = var.decode().replace('totient(n)', 'phi')
        val = int(val)

        print(var, val)
        globals()[var] = val

    to_calc = conn.recvline().decode()
    to_calc = to_calc.replace('totient(n)', 'phi')

    print(to_calc)
    can_calc, ans = get_answer(to_calc)
    print()

    if ans:
        conn.sendlineafter(b'(Y/N):', b'Y')
        conn.sendlineafter(b': ', str(ans).encode())
    else:
        conn.sendlineafter(b'(Y/N):', b'N')


# decode
flag = long_to_bytes(plaintext)
print(flag.decode())
