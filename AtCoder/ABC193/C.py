n = int(input())
s = set()
i = 2
while i**2 <= n:
    j = 2
    while i**j <= n:
        s.add(i**j)
        j += 1
    i += 1
print(n-len(s))