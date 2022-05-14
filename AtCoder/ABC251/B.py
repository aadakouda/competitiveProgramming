n, w = map(int, input().split())
A = list(map(int, input().split()))
good = set()

for i in range(n):
    if A[i] <= w:
        good.add(A[i])
    for j in range(i+1, n):
        if A[i]+A[j] <= w:
            good.add(A[i]+A[j])
        for k in range(j+1, n):
            if A[i]+A[j]+A[k] <= w:
                good.add(A[i]+A[j]+A[k])
print(len(good))
