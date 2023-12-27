class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_seniors = 0
        for person in details:
            if int(person[-4:-2]) > 60:
                num_seniors += 1
        return num_seniors
