alph = [-1] * 26
s_list = input()

for idx, s in enumerate(s_list):
    if alph[ord(s) - 97] == -1:
        alph[ord(s) - 97] = idx
print(*alph)