X, H, M = map(int, input().split())

H *= 60
now = H + M
next = H  + X

time = next - now

if time < 0:
    time += 60

print(time)