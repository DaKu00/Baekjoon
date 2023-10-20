import sys
n = int(input())

num_list = {key : 0 for key in map(int, input().split())}
# num_list = list(map(int, sys.stdin.readline().split()))
m = int(input())

mum_list = list(map(int, sys.stdin.readline().split()))

result = []

for i in mum_list:
    try:
        num_list[i] += 1
    except:
        result.append(0)
    else:
        result.append(1)
    

print(*result, sep = '\n')