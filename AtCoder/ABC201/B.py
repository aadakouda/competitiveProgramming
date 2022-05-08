n = int(input())
height = {}
S = []
T = []
for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    S.append(s)
    T.append(t)
    height[t] = i
T.sort(reverse=True)
print(S[height[T[1]]])
