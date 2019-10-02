# shuffle-o-matic
# bfs, dfs 최소 탐색하는 법을 알고 실행

T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    left = cards[:N//2+1]
    right = cards[N//2+1:]
    x = 1
    cnt = 0
    #셔플
    while cnt <= 5:
        # 오름차순 또는 내림차순이면 break
        if cards == [i for i in range(1, N+1)]:
            break
        elif cards == [i for i in range(N, 0, -1)]:
            break

        if x == 1:
            right.insert(0, left.pop(-1))
            left.append(right.pop(0))
            cards = left + right
            cnt += 1
        elif x == 2:
            a = left.pop(-1)
            b = left.pop(-1)
            c = right.pop(0)
            d = right.pop(0)
            right.insert(0, a)
            right.insert(0, d)
            left.append(c)
            left.append(b)
            cards = left + right
            cnt += 1
        elif x == 3:
            a = left.pop(-1)
            b = left.pop(-1)
            b = left.pop(-1)
            c = right.pop(0)
            d = right.pop(0)
            d = right.pop(0)
            cnt += 1
        elif x == 4:
            pass
            cnt += 1
        elif x == 5:
            pass
            cnt += 1

    if cnt > 5:
        cnt = -1
        print('#{} {}'.format(tc+1, cnt))
    else:
        print('#{} {}'.format(tc+1, cnt))