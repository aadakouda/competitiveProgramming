n = input()
keta = [int(i) for i in n]
r = sum(keta) % 3
if r == 0:
    mi = 0
else:
    r1 = 0
    r2 = 0
    for i in range(len(keta)):
        if keta[i] % 3 == 1:
            r1 += 1
        elif keta[i] % 3 == 2:
            r2 += 1
    if r == 1:
        if r1 > 0:
            mi = 1
        elif r2 >= 2:
            mi = 2
    elif r == 2:
        if r2 > 0:
            mi = 1
        elif r1 >= 2:
            mi = 2
print(mi if len(keta)-mi > 0 else -1)