a, b, c = map(int, input().split())
lst = [a, b, c]
lst.sort()
if b == lst[1]:
    print('Yes')
else:
    print('No')