import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops =0

        while nums[0]<k:
            if len(nums)<2:
                return -1

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            new_val = min(x,y) *2 + max(x,y)

            heapq.heappush(nums,new_val)
            ops+=1

        return ops
        