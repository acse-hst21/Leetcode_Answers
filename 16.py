class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = inf
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                for index3, num3 in enumerate(nums):
                    if index1 == index2 or index1 == index3 or index2 == index3:
                        continue
                    sum_of_nums = num1 + num2 + num3
                    if sum_of_nums == target:
                        return sum_of_nums
                    if abs(sum_of_nums - target) < diff:
                        diff = abs(sum_of_nums - target)
                        current_value = sum_of_nums
        return current_value
