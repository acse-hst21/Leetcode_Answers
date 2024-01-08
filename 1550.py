class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for index, _ in enumerate(arr):
            if index <= 1:
                pass
            else:
                if arr[index] % 2 != 0 and arr[index - 1] % 2 != 0 and arr[index - 2] % 2 != 0:
                    return True
        return False
