#n = int(input())
#a1 = list(map(int, input().split()))
#a2 = list(map(int, input().split()))
#result = [0] * n
#for i in range(n):
#    flg = False
#    for j in range(n):
#        if j == i:
#            result[i] += a1[j] + a2[j]
#            flg = True
#        else:
#            if not flg:
#                result[i] += a1[j]
#            else:
#                result[i] += a2[j]
#print(max(result))

n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
r1 = [0] * n
r1[0] = a1[0]
r2 = [0] * n
r2[-1] = a2[-1]
for i in range(1, n):
    r1[i] = r1[i-1] + a1[i]
for i in range(n-2, -1, -1):
    r2[i] = r2[i+1] + a2[i]
print(max([r1[i]+r2[i] for i in range(n)]))