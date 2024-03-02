class Solution:
    def minimumMoves(self, s: str) -> int:
        output = 0
        s_as_list = [*s]
        for index, _ in enumerate(s_as_list):
            if s_as_list[index] == 'X':
                try:
                    s_as_list[index + 1] = 'O'
                    s_as_list[index + 2] = 'O'
                except IndexError:
                    pass
                output += 1
        return output
