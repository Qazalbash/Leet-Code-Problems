// https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = head
        while final:
            n = final.val
            first_part = final
            final = final.next
            while final.val == n:
                if final.next:
                    final = final.next
            first_part.next = final
            final = final.next
        return head