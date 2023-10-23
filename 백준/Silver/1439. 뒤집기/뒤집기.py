s = input()
num = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        num += 1

if num % 2 == 0:
    print(int(num / 2))
else:
    print(int((num + 1) / 2))
        


