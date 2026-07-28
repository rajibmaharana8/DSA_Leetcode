class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """my_set = set()
        for num in nums:
            my_set.add(num)
        
        for i in range(len(nums)+1):
            if i not in my_set:
                return i
        """
        n = len(nums)
        total = sum(nums)

        res = n*(n+1) // 2
        return res - total