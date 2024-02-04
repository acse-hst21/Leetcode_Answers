class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for row in range(2, numRows+1):
            temp = [1]
            for column in range(1, row-1):
                temp.append(output[-1][column] + output[-1][column-1])
            temp.append(1)
            output.append(temp)
        
        return output
