class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for index, num in enumerate(nums):
            if num in my_dict and abs(index - my_dict[num]) <= k:
                return True
            else:
                my_dict[num] = index
        return False
