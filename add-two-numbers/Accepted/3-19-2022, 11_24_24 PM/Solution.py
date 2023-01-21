// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = 0
        w = l = ListNode()
        while True:
            l.val = l1.val + l2.val + r
            r = l.val // 10
            l.val %= 10
            
            l1 = l1.next
            l2 = l2.next
            if l1 == None or l2 == None:
                break            
            
            l.next = ListNode()
            l = l.next
        
        if l1 != None:
            
            l.next = ListNode()
            l = l.next
            
            while True:
                l.val = l1.val + r
                r = l.val // 10
                l.val %= 10
                l1 = l1.next

                if l1 == None:
                    break            

                l.next = ListNode()
                l = l.next
                
        if l2 != None:
            
            l.next = ListNode()
            l = l.next
            
            while True:
                l.val = l2.val + r
                r = l.val // 10
                l.val %= 10
                l2 = l2.next

                if l2 == None:
                    break            

                l.next = ListNode()
                l = l.next
        
        if r != 0:
            l.next = ListNode()
            l = l.next
            l.val = r

        return w