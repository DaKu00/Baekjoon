a,b,c = map(int,input().split())

if a==b:
    if b==c:
        print(10000+a*1000)
    elif b!=c:
        print(1000+a*100)
elif a==c:
    if b!=c:
        print(1000+a*100)
elif b==c:
    if a!=c:
        print(1000+b*100)
elif a>b:
    if a>c:
        print(a*100)
    else:
        print(c*100)
elif b>c:
    if a>b:
        print(a*100)
    else:
        print(b*100)
else:
    print(c*100)