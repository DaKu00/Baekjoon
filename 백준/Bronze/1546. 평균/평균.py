n = int(input())
max_n = 0
n_l = []


num = map(int, input().split())

for nu in num:
  if max_n < nu:
    max_n = nu

  n_l.append(nu)

sum_n = 0
for i in n_l:
  sum_n += i / max_n * 100

print(sum_n / n)
