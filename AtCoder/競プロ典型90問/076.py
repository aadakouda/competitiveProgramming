from collections import deque

n = int(input())
a = list(map(int, input().split()))
size = sum(a) // 10
sum_size = 0
d = deque()
flg = False
for i in range(n*2):
    cur = i % n
    if a[cur] <= size:
        d.append(a[cur])
        sum_size += a[cur]
        if sum_size == size:
            flg = True
        while sum_size > size:
            sum_size -= d.popleft()
    else:
        d = deque()
        sum_size = 0
print('Yes' if flg else 'No')