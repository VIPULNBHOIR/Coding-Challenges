# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        if not head or not head.next:
            return head
        current=head
        prev=None
        next=head.next
        while next:
            next=current.next
            current.next=prev
            prev=current
            current=next
        
        return prev
            
        