from typing import List, Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Method 2 :: Use the runner method 
        """
        Modify the flow as
        (Before) rev.next <- rev        slow -> slow.next
        (After)           <- rev.next <-  rev         slow    -> 
    
        """
        slow = fast = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev
        
        # If odd num, we need to check except middle term
        if fast:
            slow = slow.next
        
        while slow and rev:
            print("slow:", slow.val, "rev:", rev.val)
            if slow.val != rev.val:
                return False
            slow = slow.next 
            rev = rev.next  
        return True
        



heads = [1,2]
nodes = []
for item in heads:
    node = ListNode()
