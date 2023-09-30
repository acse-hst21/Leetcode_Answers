class Solution:
    def maxDepth(self, s: str) -> int:
        num_brackets = 0
        num_brackets_list = []
        for value in s:
            if value == '(':
                num_brackets += 1
            elif value == ')':
                num_brackets -= 1
            num_brackets_list.append(num_brackets)
        max_value = max(num_brackets_list)

        return max_value
