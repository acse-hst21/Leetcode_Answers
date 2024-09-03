class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_rep = ''.join([str(ord(x) - 96) for x in s])
        counter = 0
        while counter < k:
            num_rep = str(num_rep)
            num_rep = sum([int(x) for x in num_rep])
            counter += 1
        return num_rep 
