class Solution:
    def Counter(self, s: str) -> dict:
        Counter = defaultdict(int)
        for letter in s:
            Counter[letter] += 1
        return Counter
    def longestPalindrome(self, s: str) -> int:
        counter = self.Counter(s)
        num_odd = 0
        num_even = 0
        is_odd_present = False
        for value in counter:
            if counter[value] % 2 == 0:
                num_even += counter[value]
            else:
                is_odd_present = True
                num_odd += counter[value] - 1
        return num_even + num_odd + is_odd_present
