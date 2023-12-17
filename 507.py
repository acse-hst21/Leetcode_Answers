class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum_of_divisors = 1
        for number in range(2, int(num ** 0.5) + 1):
            if num % number == 0:
                sum_of_divisors += number + (num/number)
        return sum_of_divisors == num
