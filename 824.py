class Solution:
    def beginWithVowel(self, word: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if word[0].lower() in vowels:
            return word + 'ma'
        else:
            return word[1:] + word[0] + 'ma'
    def toGoatLatin(self, sentence: str) -> str:
        res = ''
        for index, word in enumerate(sentence.split()):
            res += self.beginWithVowel(word) + ((index+1) * 'a') + ' '
        return res.rstrip()
