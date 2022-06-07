import math


def prime_list(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i+i, n+1, i):
                is_prime[j] = False
    result = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            result.append(i)
    return result


n = int(input())
q = prime_list(math.ceil(n**0.34))
cnt = 0
for i in range(len(q)):
    p = min(n // (q[i]**3), q[i-1])
    
    j = 0
    while q[j] <= p and q[j] < q[i]:
        cnt += 1
        j += 1

print(cnt)