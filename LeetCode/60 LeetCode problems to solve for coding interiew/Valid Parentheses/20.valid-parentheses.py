#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')': '(', '}': '{', ']': '['}
        stack = []
        i = 0
        while i < len(s):
            if stack and s[i] in parentheses and stack[-1] == parentheses[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return True if not stack else False
        
# @lc code=end

