class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        head=ListNode()
        temp = head
        while (list1 is not None and list2 is not None):
            if (list1.val <= list2.val):
                temp.next= list1
                list1= list1.next
            else:
                temp.next= list2
                list2=list2.next
            temp=temp.next

        if (list1 is not None):
            temp.next= list1
        if (list2 is not None):
            temp.next=list2
        
        head=head.next
        return head

print(Solution().mergeTwoLists([1,3,4],[2,4]))


