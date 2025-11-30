class Solution(object):
    def minSubarray(self, nums, p):
        total = sum(nums)
        rem = total % p
        if rem==0:
            return 0

        prefix = 0
        last_seen = {0:-1}
        ans = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - rem) % p

            if need in last_seen:
                ans = min(ans, i - last_seen[need])

            last_seen[prefix] = i

        return -1 if ans == len(nums) else ans