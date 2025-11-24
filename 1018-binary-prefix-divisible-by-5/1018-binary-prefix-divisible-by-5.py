class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        temp =[]
        curr=0
        for bit in nums:
            curr = (curr*2 + bit) % 5
            temp.append(curr==0)

        return temp