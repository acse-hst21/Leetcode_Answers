class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_digits = 1
        sum_digits = 0
        for num in str(n):
            prod_digits = prod_digits * int(num)
            sum_digits += int(num)
        return prod_digits - sum_digits
