class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        
        is_increasing = True

        for index in range(len(arr)-1):
            print(is_increasing)
            if arr[index] == arr[index+1]:
                return False
            if is_increasing:
                if arr[index] > arr[index+1]:
                    is_increasing = False
            else:
                if arr[index] < arr[index+1]:
                    return False
        return not is_increasing
