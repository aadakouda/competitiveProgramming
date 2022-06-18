n = int(input())
a = list(map(int, input().split()))
m = [0] * 4
p = 0
for i in range(n):
    m[0] += 1
    for j in range(3, -1, -1):
        if j+a[i] > 3:
            p += m[j]
            m[j] = 0
        else:
            m[j+a[i]] += m[j]
            m[j] = 0
print(p)