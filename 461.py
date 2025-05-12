class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        max_len = max(len(bin_x), len(bin_y))
        bin_x = bin_x.zfill(max_len)
        bin_y = bin_y.zfill(max_len)
        return sum(abs(int(a) - int(b)) for a, b in zip(bin_x, bin_y))
