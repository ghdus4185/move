for test_case in range(1,11):
    dumpnum = int(input())
    height = list(map(int,input().split()))
    for dump in range(dumpnum):
        maxid = height.index(max(height))
        minid = height.index(min(height))
        height[maxid] -= 1
        height[minid] += 1
    print(f'#{test_case} {max(height)-min(height)}')