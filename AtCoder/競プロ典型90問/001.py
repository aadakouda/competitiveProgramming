import math
n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
left = 0
right = l
while right - left > 0:
    mid = math.ceil((right-left) / 2) + left
    s = [0]
    for i in range(n):
        if a[i]-s[-1] >= mid:
            s.append(a[i])
        if len(s)-1 >= k:
            break
    if len(s)-1 >= k and l-s[-1] >= mid:
        left = mid
    else:
        right = mid-1
print(left)