#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        is_checked = set()
        while head is not None:
            if head in is_checked:
                return True
            is_checked.add(head)
            head = head.next
        return False
# @lc code=end

