n, x = map(int, input().split())
A = list(map(int, input().split()))
print(' '.join(list(map(str, filter(lambda a: a != x, A)))))
