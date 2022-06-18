import itertools

h1, h2, h3, w1, w2, w3 = map(int, input().split())

pattern =[x for x in itertools.product(range(1, 31), repeat=3)]

hp = [[] for _ in range(3)]
h = [h1, h2, h3]

for i in range(3):
    for p in pattern:
        if sum(p) == h[i]:
            hp[i].append(p)

cnt = 0

for hp1 in hp[0]:
    for hp2 in hp[1]:
        for hp3 in hp[2]:
            wp1 = hp1[0] + hp2[0] + hp3[0]
            wp2 = hp1[1] + hp2[1] + hp3[1]
            wp3 = hp1[2] + hp2[2] + hp3[2]
            if wp1 == w1 and wp2 == w2 and wp3 == w3:
                cnt += 1

print(cnt)