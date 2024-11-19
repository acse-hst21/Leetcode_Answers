class Solution:
    def counter(self, text: str) -> int:
        counter = defaultdict(int)
        for letter in text:
            counter[letter] += 1
        return counter
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_counter = self.counter('balloon')
        text_counter = self.counter(text)
        output = 0
        while True:
            for letter in balloon_counter:
                text_counter[letter] -= balloon_counter[letter]
                if text_counter[letter] < 0:
                    return output
            output += 1
