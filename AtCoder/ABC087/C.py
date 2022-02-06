n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
result = [0] * n
for i in range(n):
    flg = False
    for j in range(n):
        if j == i:
            result[i] += a1[j] + a2[j]
            flg = True
        else:
            if not flg:
                result[i] += a1[j]
            else:
                result[i] += a2[j]
print(max(result))