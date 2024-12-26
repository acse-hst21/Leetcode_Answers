class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_num = ''.join(str(ord(letter) - 97) for letter in firstWord)
        second_num = ''.join(str(ord(letter) - 97) for letter in secondWord)
        target_num = ''.join(str(ord(letter) - 97) for letter in targetWord)

        return int(first_num) + int(second_num) == int(target_num)
