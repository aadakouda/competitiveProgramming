n, k = map(int, input().split())
village = 10**100 + 1
friends = {}
for i in range(n):
    a, b = map(int, input().split())
    if a in friends:
        friends[a] += b
    else:
        friends[a] = b
A = sorted(friends.keys())
cur = k
for a in A:
    if a <= cur:
        cur += friends[a]
print(cur)
