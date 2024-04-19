class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        encrypted_nums = []
        for num in nums:
            max_digit = max(int(digit) for digit in str(num))
            encrypted_num = int(str(1111)[:len(str(num))]) * max_digit
            encrypted_nums.append(encrypted_num)
        return sum(encrypted_nums)
