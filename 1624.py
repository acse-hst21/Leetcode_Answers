class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        list_of_lengths = []
        for index1, value1 in enumerate(s):
            for index2, value2 in enumerate(s):
                if value1 == value2:
                    list_of_lengths.append(abs(index1 - index2))
        
        if max(list_of_lengths) == 0:
            return -1
        else:
            return max(list_of_lengths) - 1
