N, D = map(int, input().split())

enableWatchNum = D * 2 + 1

if N % enableWatchNum == 0:
    print(N // enableWatchNum)
else:
    print(N // enableWatchNum + 1)
