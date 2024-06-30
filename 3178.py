class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        forward = [x for x in range(n)]
        backward = forward[1:-1][::-1]
        num_turns = -(-k//(n-1))
        full_list = []
        for turn in range(num_turns+1):
            if turn % 2 == 0:
                full_list += forward
            else:
                full_list += backward
        return full_list[k]
