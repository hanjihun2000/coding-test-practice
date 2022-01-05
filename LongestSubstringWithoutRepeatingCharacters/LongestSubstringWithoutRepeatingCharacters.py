class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        output = 0
        sub = []
        for i in range(len(s)):
            if s[i] in sub:
                start = sub.index(s[i]) + 1
                sub = sub[start:]
                sub.append(s[i])
                output = max(output, len(sub))
            else:
                sub.append(s[i])
                output = max(output, len(sub))
        return output
