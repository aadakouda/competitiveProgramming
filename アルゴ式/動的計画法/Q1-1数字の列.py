# https://algo-method.com/tasks/302
n, x, y = map(int, input().split())
a = [0] * n
a[0], a[1] = x, y
for i in range(n):
    a[i] = (a[i-1] + a[i-2]) % 100
print(a[-1])