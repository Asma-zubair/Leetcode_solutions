# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumy=ListNode(0,head)
        curr=dumy
         
        while curr.next and curr.next.next:
            first=curr.next
            second=curr.next.next
            curr.next=second
            first.next=second.next
            second.next=first
            curr=curr.next.next
        return dumy.next