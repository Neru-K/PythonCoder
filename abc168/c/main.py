import math

A, B, H, M = map(int, input().split())

angH = (60 * H + M) / 720 * 360
angM = M / 60 * 360
angTheta = angH - angM
angTheta = 360 - angTheta if angTheta < 0 else angTheta

thetaRad = math.radians(angTheta)
cosTheta = math.cos(thetaRad)

lenCSquared = ((A ** 2) + (B ** 2)) - (2 * A * B * cosTheta)

print(lenCSquared ** 0.5)