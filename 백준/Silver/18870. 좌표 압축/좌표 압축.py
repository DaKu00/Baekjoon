l = []

n = input()

n_l = list(map(int, input().split()))

s_l = list(set(n_l))
s_l.sort()
s_d = {value : index for index, value in enumerate(s_l)}
for i in n_l:
    print(s_d[i], end = ' ')

    