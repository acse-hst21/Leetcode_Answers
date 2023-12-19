class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        converted_list = []
        for value in strs:
            try: 
                value = int(value)
                converted_list.append(value)
            except ValueError:
                converted_list.append(len(value))
        return max(converted_list)
