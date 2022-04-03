n = int(input())
a = list(map(int, input().split()))
used = [False] * 3000
for A in a:
    used[A] = True
for i in range(3000):
    if not used[i]:
        print(i)
        break