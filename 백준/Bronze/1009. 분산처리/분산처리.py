o = [1]
a = [2, 4, 8, 6]
b = [3, 9, 7, 1]
c = [4, 6]
ff = [5]
ss = [6]
d = [7, 9, 3, 1]
e = [8, 4, 2, 6]
f = [9, 1]
a_list = [o, a, b, c, ff, ss, d, e, f]
n = int(input())
n_list = []
for i in range(n):
    ud, up = map(int, input().split())
    
    if ud % 10 == 0:
        n_list.append(10)
        continue
    
    n_list.append(a_list[(ud % 10) - 1][(up%len(a_list[(ud % 10) - 1])) - 1])
    
print(*n_list, sep = '\n')
