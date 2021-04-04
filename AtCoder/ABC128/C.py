n, m = map(int, input().split())
k = []
s = []

for _ in range(m):
    temp = list(map(int, input().split()))
    k.append(temp[0])
    s.append(temp[1:])

p = list(int, input().split())

cnt = 0

for i in range(m):
    for switch in s[i]:
        
