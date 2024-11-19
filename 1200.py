class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        output = [[arr[0], arr[1]]]
        for index in range(1, len(arr)-1):
            current_diff = abs(output[0][0] - output[0][1])
            if abs(arr[index] - arr[index+1]) > current_diff:
                pass
            elif abs(arr[index] - arr[index+1]) == current_diff:
                output.append([arr[index], arr[index+1]])
            else:
                output.clear()
                output.append([arr[index], arr[index+1]])
        return output
