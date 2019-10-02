#항구에 들어오는 배
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    happy = [int(input()) for _ in range(N)]

    for i in range(len(happy)):
        happy[i] -= 1
    happy.reverse()

    res = 0
    for i in range(len(happy)-2):
        for j in range(1, len(happy)-2-i):
            if happy[i] % happy[i+j] == 0:
                res = 1
                break
        if res == 1:
            happy.remove(happy[i])
    print(happy)
