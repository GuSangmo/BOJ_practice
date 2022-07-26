from typing import List

#23:06 ~ 
"""
Let's use dictionary
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {value: idx for idx, value in  enumerate(nums)}
        for idx, element in enumerate(nums):
            match_idx = num_dict.get(target-element, -1)
            if match_idx > 0 :
                return idx, match_idx
        