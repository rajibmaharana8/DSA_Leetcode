class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum =0
        max = float('-inf')
        n = len(nums)
        for i in range(n):
            sum += nums[i]

            if ( max < sum):
                max =sum
            if(sum<0):
                sum =0
        return max