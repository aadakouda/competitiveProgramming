# n = int(input())
# min = 10000000000
#
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i * j == n:
#             if min > max(len(str(i)), len(str(j))):
#                 min = max(len(str(i)), len(str(j)))
#
# print(min)

import math
import sys

n = input()
n_half = math.ceil((len(n) + 1) / 2)

for i in range(1, n_half + 1):
    for j in range(10 ** n_half, 10 ** (n_half - 1), -1):
        for k in range(10 ** (int(n) - n_half), 10 ** (int(n) - n_half - 1), -1):
            if j * k == int(n):
                print(i)
                sys.exit()
