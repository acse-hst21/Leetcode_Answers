class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output = 0
        
        for num in range(low, high + 1):
            if len(str(num)) % 2 != 0:
                continue
            first_half = str(num)[:int(len(str(num))/2)]
            second_half = str(num)[int(len(str(num))/2):]

            sum_first_half = 0
            sum_second_half = 0
            
            for value in first_half:
                sum_first_half += int(value)
            for value in second_half:
                sum_second_half += int(value)
            
            if sum_first_half == sum_second_half:
                output += 1
                print(first_half+second_half)
        return output
