class Solution:
    def toBinary(self,n):
        bit =[]
        while n>0:
            r=n%2
            bit.append(str(r))
            n=n//2
        bit.reverse()
        return "".join(bit) if bit else "0"

    def countBits(self, n: int) -> List[int]:
        res =[]
        for i in range(n+1):
            temp = self.toBinary(i)
            res.append(temp)

        result = [s.count("1") for s in res]

        return result


    