import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
q = p[:k]
heapq.heapify(q)
print(min(q))
for i in range(k, n):
    mi = heapq.heappop(q)
    mi = max(mi, p[i])
    heapq.heappush(q, mi)
    kth = heapq.heappop(q)
    print(kth)
    heapq.heappush(q, kth)