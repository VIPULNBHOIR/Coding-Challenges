# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp=head
        prev=None
        while temp:
            if temp.val == val:
                if temp == head:
                    temp=head=temp.next
                else:
                    prev.next=temp.next
                    temp=temp.next

            else:
                prev=temp
                temp=temp.next
            
        return head