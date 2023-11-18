alphabet = [0] * 26

N = int(input())
S = input()


def char_to_num(char):
    return ord(char) - ord("a")


count = 1

for i in range(N):
    if i != 0 and S[i - 1] == S[i]:
        count += 1
    elif S[i - 1] != S[i]:
        count = 1

    if alphabet[char_to_num(S[i])] < count:
        alphabet[char_to_num(S[i])] += 1

print(sum(alphabet))
