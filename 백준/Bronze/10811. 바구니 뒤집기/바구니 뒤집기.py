num, m = map(int, input().split())

n = [f'{i}' for i in range(1, num + 1)]

n_l = []

for k in range(m):
  i, j = map(int, input().split())

  l_l = []

  if i == 1 and j == num:
    l_l = n[:]
    l_l.reverse()
    n = l_l
  elif i == 1:
    l_l = n[:j]
    l_l.reverse()
    n = l_l + n[j:]
  elif j == num:
    l_l = n[i - 1:]
    l_l.reverse()
    n = n[:i - 1] + l_l
  else:
    l_l = n[i - 1 : j]
    l_l.reverse()
    n = n[: i - 1] + l_l + n[j:]

print(' '.join(n))