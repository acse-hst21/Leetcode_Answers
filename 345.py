class Solution:
    def reverseVowels(self, s: str) -> str:
        new_s = []
        missing_vowels = []

        for letter in s:
            if letter in 'aeiouAEIOU':
                new_s.append(1)
                missing_vowels.append(letter)
            else:
                new_s.append(letter)
        
        for index, letter in enumerate(new_s):
            if letter != 1:
                pass
            else:
                new_s[index] = missing_vowels[-1]
                missing_vowels = missing_vowels[:-1]

        return ''.join(new_s)
