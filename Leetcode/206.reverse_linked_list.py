from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None 
        node = head
        """
        rev.next <- rev   node -> node.next
                 rev.next<-rev      node
        """
        while node is not None:
            node, rev, rev.next = node.next, node, rev 
        return rev
        