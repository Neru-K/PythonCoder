S, A, B, X = map(int, input().split())

sec = 0
distance = 0

while sec < X:
    temp_sec = 0
    if sec + A > X:
        temp_sec = X - sec
    else:
        temp_sec = A
    distance += S * temp_sec
    sec += temp_sec

    if sec >= X:
        break

    sec += B

print(distance)
