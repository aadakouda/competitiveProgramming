n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

def dfs(i):
    dist = [-1] * n
    dist[i] = 0
    s = [i]
    while len(s) > 0:
        v = s.pop()
        for g in G[v]:
            if dist[g] == -1:
                s.append(g)
                dist[g] = dist[v] + 1
    return dist

dist0 = dfs(0)
v = dist0.index(max(dist0))
distv = dfs(v)
print(max(distv)+1)