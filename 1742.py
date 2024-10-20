class Solution:
    def sum_digits(self, num:int) -> int:
        output = 0
        while num:
            output += num % 10
            num //= 10
        return output
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        my_dict = defaultdict(int)
        for num in range(lowLimit, highLimit+1):
            sum_digits = self.sum_digits(num)
            my_dict[sum_digits] += 1
        return max(my_dict.values())
