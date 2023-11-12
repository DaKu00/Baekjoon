na_d = {}

for i in range(10):
  n = int(input())

  na = n % 42

  if na in na_d:
    na_d[f'{na}'] += 1
  else:
    na_d[f'{na}'] = 1


print(len(na_d))
