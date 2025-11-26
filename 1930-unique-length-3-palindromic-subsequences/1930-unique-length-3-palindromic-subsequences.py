class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        last = {}
        
        # Record first and last occurrence of each character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        
        palindromes = set()
        
        # For each possible outer character
        for ch in first:
            if first[ch] < last[ch]:
                # Middle characters between first and last occurrence
                for mid in set(s[first[ch]+1:last[ch]]):
                    palindromes.add(ch + mid + ch)
        
        return len(palindromes)