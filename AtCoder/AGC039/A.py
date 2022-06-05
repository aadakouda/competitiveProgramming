s = list(input())
k = int(input())
r = []
i = 0
while i < len(s):
    cnt = 1
    while i < len(s)-1 and s[i] == s[i+1]:
        cnt += 1
        i += 1
    i += 1
    r.append(cnt)
if s[0] != s[-1]:
    print(sum(R//2 for R in r)*k)
else:
    if len(r) == 1:
        print(r[0]*k // 2)
    else:
        print((r[0]+r[-1])//2 * (k-1) + sum([R//2 for R in r[1:-1]])*k + r[0]//2 + r[-1]//2)
