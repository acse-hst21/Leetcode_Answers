class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_as_list = s.split()
        nums_in_s = []
        
        for value in s_as_list:
            try:
                nums_in_s.append(int(value))
            except ValueError:
                continue
        
        for index, num in enumerate(nums_in_s):
            if index == 0:
                continue
            if num <= nums_in_s[index - 1]:
                return False
        
        return True
