from typing import List

"""
Use three pointer
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        total = 0
        for idx, first_element in enumerate(nums):
            if idx>0 and nums[idx] == nums[idx-1]:
                continue
                        
            start = idx+1 
            end = len(nums)-1 
            
            while start<end:
                if first_element + nums[start]+ nums[end] > 0 :
                    end -= 1 
                elif first_element + nums[start]+ nums[end] < 0 :
                    start+=1
                else:
                    results.append([first_element, nums[start], nums[end]])
                    while start<end and nums[start] == nums[start+1]:
                        start += 1
                    while start<end and nums[end] == nums[end-1]:
                        end -= 1                    
                    start +=1 
                    end -= 1
        return results 

s = Solution()

num1 = [0,1,1]
num2 = [0,0,0]
num3 = [-3,-3,1,1,2,2]
print(s.threeSum(num1))
print(s.threeSum(num2))
print(s.threeSum(num3))
        