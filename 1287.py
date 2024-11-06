class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        counter = 1
        limit = len(arr) // 4
        for index in range(1, len(arr)):
            if arr[index] == arr[index-1]:
                counter += 1
            else:
                counter = 1
            if counter > limit:
                return arr[index]
