def f(i, N, K, s ):
    global cnt
    global bit
    if i == N: # bit의 모든칸이 결정됨
        for j in range(N):
            if bit[j] ==1: # 0~N-1은 원 집합의 원소 1~N을 가리킴
                if bit[j] == 1: # j+1이 부분집합에 포함된 경우
                    s += j+1
            if s == K:
                cnt += 1
        else:
            f(i+1, N, K, s) # i번이 가리키는 값은 부분집합에 포함하지 않음

            f(i+1, N, K, s + i + 1) # i번이 가리키는 값을 부분집합에 포함
N = 10 # 1부터 N까지 집합의 원소
K = 10 # 부분집합의 합
cnt = 0
bit = [0] * N
print(f(1, N, K))