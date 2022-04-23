n = int(input())
A = list(map(int, input().split()))
dictA = {}
for a in sorted(A):
    if a in dictA:
        dictA[a] += 1
    else:
        dictA[a] = 1
count = 0
m = max(dictA.keys())

for i, vi in dictA.items():
    for j, vj in dictA.items():
        if i*j > m:
            break
        if i*j in dictA:
            count += vi * vj * dictA[i*j]

print(count)