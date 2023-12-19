class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        if money - sorted_prices[0] - sorted_prices[1] >= 0:
            return money - sorted_prices[0] - sorted_prices[1]
        return money
