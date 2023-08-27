N = int(input())
W = list(map(int, input().split()))

sum = sum(W)
average = sum / N
more = 0
less = 0
equal = 0

print(average)

for w in W:
    if average == w:
        equal = w
    if average > w:
        more += w
    else:
        less += w

result = 0

print(abs(more - (less + equal)))
print(abs((more + equal) - less))
