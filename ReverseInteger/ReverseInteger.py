class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        if sign == -1:
            x *= -1
        digit = []
        while x > 0:
            d = x % 10
            digit.append(str(d))
            x = x // 10
        num = int("".join([d for d in digit])) * sign
        if num > 2147483647 or num < -2147483648:
            return 0
        return num
