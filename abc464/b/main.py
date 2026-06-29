H, W = map(int, input().split())

image = []
converted = []
converted2 = []
converted3 = []
converted4 = []

for row in range(H):
    r = input()
    image.append(r)

enable_delete = True

for line in image:
    if line.count("#") > 0:
        enable_delete = False

    if not enable_delete:
        converted.append(line)

image2 = [col[::-1] for col in zip(*converted)]

enable_delete2 = True

for line2 in image2:
    if line2.count("#") > 0:
        enable_delete2 = False

    if not enable_delete2:
        converted2.append(line2)

image3 = [col[::-1] for col in zip(*converted2)]

enable_delete3 = True

for line3 in image3:
    if line3.count("#") > 0:
        enable_delete3 = False

    if not enable_delete3:
        converted3.append(line3)

image4 = [col[::-1] for col in zip(*converted3)]

enable_delete4 = True

for line4 in image4:
    if line4.count("#") > 0:
        enable_delete4 = False

    if not enable_delete4:
        converted4.append(line4)

image5 = [col[::-1] for col in zip(*converted4)]

for line5 in image5:
    print(*line5, sep="")
