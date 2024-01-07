class Solution:
    def maxPower(self, s: str) -> int:
        output = 1
        current_value = 1
        for index, _ in enumerate(s):
            if index == 0:
                pass
            else:
                if s[index] == s[index - 1]:
                    current_value += 1
                else:
                    if current_value > output:
                        output = current_value
                    current_value = 1
        return max(current_value, output)
