class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)
        if total%3==0:
            return total
        rem1 ,rem2 =[],[]

        for i in nums:
            if i%3 == 1:
                rem1.append(i)
            elif i%3 == 2:
                rem2.append(i)
        rem1.sort()
        rem2.sort()

        if total%3 == 2 :
            op1 = total - (rem2[0] if rem2 else float('inf')) 
            op2 = total - (rem1[0] + rem1[1] if len(rem1)>=2 else float('inf'))

        else:
            op1 = total - (rem1[0] if rem1 else float('inf')) 
            op2 = total - (rem2[0]+rem2[1] if len(rem2)>=2 else float('inf'))
        return max(op1,op2)        