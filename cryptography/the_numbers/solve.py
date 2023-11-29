from string import ascii_uppercase

numbers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

flag = ""

for n in numbers:
    if str(n) in "{}":
        flag += n
    else:
        flag += ascii_uppercase[n-1]

print(flag)
