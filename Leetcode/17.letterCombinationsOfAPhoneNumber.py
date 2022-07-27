from typing import List


#7:56 ~

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        total_digit = len(digits)
        results = []
        def dfs_dial(final_cands, cnt, idx):
            if cnt == total_digit:
                results.append(final_cands)
                return 
            current_dial = digits[idx]
            alphabets = num_to_letter[current_dial]

            for alphabet in alphabets:
                dfs_dial(final_cands+alphabet, cnt+1, idx+1)
        
        dfs_dial("",0,0)
     
        if not results[0]: results = []
        # print("results:", results)
        return results

    



s = Solution() 
digits1 = ""

s.letterCombinations(digits1)
                
                