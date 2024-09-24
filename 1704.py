class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_half = s[:int(len(s)/2)]
        second_half = s[int(len(s)/2):]
        first_counter = sum(1 for letter in first_half if letter in vowels)
        second_counter = sum(1 for letter in second_half if letter in vowels)

        return first_counter == second_counter
