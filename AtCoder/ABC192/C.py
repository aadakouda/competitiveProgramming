n, k = map(int, input().split())

def g1(x):
    x_list = sorted(str(x), reverse=True)
    return int(''.join(x_list))

def g2(x):
    x_list = sorted(str(x))
    return int(''.join(x_list))

def f(x):
    return g1(x) - g2(x)

for i in range(k):
    n = f(n)

print(n)
