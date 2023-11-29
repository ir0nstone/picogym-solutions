from string import ascii_lowercase, ascii_uppercase

enc_flag = r"cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

flag = ""

for c in enc_flag:
    if c in ascii_lowercase:
        flag += ascii_lowercase[(ascii_lowercase.index(c) + 13) % 26]
    elif c in ascii_uppercase:
        flag += ascii_uppercase[(ascii_uppercase.index(c) + 13) % 26]
    else:
        flag += c

print(flag)

# picoCTF{not_too_bad_of_a_problem}
