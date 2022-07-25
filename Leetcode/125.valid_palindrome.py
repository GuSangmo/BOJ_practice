"""
Ver 2. Use slicing
"""
class Solution:
    def isPalindrome(self, string: str) -> bool:
        preprocess_string = "".join([letter.lower() for letter in string if letter.isalnum()])
        return preprocess_string == preprocess_string[::-1]