from typing import List

"""
method 1 : iterative call without for loop
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        length = len(nums)

        def make_dfs_subset(subset, cur_idx):
            if cur_idx == length :
                print("list:", subset) 
                results.append(list(subset))
                return 

            # Include current cur_idx
            make_dfs_subset(subset, cur_idx+1)

            #Exclude current cur_idx
            subset.append(nums[cur_idx])
            make_dfs_subset(subset, cur_idx+1)
            subset.remove(nums[cur_idx])

        make_dfs_subset([],0)

        return results

"""
idx = 0

"""
[1]

s = Solution() 

print(s.subsets([1,2,3]))
