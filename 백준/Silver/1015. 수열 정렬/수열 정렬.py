n = int(input())
n_list = list(map(int, input().split()))

sorted_list = sorted([(value, idx) for idx, value in enumerate(n_list)])

answer = [0] * n  # 결과를 담을 리스트를 초기화합니다.
for idx, (_, original_idx) in enumerate(sorted_list):
    answer[original_idx] = idx

print(*answer)