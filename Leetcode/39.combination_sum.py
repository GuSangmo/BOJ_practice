from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(summation, arr, cnt, prev):
            if summation == target:
                results.append(arr)
                return
            elif summation > target:
                return
            
            for idx, element in enumerate(candidates):
                if idx< prev : continue
                dfs(summation + element, arr+ [element], cnt+1, idx)
            
        #Execute 
        dfs(0,[],0,0)
        return results 
