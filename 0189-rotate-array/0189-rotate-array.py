class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k = k % n
        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]
            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt
                count += 1
                if start == current:
                    break
            start += 1