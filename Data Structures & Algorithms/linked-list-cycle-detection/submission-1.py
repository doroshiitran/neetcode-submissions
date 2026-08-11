# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Core problem: the index is not gonna giving through parameter so we have to detect whether the tail is pointing to another node making a loops, the tail not gonna point to None
        If i loop current.next, if it's true it will loop forever cause there is no None at the end of the list
        hash_set ={}
        loop while current: and add each node to set
        if node in hash_set return true 
        """
        slow = head
        fast = head
        if head is None or head.next is None:
            return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False