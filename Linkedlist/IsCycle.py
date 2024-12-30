# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        visited=set()
        while head != None:
            if head in visited:
                return True
            else:
                visited.add(head)
                head=head.next

        return False
        

""" Tortoise And Hare

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head == fast:
                return True
                
        return False
"""