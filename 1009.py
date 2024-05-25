class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_num = bin(n)
        output_bin = []
        for index in range(2, len(bin_num)):
            if bin_num[index] == '1':
                output_bin.append('0')
            else:
                output_bin.append('1')
        return int(''.join(output_bin), 2) 
