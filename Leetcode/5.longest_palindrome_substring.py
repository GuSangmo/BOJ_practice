class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        D = [[0] * length for _ in range(length)]
        start, end = -1, -1
        max_length = 1
        max_string = ""
        for idx in range(length):
            D[idx][idx] = 1
            start, end = idx, idx
            
        
        for idx in range(length-1):
            if s[idx] == s[idx+1]:
                max_length = 2
                D[idx][idx+1] = 2
                start, end = idx, idx+1

        for term in range(length):
            if term<2 : continue
            for start_idx in range(length):
                end_idx = start_idx + term
                if end_idx >= length : continue 
                if s[start_idx] != s[end_idx] : continue #no need to continue 
                D[start_idx][end_idx] = D[start_idx+1][end_idx-1]+2
                if D[start_idx][end_idx] > max_length:
                    start, end = start_idx, end_idx
        print("max_length:", end-start+1)
        print("max_string:", s[start:end+1])
        return s[start:end+1]

s = Solution()
s.longestPalindrome("babad")
s.longestPalindrome("aaaaaaaaaaaaaaa")     
        
        
                


