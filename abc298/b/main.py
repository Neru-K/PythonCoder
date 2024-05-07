def rotate_grid(list2d, N):
    rotated_list = None

    if isinstance(list2d[0][0],int):
        rotated_list = [[0] * N for _ in range(N)]
    elif isinstance(list2d[0][0],str):
        rotated_list = [[""] * N for _ in range(N)]
    else:
        print('要素の型が数値型でも文字列型でもないです')
        exit()
    
    for i in range(N):
        for j in range(N):
            rotated_list[j][N - 1 - i] = list2d[i][j]

    return rotated_list

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for _ in range(4):

        A = rotate_grid(A, N)
        
        for i in range(N):
            flag = False
            for j in range(N):
                if A[i][j] == 1 and B[i][j] == 0:
                    count += 1
                    flag = True
                    break

            if flag:
                break

    if count < 4:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()