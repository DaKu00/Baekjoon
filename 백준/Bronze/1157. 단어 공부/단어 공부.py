st = input()

so_st = st.upper()

alph  = [0] * 26

for w in so_st:
    alph[ord(w) - 65] += 1

count = 26 - alph.count(0)
w_list = list(set(alph))

if alph.count(max(w_list)) > 1:
    print('?')
else:
    print(chr(alph.index(max(alph)) + 65))
