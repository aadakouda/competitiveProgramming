class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n
        self.sizes = [1] * n
    def root(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]
    def is_same(self, a, b):
        return self.root(a) == self.root(b)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return False
        if self.ranks[ra] < self.ranks[rb]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        if self.ranks[ra] == self.ranks[rb]:
            self.ranks[ra] += 1
        self.sizes[ra] += self.sizes[rb]
        return True
    def size(self, x):
        return self.sizes[self.root(x)]

n, m = map(int, input().split())
u = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    print('Yes' if not u.unite(a, b) else 'No')