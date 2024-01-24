N, S, T = map(int, input().split())

if N % 2 ^ S ^ T:
    print("Alice")
else:
    print("Bob")
