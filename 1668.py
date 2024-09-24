class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        output = 0
        counter = 1
        while True:
            if word * counter in sequence:
                output += 1
                counter += 1
            else:
                break
        return output
