class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_negative = True 
        else:
            is_negative = False

        if is_negative:
            reversed_int = int(str(x)[1:][::-1]) * -1
        else:
            reversed_int = int(str(x)[::-1])
        
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int
