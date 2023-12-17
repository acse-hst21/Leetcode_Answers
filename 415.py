class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        
        my_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                   '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        
        num1_as_num = 0
        for index, num in enumerate(num1):
            num1_as_num += 10**(len(num1) - index - 1) * my_dict[num]
        
        num2_as_num = 0
        for index, num in enumerate(num2):
            num2_as_num += 10**(len(num2) - index - 1) * my_dict[num]
        
        ans = num1_as_num + num2_as_num

        return str(ans)
