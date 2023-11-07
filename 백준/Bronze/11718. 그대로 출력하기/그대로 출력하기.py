w_list = []
for _ in range(100):
    try:
        w = input()
        w_list.append(w.strip())
    except:
        break
    # if len(w.strip()) != 0:
        
    # else:
    #     break
for j in w_list:
    print(j)