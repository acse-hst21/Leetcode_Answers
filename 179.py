class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))
        arr.sort(key=lambda x: x*10, reverse=True)
        return '0' if arr[0] == '0' else ''.join(arr)
