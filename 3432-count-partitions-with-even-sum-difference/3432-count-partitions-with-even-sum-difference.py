class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)   # total sum of array
        prefix = 0
        count = 0
        
        # iterate through valid partition indices
        for i in range(len(nums) - 1):
            prefix += nums[i]
            right = total - prefix
            # check if both sums have same parity
            if prefix % 2 == right % 2:
                count += 1
        
        return count