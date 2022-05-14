w = int(input())

result = [i for i in range(1, 100)] + [i*100 for i in range(1, 100)] + [i*10000 for i in range(1, 100)] + [10**6]

print(len(result))
print(*result)
