import sys

n = int(input())
length = 2*n + 2
used = [False] * (2*n + 2)
used[0] = True
for i in range(2*n+1):
    for j in range(length):
        if not used[j]:
            sys.stdout.write(str(j)+'\n')
            sys.stdout.flush()
            used[j] = True
            break
    if all(used):
        input()
        break
    aoki = int(input())
    used[aoki] = True