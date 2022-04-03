a, b, c, d = map(int, input().split())
flg = True
if a > c:
    flg = False
elif a == c:
    if b > d:
        flg = False
print('Takahashi' if flg else 'Aoki')