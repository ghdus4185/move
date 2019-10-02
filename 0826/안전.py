import sys
sys.stdin = open('input.txt','r')

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
print(matrix)