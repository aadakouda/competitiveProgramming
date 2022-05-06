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
        if head is None:
            return False
        rabbit = head.next
        turtle = head
        while rabbit != turtle:
            if rabbit is None or rabbit.next is None:
                return False
            rabbit = rabbit.next.next
            turtle = turtle.next
        return True

# @lc code=end

