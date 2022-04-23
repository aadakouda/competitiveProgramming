import string

existsUpper = False
existsLower = False
S = input()

for s in S:
    if s in string.ascii_lowercase:
        existsLower = True
    elif s in string.ascii_uppercase:
        existsUpper = True

print('Yes' if existsLower and existsUpper and len(set(S)) == len(S) else 'No')