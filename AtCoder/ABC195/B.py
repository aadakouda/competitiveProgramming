a, b, w = map(int, input().split())
w *= 1000
ma = w // a
mi = w // b if w % b == 0 else w // b + 1
if ma < mi:
    print('UNSATISFIABLE')
else:
    print(mi, ma)