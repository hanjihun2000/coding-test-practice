class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in nums:
            c = nums.count(i)
            n = c * (c - 1) // 2
            pairs += n
            nums = [j for j in nums if j != i]
        return pairs
