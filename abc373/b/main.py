S = list(input())
data = [[S[i],i] for i in range(26)]

sorted_data = sorted(data, key=lambda x:x[0])

distance = 0

for i in range(1,len(sorted_data)):
    distance += abs(sorted_data[i][1] - sorted_data[i - 1][1])

print(distance)