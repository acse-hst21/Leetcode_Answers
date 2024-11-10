class Solution:
    def isBalanced(self, num: str) -> bool:
        num_list = [*num]
        sum_even_indices = sum(int(num_list[index]) for index in range(len(num)) if index % 2 == 0)
        sum_odd_indices = sum(int(num_list[index]) for index in range(len(num)) if index % 2 == 1)
        return sum_even_indices == sum_odd_indices
