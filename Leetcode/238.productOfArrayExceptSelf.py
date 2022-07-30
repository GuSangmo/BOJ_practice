from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        result[i] = mul(nums[:i-1]) * mul(nums[i+1:])        
        Thus we make two list, recording prouduct of elements forward, backward resepectively
        """
        forwards = []
        backwards = []
        mul1 = 1 ; mul2 = 1
        for number in nums:
            mul1 *= number 
            forwards.append(mul1)
        
        for number in nums[::-1]:
            mul2 *= number 
            backwards.append(mul2)
        backwards.reverse()
        
        #Result 
        results = []
        for idx, number in enumerate(nums):
            if idx == 0: results.append(backwards[1])
            elif idx == len(nums)-1 : results.append(forwards[idx-1])
            else: results.append(forwards[idx-1] * backwards[idx+1])
        return results

s = Solution() 

num1 = [1,2,3,4]
num2 = [-1,1,0,-3,3]

print(s.productExceptSelf(num1))
print(s.productExceptSelf(num2))
        
            
        