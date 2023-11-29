from string import ascii_lowercase

ciphertext = 'ynkooejcpdanqxeykjrbdofgkq'

for shift in range(26):
    new_c = ''

    for c in ciphertext:
        new_c += ascii_lowercase[(ascii_lowercase.index(c) + shift) % 26]

    print(new_c)

# picoCTF{crossingtherubiconvfhsjkou}
