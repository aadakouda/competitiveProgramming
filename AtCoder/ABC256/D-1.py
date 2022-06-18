class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1: return x
        else:
          self.par[x] = self.root(self.par[x])
          return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True
    
    def size(self, x):
        return siz[self.root(x)]

n = int(input())
u = UnionFind(n)
s = []
for i in range(n):
    s.append(tuple(map(int, input().split())))
s = sorted(s, key=lambda x: (x[0], x[1]))

i = 0
while i < n:
    if i+1 < n:
        j = i+1
        r = s[i][1]
        while j < n and s[j][0] <= r:
            u.unite(i, j)
            r = max(r, s[j][1])
            j += 1
        i = j
    else:
        break

i = 0
while i < n:
    if i+1 < n:
        j = i+1
        r = s[i][1]
        while j < n and u.issame(i, j):
            r = max(r, s[j][1])
            j += 1
        print(s[i][0], r)
        i = j
    else:
        print(s[i][0], s[i][1])
        break