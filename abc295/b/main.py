#N = int(input())
#S = input() 
#S = float(input())
#list_s = input().split()
#A, B, C = input().split()
R, C = map(int, input().split())
#list_s = list(map(int, input().split()))
#N, M = map(int, input().split())
B = [list(input()) for _ in range(R)]

def manhattan(x, y, distance):

    for d in range(1,distance+1):

        dx = [0,d-1,d,d-1,0,1-d,-d,1-d]
        dy = [-d,1-d,0,d-1,d,d-1,0,1-d]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == x and ny == y:
                continue

            if 0 <= nx < C and 0 <= ny < R and B[ny][nx] == "#":
                B[ny][nx] = "."

def main():
    for r in range(R):
        for c in range(C):
            if B[r][c] != "#" and B[r][c] != ".":
                
                manhattan(c,r,int(B[r][c]))
                B[r][c] = "."

    for i in range(R):
        print("".join(B[i]))

if __name__ == '__main__':
    main()

