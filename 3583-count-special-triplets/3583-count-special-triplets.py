from collections import Counter

class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Frequency map for right side (all elements initially)
        right = Counter(nums)
        left = Counter()
        
        result = 0
        
        for j in range(len(nums)):
            val = nums[j]
            
            # Remove current element from right (since j is now considered)
            right[val] -= 1
            
            # Count how many i < j satisfy nums[i] == 2*val
            countLeft = left[2 * val]
            
            # Count how many k > j satisfy nums[k] == 2*val
            countRight = right[2 * val]
            
            # Add contribution
            result = (result + countLeft * countRight) % MOD
            
            # Add current element to left
            left[val] += 1
        
        return result