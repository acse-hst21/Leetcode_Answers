class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        output = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for word in words[left:right+1]:
            if word[0] in vowels and word[-1] in vowels:
                output += 1
        return output
