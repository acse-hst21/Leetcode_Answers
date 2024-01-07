class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = str(bin(num))[2:]
        output = '0b'
        for letter in bin_num:
            if letter == '0':
                output += '1'
            else:
                output += '0'
        return int(output, 2)
