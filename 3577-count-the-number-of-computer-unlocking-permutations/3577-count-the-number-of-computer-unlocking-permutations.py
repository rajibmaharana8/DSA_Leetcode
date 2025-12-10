class Solution(object):
    def countPermutations(self, complexity):
        M = 10**9 + 7
        result =1
        for i in range(1,len(complexity)):
            if (complexity[i]<=complexity[0]):
                return 0
            result = (result * i)%M

        return result