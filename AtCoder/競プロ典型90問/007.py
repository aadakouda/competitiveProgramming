n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]
a.sort()
for i in range(q):
    right = n-1
    left = 0
    while right-left > 0:
        mid = (right-left) // 2 + left
        if b[i] < a[mid]:
            right = mid
        else:
            left = mid+1
    print(min(abs(a[right]-b[i]), abs(a[right-1]-b[i])))