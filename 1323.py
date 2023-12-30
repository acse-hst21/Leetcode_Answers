class Solution:
    def maximum69Number (self, num: int) -> int:
        max_index = 0
        num_as_str = str(num)
        if '6' not in num_as_str:
            return num
        
        for index, num in enumerate(num_as_str):
            if num == '6':
                max_index = index
                break
        
        num_as_str = num_as_str[:index] + '9' + num_as_str[index + 1:]
        return int(num_as_str)
