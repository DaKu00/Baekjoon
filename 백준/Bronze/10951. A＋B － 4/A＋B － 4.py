n_list = []
while True:
    try:
        a, b = map(int, input().split())
        n_list.append(a + b)
    except:
       break
print(*n_list, sep = '\n')