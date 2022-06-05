from collections import deque

Q = int(input())
d = deque()
for i in range(Q):
    q = input()
    if q[0] == '1':
        d.append(tuple(map(int, q.split()))[1:])
    elif q[0] == '2':
        n, c = map(int, q.split())
        s = 0
        while c > 0:
            X, C = d.popleft()
            if c <= C:
                s += X*c
                d.appendleft((X, C-c))
                c = 0
            elif c > C:
                s += X*C
                c -= C
        print(s)