from typing import List, Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Traidional method 1 :: Make the array
        nums = []
        node = head
        while node is not None:
            nums.append(self.val)
            node = node.next
        print("nums:", nums)
        return nums == nums[::-1]