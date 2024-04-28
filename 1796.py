class Solution:
    def secondHighest(self, s: str) -> int:
        list_nums = []
        for char in s:
            try:
                list_nums.append(int(char))
            except ValueError:
                pass
        if len(list_nums) == 0:
            return -1
        sorted_nums = sorted(set(list_nums))
        if sorted_nums[0] == sorted_nums[-1]:
            return -1
        return sorted_nums[-2]
