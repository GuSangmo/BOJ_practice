from typing import List
from collections import deque
"""
Make new ftn
"""




class Solution:

    def compare_string(self, nums, k):
        n = len(nums)
        new_candidate = nums[:] * (k//n)
        new_candidate += nums[:int(k%n)]
        return new_candidate

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key = lambda x: self.compare_string(x,10))
        result = "".join(nums[::-1])
        if "0" in result[0]: return "0"

        return result

s = Solution()

nums = [0,0]
s.largestNumber(nums)
            
        
        