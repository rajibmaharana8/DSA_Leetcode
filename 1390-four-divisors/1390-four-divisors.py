from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(n: int) -> List[int]:
            divisors = set()
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                if len(divisors) > 4:  # early exit
                    return []
            return list(divisors)

        total = 0
        for num in nums:
            divisors = get_divisors(num)
            if len(divisors) == 4:
                total += sum(divisors)
        return total