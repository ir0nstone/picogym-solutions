from string import ascii_lowercase, ascii_uppercase

enc_flag = 'cvpbPGS{P7e1S_54I35_71Z3}'

for shift in range(26):
    flag = ''

    for c in enc_flag:
        if c in ascii_lowercase:
            flag += ascii_lowercase[(ascii_lowercase.index(c) + shift) % 26]
        elif c in ascii_uppercase:
            flag += ascii_uppercase[(ascii_uppercase.index(c) + shift) % 26]
        else:
            flag += c

    print(flag)

# picoCTF{C7r1F_54V35_71M3}
