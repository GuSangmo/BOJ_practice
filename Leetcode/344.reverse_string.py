# 3 Minute

from typing import List

"""
Method 1 :: two pointer

Method 2 :: built_in fuction
"""



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0 ; end = len(s)-1 
        while start+1<=end:
            s[start], s[end] = s[end], s[start]
            start+=1 ; end-=1
        return s 
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


