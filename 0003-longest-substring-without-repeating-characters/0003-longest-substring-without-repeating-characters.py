class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sett = set()
        max_len =0
        for h in range(len(s)):
            while s[h] in sett:
                sett.remove(s[l])
                l+=1
                
            sett.add(s[h])
            max_len = max(max_len,h-l+1)
        return max_len


            
            

