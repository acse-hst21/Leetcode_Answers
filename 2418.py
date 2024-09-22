class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict = {height: name for height, name in zip(heights, names)}
        my_keys = list(my_dict.keys())
        my_keys.sort(reverse=True)
        return [my_dict[key] for key in my_keys]
