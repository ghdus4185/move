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
#     answer_list.reverse()
#     # print(answer_list)
#     for i in range(len(answer_list)):
#         ok = True
#         word = str(answer_list[i])
#         for k in range(len(word) - 1):
#             if int(word[k]) > int(word[k + 1]):
#                 ok = False
#                 break
#         if ok:
#             A = answer_list[i]
#             break
#
#     if i == len(answer_list) - 1:
#         result.append(-1)
#     else:
#         result.append(A)
#
# for i in range(T):
#     print("#{} {}".format(i + 1, result[i]))