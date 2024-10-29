class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        output = ''
        counter = defaultdict(int)
        
        for word in arr:
            counter[word] += 1
        
        index = 1
        for word in arr:
            if counter[word] == 1:
                if index == k:
                    output += word
                    break
                else:
                    index += 1
        return output
