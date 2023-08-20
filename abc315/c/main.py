N = int(input())

FS = [list(map(int, input().split)) for _ in range(N)]

sorted = sorted(FS, key=lambda x: x[1])
