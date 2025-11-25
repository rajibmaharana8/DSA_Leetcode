class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        # If k is divisible by 2 or 5, no such number exists
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 1 % k
        length = 1
        visited = set()

        while remainder != 0:
            if remainder in visited:
                return -1
            visited.add(remainder)

            remainder = (remainder * 10 + 1) % k
            length += 1

        return length