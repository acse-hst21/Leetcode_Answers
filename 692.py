class Solution:
    def sorted_counter(self, words: List[str]) -> dict:
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        sorted_counter = {key:value for key, value in sorted(counter.items(), key=lambda item: (-item[1], item[0]))}
        return sorted_counter
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(self.sorted_counter(words).keys())[:k]
