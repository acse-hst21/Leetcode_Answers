class Solution:
    def counter(self, s: str) -> dict:
        counter = defaultdict(int)
        for letter in s:
            counter[letter] += 1
        return counter
    def checkRecord(self, s: str) -> bool:
        return self.counter(s)['A'] < 2 and 'LLL' not in s
