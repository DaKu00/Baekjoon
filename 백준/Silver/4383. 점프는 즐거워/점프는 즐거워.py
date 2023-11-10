while True:
    try:
        n_list = list(map(int, input().split()))
        n_list = n_list[1:]
        su_list = []
        for idx in range(len(n_list) - 1):
            su_list.append(abs(n_list[idx] - n_list[idx + 1]))
        su_list.sort()
        if len(n_list) == 1:
                print('Jolly')
        elif su_list == [i for i in range(1, len(su_list) + 1)]:
            print('Jolly')
        else:
            print('Not jolly')
    except:
        break
