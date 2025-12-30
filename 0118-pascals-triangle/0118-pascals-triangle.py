class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            temp = []
            val = 1
            for j in range(i + 1):
                if j == 0:
                    val = 1
                else:
                    val = val * (i - j + 1) // j
                temp.append(val)
            triangle.append(temp)
        return triangle