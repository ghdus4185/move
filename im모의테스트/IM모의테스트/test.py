import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)] # 0으로 칠해진 영역
    maxV = 0

    for x in range(K): # 칠하기
        a, b, c, d, e = map(int, input().split())
        #해당 영역에 더 큰 명도로 칠해진 칸이 있는지 확인
        result = 0
        for row in range(a, c+1):
            for col in range(b, d+1):
                if board[row][col] > e:
                    result = 1
        #칠할 수 있으면 칠함
        if result ==0: #더 큰 명도가 없었으면
            for row in range(a, c+1):
                for col in range(b,d+1):
                    board[row][col] = e
    # 명도 개수 기록
    bright = [0]*11 # 0번~10번
    # 모든 영역을 돌면서 해당 숫자를 리스트에 cnt +1
    for i in range(N):
        for j in range(M):
            bright[board[i][j]] += 1
    print('#{} {}'.format(tc+1, max(bright)))