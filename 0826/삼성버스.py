import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(T):
    N = int(input()) # 버스노선 갯수
    bus_range = []
    lists = []
    for i in range(N):
        bus_range.append(list(map(int, input().split()))) # aj <= i번째 버스 <=bj를 다닐 수 있음

    P = int(input())
    for j in range(P):
        cnt = 0
        C = int(input())
        for x in range(N):
            if C >= bus_range[x][0] and C <= bus_range[x][1]:
                cnt += 1
        lists.append(cnt)
    print(f"#{tc+1} {' '.join(list(map(str,lists)))}")
