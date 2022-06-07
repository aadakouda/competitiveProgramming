n, k, a = map(int, input().split())
if a+k < n:
    print(a+k-1)
else:
    k += a - 1
    print(k % n if k % n != 0 else n)