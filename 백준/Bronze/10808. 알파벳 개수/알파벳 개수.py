d = {k : 0 for k in range(ord('a'), ord('z') + 1)}
s = input()
for i in s:
    d[ord(i)] += 1
print(*list(d.values()), sep = ' ')