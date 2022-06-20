from collections import deque
S = input()
d = deque()
for s in S:
    d.append(s)
Q = int(input())
q = [input() for _ in range(Q)]
reverse = False
for i in range(Q):
    if q[i][0] == '1':
        reverse = not reverse
    elif q[i][0] == '2':
        t, f, c = map(str, q[i].split())
        if (not reverse and f == '1') or (reverse and f == '2'):
            d.appendleft(c)
        else:
            d.append(c)
if reverse:
    for i in range(len(d)-1, -1, -1):
        print(d[i], end='')
    print()
else:
    print(''.join(d))