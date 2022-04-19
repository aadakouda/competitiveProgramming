class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.count = n
    def root(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    def unite(self, a, b):
        if self.is_same(a, b):
            return False
        ra = self.root(a)
        rb = self.root(b)
        if self.ranks[ra] < self.ranks[rb]:
            ra, rb = rb, ra
        elif self.ranks[ra] == self.ranks[rb]:
            self.ranks[ra] += 1
        self.parents[rb] = ra
        self.sizes[ra] += self.sizes[rb]
        self.count -= 1
        return True

n, m = map(int, input().split())
u = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    u.unite(a, b)
print(u.count)