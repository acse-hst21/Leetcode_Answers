class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_values = set(arr)
        count = []
        for num in unique_values:
            count.append(arr.count(num))
        if len(set(count)) == len(count):
            return True
        return False
