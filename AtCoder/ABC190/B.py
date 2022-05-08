n, s, d = map(int, input().split())
flg = False
for i in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        flg = True
print('Yes' if flg else 'No')
