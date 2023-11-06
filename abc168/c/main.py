import math

A, B, H, M = map(int, input().split())

angleH = (H % 12) * 30 + M * 0.5

angleM = M * 6

angle = abs(angleH - angleM)

if angle > 180:
    angle = 360 - angle

angle_rad = math.radians(angle)

C2 = A**2 + B**2 - 2 * A * B * math.cos(angle_rad)

C = math.sqrt(C2)

print(C)
