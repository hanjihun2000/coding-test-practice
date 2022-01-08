class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
#         Solution using dynamic programming, but keep failing due to "Time Limit Exceeded" at testcase around 170/180
#         However when you run the code using whatever a testcase you want, the code works well.

#         if len(s) <= 1:
#             return s

#         result = s[0]
#         arr = [[0 for c in range(len(s))] for r in range(len(s))]

#         for i in range(len(s)):
#             arr[i][i] = 1 # character itself is a palindrome

#         for lp in range(len(s)):
#             sp = 0
#             while sp < lp:
#                 if s[sp] == s[lp]:
#                     if lp-sp == 1:
#                         arr[sp][lp] = 1
#                     if arr[sp+1][lp-1] == 1:
#                         arr[sp][lp] = 1
#                 if arr[sp][lp] == 1:
#                     if len(result) < len(s[sp:lp+1]):
#                         result = s[sp:lp+1]
#                 sp += 1
#         return result

        result = ""
        length = len(s)

        for i in range(length):
            # for s with odd length
            sp, ep = i, i  # sp is start point, ep is end point
            while sp >= 0 and ep < length and s[sp] == s[ep]:
                pLen = ep-sp+1
                if len(result) < pLen:
                    result = s[sp:ep+1]
                sp, ep = sp-1, ep+1

            # for s with even length
            sp, ep = i, i+1
            while sp >= 0 and ep < length and s[sp] == s[ep]:
                pLen = ep-sp+1
                if len(result) < pLen:
                    result = s[sp:ep+1]
                sp, ep = sp-1, ep+1
        return result
