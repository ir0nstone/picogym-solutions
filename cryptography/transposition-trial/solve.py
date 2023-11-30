message = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4'

trigrams = [message[x:x+3] for x in range(0, len(message), 3)]

dec = ''

for t in trigrams:
    dec += t[2] + t[0] + t[1]

print(dec)

# The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
