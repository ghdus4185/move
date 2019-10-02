def danjo(num):
    if len(num) == 1:
        return int(num)
    for i in range(1, len(num)):
        if int(num[i]) - int(num[i - 1]) < 0:
            return -1
    return int(num)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    combine = []
    for i in range(N):
        for j in range(i+1, N):
            a = str(num_list[i] * num_list[j])
            dan = danjo(a)
            combine.append(dan)
    combine = sorted(combine)
    res = combine[-1]
    print('#{} {}'.format(tc, res))

#승연
# result = []
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     A = 0
#     answer_list = []
#     for i in range(N):
#         for j in range(i + 1, N):
#             answer = nums[i] * nums[j]
#             answer_list.append(answer)
#
#     answer_list.sort()
#     answer_list.reverse() # 큰게 word 단조증가수이면 끝
#     # print(answer_list)
#     for i in range(len(answer_list)):
#         ok = True
#         word = str(answer_list[i])
#         for k in range(len(word) - 1):
#             if int(word[k]) > int(word[k + 1]):
#                 ok = False
#                 break # 단조가 아님
#         if ok: # 다돌았는데도 false가 안나오면 단조라는 말이니까 넣고 종료
#             A = answer_list[i]
#             break
#
#     if i == len(answer_list) - 1: # for문 맨 마지막까지 갔는데 단조가 없으면 종료
#         result.append(-1) # 맨 마지막이 단조면
#     else:
#         result.append(A)
#
# for i in range(T):
#     print("#{} {}".format(i + 1, result[i]))