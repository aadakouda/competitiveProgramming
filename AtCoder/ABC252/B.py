n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
uma = set()
max_uma = 0
for i in range(n):
    if a[i] > max_uma:
        max_uma = a[i]
        uma = set([i+1])
    elif a[i] == max_uma:
        uma.add(i+1)
flg = False
for i in range(k):
    if b[i] in uma:
        flg = True
        break
print('Yes' if flg else 'No')