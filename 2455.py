class Solution:
    def averageValue(self, nums: List[int]) -> int:
        multiples_of_three = []
        for num in nums:
            if num % 6 == 0:
                multiples_of_three.append(num)
        if len(multiples_of_three) == 0:
            return 0
        return int(sum(multiples_of_three)/len(multiples_of_three))
