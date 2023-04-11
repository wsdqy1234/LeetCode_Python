# 采用快慢指针法，如果快指针遇到了慢指针，说明成环了；如果快指针最后指向空，说明没成环

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None: # 因为fast一次走2步
                return False
            slow = slow.next
            fast = fast.next.next
        return True