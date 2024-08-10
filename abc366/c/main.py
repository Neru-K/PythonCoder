Q = int(input())

bag = [0] * (10 ** 6 + 1)
set_bag = set()

for i in range(Q):
    q = input()

    if q[0] == '1':
        _, n = map(int,q.split())
        bag[n-1] += 1
        set_bag.add(n)
    elif q[0] == '2':
        _, n = map(int,q.split())
        bag[n-1] -= 1
        if bag[n-1] == 0:
            set_bag.remove(n)
    else:
        
        print(len(set_bag))