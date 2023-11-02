n = int(input())
answer_list = None
for i in range(n):
    second_line = input()
    if not answer_list:
        answer_list = list(second_line)
    else:    
        for idx in range(len(answer_list)):
            if answer_list[idx] != list(second_line)[idx]:
                answer_list[idx] = '?'
print(*answer_list, sep = '')
			