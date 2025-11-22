class Solution(object):
    def minimumOperations(self, nums):
        op = 0
        for i in range(len(nums)):
            if(nums[i]%3==1):
                op+=1
            elif(nums[i]%3==2):
                op+=1
            else:
                continue
        return op