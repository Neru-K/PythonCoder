L, R = map(int, input().split())

def loopKeta(numBegin, numEnd):
  sumNum = 0
  digitNumBegin = len(str(numBegin))
  digitNumEnd = len(str(numEnd))

  for digitMinusOne in range(digitNumBegin - 1, digitNumEnd):
    for i in range(1, 10):
      sumNum += digitMinusOne * i

  return sumNum

print(loopKeta(10, 999))