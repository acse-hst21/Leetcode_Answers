class Solution:
    def reformat(self, s: str) -> str:
        list_of_chars = []
        list_of_nums = []

        output = ''
        for value in s:
            try:
                type(int(value)) == int
                list_of_nums.append(value)
            except ValueError:
                list_of_chars.append(value)
        
        if abs(len(list_of_chars) - len(list_of_nums)) > 1:
            return ''
        else:
            if len(list_of_chars) - len(list_of_nums) >= 0:
                for index in range(len(s)):
                    if index % 2 == 0:
                        output += list_of_chars[int(index/2)]
                    else:
                        output += list_of_nums[int(index/2) - 1]
            elif len(list_of_nums) - len(list_of_chars):
                for index in range(len(s)):
                    if index % 2 == 0:
                        output += list_of_nums[int(index/2)]
                    else:
                        output += list_of_chars[int(index/2) - 1]
        return output
