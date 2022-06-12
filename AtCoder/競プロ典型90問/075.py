import math

def check_prime(n):
    flg = True
    i = 2
    while i*i <= n:
        if n % i == 0:
            flg = False
            break
        i += 1
    return flg

n = int(input())
i = 2
cnt = 0

while i*i <= n:
    while n % i == 0:
        cnt += 1
        n //= i
    i += 1
if n != 1:
    cnt += 1

result = 0
while cnt > 1:
    result += 1
    cnt = math.ceil(cnt / 2)
print(result)
