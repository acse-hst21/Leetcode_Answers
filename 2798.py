import numpy as np

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours = np.array(hours)
        hours -= target
        output = (hours >= 0).sum()

        return output
