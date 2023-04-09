import math

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if lens <= 1 or numRows == 1:
            return s
        width = int(math.ceil(float(lens)/(2*numRows-2))*(numRows-1))
        arr = [[None for c in range(width)] for r in range(numRows)]
        r, c = 0, 0
        for i in s:
            if r < numRows-1 and c % (numRows-1) == 0:
                arr[r][c] = i
                r += 1
            elif r == numRows-1 and c % (numRows-1) == 0:
                arr[r][c] = i
                r -= 1
                c += 1
            elif c % (numRows-1) != 0:
                arr[r][c] = i
                r -= 1
                c += 1
        result = "".join([str(c) for l in arr for c in l if c != None])
        return result
