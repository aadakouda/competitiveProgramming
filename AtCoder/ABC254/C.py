n, k = map(int, input().split())
a = list(map(int, input().split()))
a_sort = sorted(a)
flg = True
for i in range(k):
    a_set = set([a[j] for j in range(i, n, k)])
    as_set = set([a_sort[j] for j in range(i, n, k)])
    if a_set != as_set:
        flg = False
print('Yes' if flg else 'No')