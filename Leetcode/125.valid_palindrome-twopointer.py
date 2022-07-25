"""
Ver 1. Two-pointer
"""

def eval_palindrome(letter):
    # Use two pointer, because of OOM.    
    # Base condition : 0 or 1 letter is palindrome
    if len(letter)< 2: return True


    first = 0 ; end = len(letter)-1
    while first+1< end:
        if letter[first] != letter[end]: #Unmatch, so false
            return False 
        else:
            first+=1 ; end-=1 

    #Finally, 2 cases : first+1 = end or first = end
    if letter[first] != letter[end]:
        return False

    return True

class Solution:
    def isPalindrome(self, string: str) -> bool:
        #Step 1. process the string - use "".join(string)
        preprocess_string = "".join([letter.lower() for letter in string if letter.isalnum()])
        isPalindrome = eval_palindrome(preprocess_string)
        del preprocess_string
        result = "true" if isPalindrome else "false"
        return isPalindrome