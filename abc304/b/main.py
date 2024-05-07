N = int(input())

if N < 1000 :
    print(N)
elif N <= 10_000 - 1 :
    print(N - N % 10)
elif N <= 100_000 - 1 :
    print(N - N % 100)
elif N <= 1_000_000 - 1 :
    print(N - N % 1000)
elif N <= 10_000_000 - 1 :
    print(N - N % 10000)
elif N <= 100_000_000 - 1 :
    print(N - N % 100000)
elif N <= 1_000_000_000 - 1 :
    print(N - N % 1000000)