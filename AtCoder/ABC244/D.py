s = list(map(str, input().split()))
t = list(map(str, input().split()))
same = [s[i] == t[i] for i in range(3)]
if sum(same) == 1:
    print('No')
else:
    print('Yes')