n = int(input())
result = []
for i in range(2**n):
    cnt0 = 0
    cnt1 = 0
    res = ''
    for j in range(n):
        if ((i >> j) & 1):
            cnt1 += 1
            res += ')'
        else:
            cnt0 += 1
            res += '('
        if cnt0 < cnt1:
            break
    if cnt0 == cnt1:
        result.append(res)
result.sort()
print(*result, sep='\n')