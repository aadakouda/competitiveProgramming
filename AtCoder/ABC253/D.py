import math

n, a, b = map(int, input().split())
c = a*b // math.gcd(a, b)
cnt1 = n // a
cnt2 = n // b
cnt3 = n // c
sumn = (1+n)*n // 2
suma = a * ((1+cnt1)*cnt1 // 2)
sumb = b * ((1+cnt2)*cnt2 // 2)
sumc = c * ((1+cnt3)*cnt3 // 2)
result = sumn-suma-sumb+sumc
print(result)