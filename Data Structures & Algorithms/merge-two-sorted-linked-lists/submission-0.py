# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        List 1 empty => Return list 2
        List 2 empty => Return list 1
        Initial an ans listnode w head = None, previous = head, current = previous.next
        Comparing 2 value in list1 and list 2, any smaller value could go to ans listnode, after add a value, the pointer will increase at the working list: previous: current, current = current.next
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        ans = ListNode()
        previous = ans
        current1, current2 = list1, list2
        while current1 and current2:
            if current1.val < current2.val:
                previous.next = current1
                current1 = current1.next
            else:
                previous.next = current2
                current2 = current2.next
            previous = previous.next
        if current1:
            previous.next = current1
        if current2:
            previous.next = current2
        return ans.next