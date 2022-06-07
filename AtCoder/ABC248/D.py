def search(lst, v):
    l = 0
    r = len(lst)
    while l < r:
        mid = (r-l) // 2 + l
        if lst[mid] < v:
            l = mid + 1
        elif lst[mid] >= v:
            r = mid
    return l

n = int(input())
a = list(map(int, input().split()))
idx = {}
for i in range(n):
    if a[i] in idx:
        idx[a[i]].append(i)
    else:
        idx[a[i]] = [i]
Q = int(input())
q = [input() for _ in range(Q)]
for i in range(Q):
    l, r, x = map(int, q[i].split())
    l -= 1
    r -= 1
    if x in idx:
        l_idx = search(idx[x], l)
        r_idx = search(idx[x], r+1)
        print(r_idx - l_idx)
    else:
        print(0)