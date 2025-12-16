class Solution(object):
    def uniquePaths(self, m, n):
        return self.comb(m + n - 2, m - 1)

    def comb(self, n, k):
        if k > n - k:
            k = n - k
        res = 1
        for i in range(1, k + 1):
            res = res * (n - k + i) // i
        return res