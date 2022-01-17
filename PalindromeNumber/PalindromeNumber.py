class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        lens = len(s)
        if lens == 0 or lens == 1:
            return True
        for i in range(lens//2):
            if s[i] != s[lens - 1 - i]:
                return False
        return True
