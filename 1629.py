class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        times = [releaseTimes[index+1] - releaseTimes[index] for index in range(len(releaseTimes)-1)]
        times.insert(0, releaseTimes[0])
        max_indices = [index for index in range(len(times)) if times[index] == max(times)]
        max_value = max([keysPressed[index] for index in max_indices])
        return max_value
