class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            num_as_str = str(num)
            for letter in num_as_str:
                output.append(int(letter))
        return output
