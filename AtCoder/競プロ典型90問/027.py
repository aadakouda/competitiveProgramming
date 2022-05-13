n = int(input())
s = [input() for _ in range(n)]
name = set()
for i in range(n):
    if s[i] not in name:
        print(i+1)
    name.add(s[i])
