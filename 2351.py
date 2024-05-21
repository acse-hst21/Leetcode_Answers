class Solution:
    def repeatedCharacter(self, s: str) -> str:
        list_of_letters = []
        for letter in s:
            if letter in list_of_letters:
                return letter
            list_of_letters.append(letter)
