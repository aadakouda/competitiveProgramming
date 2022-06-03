n, a, b = map(int, input().split())
nr1 = ('.'*b + '#'*b) * n
nr1 = nr1[:len(nr1)//2]
nm = [nr1] * a
nr2 = ('#'*b + '.'*b) * n
nr2 = nr2[:len(nr2)//2]
nm += [nr2] * a
nm *= n
nm = nm[:len(nm)//2]
for i in range(len(nm)):
    print(*nm[i], sep='')