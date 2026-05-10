class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res=""
        max_len = 0
        for i in range(len(s)):
            #odd length
            l,r = i,i
            while self.isPalindrome(s,l,r):
                if(r-l+1 > max_len):
                    res = s[l:r+1]
                    max_len= max(max_len,r-l+1)
                l-=1
                r+=1

            #even length
            l,r=i,i+1

            while self.isPalindrome(s,l,r):
                if(r-l+1 > max_len):
                    res = s[l:r+1]
                    max_len= max(max_len,r-l+1)
                l-=1
                r+=1
        return res
    
    def isPalindrome(self,s,l,r):
        if (l>= 0 and r< len(s) and s[l]==s[r]):
            return True
    