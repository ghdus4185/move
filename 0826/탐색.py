# 1) 오른쪽부터 시계방향으로 0, 1, 2, 3 방향이라 정함
# 2) 0번 방향으로 설정, 맨 왼쪽 윗칸을 탐색 위치로 정함
# 3) 맨 위쪽 윗칸부터 설정 방향으로 탐색시작
# 4) 현재 방향의 마지막 칸이거나, 다음 칸에 값이 있으면 다음 방향으로 변경
# 5) N*N칸 이내면 3) 반복
# 6) 더이상 남은 칸이 없으면 종료
# 재귀로 할지 반복으로 할지 선택


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dir = 0
    i = 0
    j= 0
    k = 1 # 칸에 기록할 값

    while k <= 9: # 아직 N*N칸 이내면
        arr[i][j] = k # 현재칸에 값을 쓰고
        k += 1
        # 다음칸을 결정, 배열을 벗어나지 않고 비어있어야 함
        #현재 방향으로 다음칸을 계산할 지, 다음 방향으로 계산할 지 결정
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni >= 0 and ni < N and nj >= 0 and nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir+1)%4
            i += di[dir]
            j += dj[dir]
    print('#{}'.format(tc+1))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end='')
        print()