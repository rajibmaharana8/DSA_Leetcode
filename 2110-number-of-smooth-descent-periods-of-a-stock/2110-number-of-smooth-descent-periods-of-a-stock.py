class Solution(object):
    def getDescentPeriods(self, prices):
        res = 0
        counter = 1
        prev_num = prices[0]
        for p in prices:
            if p == prev_num - 1:
                counter += 1
            else:
                counter = 1
            res += counter
            prev_num = p
        return res
