T = int(input())
for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    combine = []
    maxV = 0
    # 조합 찾기
    for i in range(N-1):
        for j in range(i+1, N):
            a = num_list[i] * num_list[j]
            combine.append(a)
    check = []
    upnum = []
    # 단조 수를 찾음
    for i in range(len(combine)):
        for j in range(len(str(i))):
            for x in range(len(str(i))-1-j):
                if combine[i][j] < combine[i][j+1+x]:
                    pass
                else:
                    break
    if j == len(str(i)) -1:
        if maxV < combine[i]:
            maxV = combine[i]
    # 단조 증가하는 수 중 가장 큰 수 출력
    print('#{} {}'.format(tc+1, maxV))