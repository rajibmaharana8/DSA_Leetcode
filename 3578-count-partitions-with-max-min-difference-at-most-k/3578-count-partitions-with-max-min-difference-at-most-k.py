class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1

        from collections import deque
        maxdq = deque()
        mindq = deque()

        L = 0
        for i in range(n):
            # Insert current value into max deque
            while maxdq and nums[maxdq[-1]] <= nums[i]:
                maxdq.pop()
            maxdq.append(i)

            # Insert current value into min deque
            while mindq and nums[mindq[-1]] >= nums[i]:
                mindq.pop()
            mindq.append(i)

            # Shrink left pointer while invalid
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                L += 1
                if maxdq[0] < L:
                    maxdq.popleft()
                if mindq[0] < L:
                    mindq.popleft()

            # Now valid window: L … i
            # dp[i+1] = sum(dp[L] ... dp[i])
            left = L
            right = i
            dp[i + 1] = (pref[right] - (pref[left - 1] if left > 0 else 0)) % MOD

            # update prefix sum
            pref[i + 1] = (pref[i] + dp[i + 1]) % MOD

        return dp[n]
