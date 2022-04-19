class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.min_nums = [i for i in range(n)]
    def root(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]
    def unite(self, a, b):
        if self.root(a) == self.root(b):
            return False
        ra = self.root(a)
        rb = self.root(b)
        if self.ranks[ra] < self.ranks[rb]:
            ra, rb = rb, ra
        elif self.ranks[ra] == self.ranks[rb]:
            self.ranks[ra] += 1
        self.parents[rb] = ra
        self.sizes[ra] += self.sizes[rb]
        self.min_nums[ra] = min(self.min_nums[ra], self.min_nums[rb])
        return True
    def get_min(self, x):
        return self.min_nums[self.root(x)]

n, m = map(int, input().split())
u = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    u.unite(a, b)
for i in range(n):
    print(u.get_min(i))