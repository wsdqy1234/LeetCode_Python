# 快慢指针法找中点，将后链表反转，而后跟前链表比较

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head.next is None: return True

        slow, fast = head, head
        while fast.next and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        head_r = slow.next # 后半部分链表表头
        slow.next = None
        
        # 反转后半链表
        pre = None
        ptr = head_r
        while ptr.next != None:
            tmp = ptr.next
            ptr.next = pre
            pre = ptr
            ptr = tmp
        ptr.next = pre
        
        # 比较两个链表
        p = head
        while p and ptr is not None:
            if p.val != ptr.val: return False
            p = p.next
            ptr = ptr.next
        return True