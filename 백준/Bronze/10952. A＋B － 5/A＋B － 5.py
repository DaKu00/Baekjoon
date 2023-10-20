num_list = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    num_list.append(a + b)

print(*num_list, sep = '\n')