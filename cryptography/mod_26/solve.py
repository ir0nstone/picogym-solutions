from string import ascii_lowercase, ascii_uppercase

enc_flag = r"cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"

flag = ""

for c in enc_flag:
    if c in ascii_lowercase:
        flag += ascii_lowercase[(ascii_lowercase.index(c) + 13) % 26]
    elif c in ascii_uppercase:
        flag += ascii_uppercase[(ascii_uppercase.index(c) + 13) % 26]
    else:
        flag += c

print(flag)

# picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}
