class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        counter = 0
        for index1 in range(len(hours)):
            for index2 in range(len(hours)):
                if index1 == index2:
                    continue
                if (hours[index1]+hours[index2]) % 24 == 0:
                    counter += 1
        return int(counter/2)
