class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        count = 1
        max_count = 1
        nums = sorted(set(nums))

        for i in range(len(nums)-1):

            if nums[i] == nums[i+1] or nums[i]+1 != nums[i+1]:
                count = 1
                continue

            else:
                count+=1
            max_count = max(max_count,count)
        
        return max_count