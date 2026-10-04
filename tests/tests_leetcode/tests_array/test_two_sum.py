from leetcode.array.two_sum import Solution


def test_success():
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) in ([0, 1], [1, 0])


def test_success_multiple_pairs():
    """Tests a case where multiple pairs sum to the target."""
    nums = [3, 3, 4, 3]
    target = 6
    assert Solution().twoSum(nums, target) in (
        [0, 1],
        [1, 0],
        [0, 3],
        [3, 0],
        [1, 3],
        [3, 1],
    )


def test_return_none():
    """Tests the case where no two numbers sum up to the target."""
    nums = [1, 2, 3, 4]
    target = 10
    assert Solution().twoSum(nums, target) is None


def test_empty_nums_list():
    nums = []
    target = 5
    assert Solution().twoSum(nums, target) is None


def test_single_element_nums_list():
    nums = [5]
    target = 10
    assert Solution().twoSum(nums, target) is None
