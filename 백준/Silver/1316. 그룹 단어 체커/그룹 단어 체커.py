word_list = []
    
for i in range(int(input())):
    word_list.append(input())


check_num = 0
for w in word_list:
    w_d = {}
    n_n = None
    for s in w:
        
        if s in w_d.keys() and s != n_n:
            break
        else:
            w_d[s] = 0
            n_n = s
    else:
        check_num += 1
print(check_num)