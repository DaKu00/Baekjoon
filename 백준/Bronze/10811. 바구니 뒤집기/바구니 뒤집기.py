n, m = map(int, input().split())
n_list = [num for num in range(1, n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    r_list = n_list[a - 1 : b]
    r_list.reverse()
    n_list = n_list[: a - 1] + r_list + n_list[b : ]
    
print(*n_list, sep = ' ')



