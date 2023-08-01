h, w = map(int, input().split())

g = [input() for _ in range(h)]

pairs = [(0, 0)]


def is_duplicated(pairs):
    unique_pairs = list(set(pairs))

    if len(pairs) != len(unique_pairs):
        return True
    else:
        return False
