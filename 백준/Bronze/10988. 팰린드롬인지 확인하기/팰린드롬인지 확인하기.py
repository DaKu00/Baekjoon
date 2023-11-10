st = input()

re_st = list(st)
re_st.reverse()
if st == ''.join(re_st):
    print(1)
else:
    print(0)