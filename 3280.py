class Solution:
    def convertDateToBinary(self, date: str) -> str:
        num_list = date.split('-')
        bin_list = [bin(int(num))[2:] for num in num_list]
        return '-'.join(bin_list)
