import math
import sys

n = int(input())
n_half = math.floor(math.sqrt(n))

for i in range(n_half, 0, -1):
    if n % i == 0:
        print(len(str(n // i)))
        sys.exit()
