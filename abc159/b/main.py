S = input()

begin = S[0 : (len(S) - 1) // 2]
end = S[(len(S) + 1) // 2 : len(S)]

result = "No"

if begin == end[::-1]:
    if begin == begin[::-1] and end == end[::-1]:
        result = "Yes"

print(result)
