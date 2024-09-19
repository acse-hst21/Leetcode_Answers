class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(' ')
        output = [0] * len(s_list)
        for word in s_list:
            output[int(word[-1])-1] = word[:-1]
        return ' '.join(output)
