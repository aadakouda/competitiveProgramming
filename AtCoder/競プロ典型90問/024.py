n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
diff = [abs(a[i] - b[i]) for i in range(n)]
print('Yes' if k >= sum(diff) and k % 2 == sum(diff) % 2 else 'No')
