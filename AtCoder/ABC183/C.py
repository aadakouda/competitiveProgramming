import itertools
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
result = 0

for s in itertools.permutations(range(1, n)):
    temp = t[0][s[0]]
    for i in range(1, n-1):
        temp += t[s[i-1]][s[i]]
    temp += t[s[-1]][0]
    if temp == k:
        result += 1
print(result)