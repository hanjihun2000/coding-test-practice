from leetcode.array.max_profit import Solution


def test_success():
    prices = [7, 1, 5, 3, 6, 4]
    assert Solution().maxProfit(prices) == 5


def test_no_profit():
    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0
