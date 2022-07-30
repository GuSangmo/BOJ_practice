from typing import List

"""
method 2 : Record all route!
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        length = len(nums)

        def make_dfs_subset(idx, subset):
            results.append(subset)

            for i in range(idx, length):
                make_dfs_subset(i+1, subset+[nums[i]])
        make_dfs_subset(0,[])

        return results
"""
idx = 0

"""


s = Solution() 

print(s.subsets([1,2,3]))
