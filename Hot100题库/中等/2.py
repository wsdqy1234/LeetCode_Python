# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0 #进位
        l = ListNode(0)
        pre = l # 相当于在结果前面补一个pre=0，不然没办法往前指向
        while l1 or l2 is not None:
            if l1 is None:
                v1, v2 = 0, l2.val
                l2 = l2.next
            elif l2 is None:
                v1, v2 = l1.val, 0
                l1 = l1.next
            else:
                v1, v2 = l1.val, l2.val
                l1 = l1.next
                l2 = l2.next
            l.next = ListNode((v1+v2+c)%10)
            c = (v1+v2+c)//10
            l = l.next
        if c == 1: # 最后还有进位
            l.next = ListNode(1)
            l = l.next
            l.next = None
        else:   # 最后没有进位
            l.next = None
        return pre.next

              
            
                