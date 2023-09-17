class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            binary_num = bin(num)
            ans.append(binary_num.count('1'))
        return ans
