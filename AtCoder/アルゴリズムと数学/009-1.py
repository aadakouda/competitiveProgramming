n, s = map(int, input().split())
a = list(map(int, input().split()))
flg = False
for i in range(2**n):
    temp = 0
    for j in range(n):
        if ((i >> j) & 1):
            temp += a[j]
        if temp == s:
            flg = True
            break
print('Yes' if flg else 'No')