from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merge_intervals = []
        
        merge_start, merge_end = -1, -1
        for idx, (start, end) in enumerate(intervals):
            if idx == 0 :
                merge_start, merge_end = start, end 
                continue
                            
            """
            If overlapped, keep going else continue !
            """
            
            #If new segment, modify the pointer
            if start > merge_end :
                merge_intervals.append([merge_start, merge_end])
                merge_start = start 
                merge_end = end
            
            else:
                merge_end = max(merge_end, end)
        #Last segment
        merge_intervals.append([merge_start, merge_end])
        return merge_intervals
s = Solution()

intervals = [[1,3]]
print(s.merge(intervals))
            
            
            
        
        