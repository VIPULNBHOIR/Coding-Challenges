# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp=head
        total_node = 0
        while temp:
            temp=temp.next
            total_node +=1
        
        Kth = total_node - n 

        if Kth == 0:
            return head.next

        temp=head
        prev=None

        while Kth > 0 :
            prev=temp
            temp=temp.next
            Kth -= 1
        
        prev.next=temp.next


        return head

