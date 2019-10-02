T = int(input())
for tc in range(T):
    X=list(input())
    lists = []
    for i in X:
        if i not in lists:
            lists.append(i)
    print('#{} {}'.format(tc+1, len(lists)))