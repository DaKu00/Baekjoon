n, j = input().split()

sum_n = 0

n = list(n)
n.reverse()

for i, v in enumerate(n):
    if not v.isdigit():
        a = (ord(v) - 55) * (int(j) ** i)
    else:
        a = int(v) * int(j) ** i
    sum_n += a

print(sum_n)