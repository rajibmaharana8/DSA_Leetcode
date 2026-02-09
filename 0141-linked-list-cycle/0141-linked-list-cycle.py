# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s_head = head
        f_head = head
        while f_head is not None and f_head.next is not None:
            s_head = s_head.next
            f_head = f_head.next.next

            if s_head==f_head:
                return True
        return False