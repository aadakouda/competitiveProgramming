n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
y = 0
for i in range(n):
    if a[i] == b[i]:
        x += 1
for i in range(n):
    for j in range(n):
        if a[i] == b[j] and i != j:
            y += 1
print(x)
print(y)