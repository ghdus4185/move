import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split()) # N명, M초에 K개씩 만듬
    nums = list(map(int, input().split())) # 손님 도착 시간
    a = sorted(nums)

    second = 0
    bread = 0
    res = 0
    for i in range(a[-1]):
        # 손님도착시간이 붕어빵 만들시간 보다 작으면 종료
        if nums[0] < M:
            res = 1
            break
        if second > 0 and second % M == 0:
            bread += K
        for j in range(len(a)):
            if second == a[j]:
                if bread == 0:
                    res = 1
                    break
                else:
                    bread -= 1
        second += 1

    if res == 1:
        print('#{} Impossible'.format(tc+1))
    else:
        print('#{} Possible'.format(tc+1))