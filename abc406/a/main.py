A, B, C, D = map(int, input().split())

accepted = (A * 60) + B
submitted = (C * 60) + D

if accepted > submitted:
  print("Yes")
else:
  print("No")