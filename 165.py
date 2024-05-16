class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_sum = 0
        version2_sum = 0

        for index, num in enumerate(version1.split('.')):
            version1_sum += int(num) * 100**(-index)
        for index, num in enumerate(version2.split('.')):
            version2_sum += int(num) * 100**(-index)

        if version1_sum > version2_sum:
            return 1
        elif version1_sum < version2_sum:
            return -1
        else:
            return 0   
