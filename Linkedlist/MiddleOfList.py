# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next==None:
            return head
            
        double=head.next.next
        while head:
            if double == None:
                return head.next
            elif double.next == None:
                return head.next
            else:
                head=head.next
                double=double.next.next

