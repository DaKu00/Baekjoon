num_l = []

for j in range(2, 10):
    if j == 7 or j == 9:
        for i in range(4):
            num_l.append(j)
    else:
        for i in range(3):
            num_l.append(j)
        
str_s = input()

sum_n = len(str_s)

for s in str_s:
    sum_n += num_l[ord(s) - 65]
print(sum_n)