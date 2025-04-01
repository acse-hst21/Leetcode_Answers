class Solution:
    def counter(self, words: List[str]) -> dict:
        Counter = defaultdict(int)
        words = ''.join(words)
        for letter in words:
            Counter[letter] += 1
        return Counter
    def makeEqual(self, words: List[str]) -> bool:
        Counter = self.counter(words)
        for letter in Counter:
            if Counter[letter] % len(words) == 0:
                pass
            else:
                return False
        return True
