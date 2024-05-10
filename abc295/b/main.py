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

    for dx in range(-distance, distance + 1):
        for dy in range(-distance, distance + 1):
            if abs(dx) + abs(dy) <= distance:
                nx = x + dx
                ny = y + dy

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

