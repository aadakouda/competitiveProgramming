n = int(input())
first = [0] * n
second = [0] * n
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        first[i] = p
    else:
        second[i] = p
for i in range(n-1):
    first[i+1] += first[i]
    second[i+1] += second[i]
first.insert(0, 0)
second.insert(0, 0)
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(first[r] - first[l-1], second[r]- second[l-1])