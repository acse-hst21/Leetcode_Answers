class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        my_dict = {}
        for letter in s:
            if letter in my_dict:
                my_dict[letter] += 1
            else:
                my_dict[letter] = 1
        return len(set(my_dict.values())) == 1
