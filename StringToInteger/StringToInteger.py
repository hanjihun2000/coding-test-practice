class Solution:
    def myAtoi(self, s: str) -> int:
        lens = len(s)
        sign = 1
        hasSign = False
        res = []

        MAX = 2 ** 31 - 1
        MIN = -(2 ** 31)

        for i in range(lens):
            if hasSign == False and len(res) == 0:  # check if a string s has ' ' (whitespace), '+' and '-' at the front
                if s[i] == ' ':
                    continue
                if s[i] == '-':
                    sign = -1
                    hasSign = True
                    continue
                if s[i] == '+':
                    sign = 1
                    hasSign = True
                    continue
            if ord(s[i]) > 57 or ord(s[i]) < 48:
                break
            res.append(s[i])
        # No digits were read (only strings)
        if len(res) == 0:
            ans = 0
            return ans

        ans = int("".join([str(c) for c in res])) * sign

        if ans > MAX:
            return MAX
        elif ans < MIN:
            return MIN
        else:
            return ans
