class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for word in words:
            output += word.split(separator)
        return list(filter(lambda word: word != '', output))
