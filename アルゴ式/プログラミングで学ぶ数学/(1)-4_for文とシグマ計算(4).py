# https://algo-method.com/tasks/569

n = int(input())
result = 0

for i in range(1, n):
    for j in range(i+1, n+1):
        result += i * j

print(result)
