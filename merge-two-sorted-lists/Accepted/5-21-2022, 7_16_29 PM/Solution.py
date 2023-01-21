// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        head = final
        
        while list1 and list2:
            if list1.val < list2.val:
                final.next = ListNode(list1.val)
                list1 = list1.next
            else:
                final.next = ListNode(list2.val)
                list2 = list2.next
            final = final.next
        
        if list1:
            final.next = list1
        else:
            final.next = list2
            
        return head.next