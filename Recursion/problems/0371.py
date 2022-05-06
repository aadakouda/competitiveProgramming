# https://recursionist.io/dashboard/problems/371

def helper(f1, f2, total, n):
    if n == 0:
        return total
    return helper(f2, f1+f2, total+f1+f2, n-1)

def fibonacciTotal(n):
    # nは自然数とあるが、テストケースに存在するため
    if n == 0:
        return 0
    return helper(0, 1, 1, n-1)
