n = int(input())
p = []
p_set = set()

for i in range(n):
    s, t = map(str, input().split())
    if s not in p_set:
        p_set.add(s)
        p.append([int(t), i])
max_t = 0
min_i = 10**5

for ti in p:
    t = ti[0]
    i = ti[1]
    if t > max_t:
        max_t = t
        min_i = i
    elif t == max_t and i < min_i:
        min_i = i
print(min_i+1)

