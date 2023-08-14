t = int(input())


def wierdFunction(x):
    return x**2 + 2 * x + 3


print(
    wierdFunction(wierdFunction(wierdFunction(t) + t) + wierdFunction(wierdFunction(t)))
)
