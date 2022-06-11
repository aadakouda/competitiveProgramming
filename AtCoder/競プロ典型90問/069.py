n, k = map(int, input().split())
d = 10**9 + 7
if k < 3:
    if n <= k:
        print(k)
    else:
        print(0)
elif n == 1:
    print(k)
elif n == 2:
    print(k * (k-1))
else:
    result = k * (k-1) % d
    print(result * pow(k-2, n-2, d) % d)