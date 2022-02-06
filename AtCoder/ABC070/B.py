a, b, c, d = map(int, input().split())
start = max(a, c)
end = min(b, d)
print(end - start if end-start >= 0 else 0)