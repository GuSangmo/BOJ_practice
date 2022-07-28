from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        max_length = len(nums)
        results = []
        isvisit = [False] * max_length
        def dfs(arr, cnt):
            if cnt == max_length:
                results.append(arr)
                return 

            for idx, element in enumerate(nums):
                if isvisit[idx]: continue
                isvisit[idx] = True 
                dfs(arr+[element],cnt+1)
                isvisit[idx] = False

        dfs([],0)
        return results

s = Solution()
print(s.permute([1,2,3]))      
        
        