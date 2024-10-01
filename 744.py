class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        output = letters[0]
        l = 0
        r = len(letters)-1
        while l <= r:
            mid = (l+r) //2
            if ord(letters[mid]) <= ord(target):
                l = mid+1
            else:
                output = letters[mid]
                r = mid-1
        return output
