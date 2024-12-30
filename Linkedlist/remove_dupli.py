if head == None or head.next == None:
    return head
counter=1
temp=head
while temp and temp.next:
    if temp.val==temp.next.val:
        counter += 1
    else:
        counter = 1
    if counter > 1:
        temp.next=temp.next.next
    else:
        temp=temp.next

return head


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        counter=1
        temp=head
        while temp and temp.next:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next

        return head
"""