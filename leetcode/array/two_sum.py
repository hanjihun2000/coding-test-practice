class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hashmap = {}

        for i in range(n):
            t = target - nums[i]
            if t in hashmap:
                return [i, hashmap[t]]
            hashmap[nums[i]] = i
