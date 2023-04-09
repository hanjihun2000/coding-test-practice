class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = target - x
                if nums[j] == y:
                    result = [i, j]
                    return result
