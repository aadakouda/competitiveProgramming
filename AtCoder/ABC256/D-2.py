from collections import deque
n = int(input())
s = []
for i in range(n):
    s.append(tuple(map(int, input().split())))
s = sorted(s, key=lambda x: (x[0], x[1]))

d = deque()
d.append(s[0][0])
d.append(s[0][1])
for i in range(1, n):
    if s[i][0] <= d[-1] and d[-1] < s[i][1]:
        d.append(s[i][1])
    elif d[-1] < s[i][0]:
        print(d[0], d[-1])
        d = deque()
        d.append(s[i][0])
        d.append(s[i][1])
print(d[0], d[-1])