# https://recursionist.io/dashboard/problems/370

def recursiveIsPalindrome(s):
    s = s.replace(' ', '').lower()
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return recursiveIsPalindrome(s[1:-1])
