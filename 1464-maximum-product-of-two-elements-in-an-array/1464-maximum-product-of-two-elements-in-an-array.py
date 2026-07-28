class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max1 = float('-inf')
        max2 = float('-inf')
        idx = 0
        for i in range(n):
            if max1 < nums[i]:
                max1 = nums[i]
                idx = i
        for j in range(n):
            if max2 < nums[j] and idx!=j:
                max2 = nums[j]
            
        return (max1-1)*(max2-1)