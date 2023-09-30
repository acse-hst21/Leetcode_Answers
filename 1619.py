class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        five_percent = int(len(arr) / 20)

        shortened_arr = arr[five_percent: -(five_percent)]

        output = sum(shortened_arr) / len(shortened_arr)

        return output
