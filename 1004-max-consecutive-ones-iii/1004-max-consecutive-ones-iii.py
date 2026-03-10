class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right,maxx = 0,0,0
        zeroes = 0
        while right< len(nums):
            if nums[right] == 0:
                zeroes+=1
            if zeroes>k:
                if nums[left]==0:
                    zeroes-=1
                left+=1
            if zeroes<=k:
                maxx = max(maxx,right-left+1)
            right+=1
        return maxx

