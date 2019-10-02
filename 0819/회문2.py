import sys
sys.stdin = open('input.txt','r')

for test_case in range(10):
    n = input()
    matrix = []
    result_list = []
    for i in range(100):
        matrix.append(input())
    matrix_zip = list(zip(*matrix))

    for i in range(100):
        for j in range(100):
            #가로검사
            if matrix[i][j:100+j] == matrix[i][j:100+j][::-1]:
                a = len(matrix[i][j:100+j])
                result_list.append(a)
            #세로검사
            elif matrix_zip[i][j:100+j] == matrix_zip[i][j:100+j][::-1]:
                b = len(matrix[i][j:100+j])
                result_list.append(b)
    maxresult = max(result_list)
    print(f'#{test_case+1} {maxresult}')