# 원자 소멸 시뮬레이션 2019
T = int(input())
for tc in range(T):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    energy = 0
    plate = [[0]*1000 for _ in range(1000)]

    #원자의 움직임
    for i in range():
        for j in range():

    # if 1: # 만약에 부딪히면 energy += atom1(e) atom2(e)
    #     pass

    # print('#{} {}'.format(tc+1, energy))