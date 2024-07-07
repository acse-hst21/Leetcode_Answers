class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        return max(True if (2*x) in arr and x != 0 else False for x in arr)
