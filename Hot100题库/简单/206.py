# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1. 通过tmp存储下一个节点，通过pre指向前一个节点，每次都把当前节点的next指向pre，最后返回pre
        pre = None 
        while head != None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

        # 2. 待续