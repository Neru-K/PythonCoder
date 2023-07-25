n = int(input())
array = [1]

print("1")

for i in range(n - 1):
    array1 = array + [0]
    array2 = [0] + array
    array = [a + b for a, b in zip(array1, array2)]

    str_list = [str(num) for num in array]
    print(" ".join(str_list))
