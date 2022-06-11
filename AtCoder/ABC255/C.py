x, a, d, n = map(int, input().split())
n -= 1
smin = min(a, a+d*n)
smax = max(a, a+d*n)
if x <= smin:
    print(abs(smin - x))
elif x >= smax:
    print(abs(x - smax))
else:
    x -= a
    d = abs(d)
    mod = x % d
    print(min(mod, abs(d - mod)))