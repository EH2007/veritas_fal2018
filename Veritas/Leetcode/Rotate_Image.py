import copy
class Solution:
    def rotate(self, matrix):
        counter = 0
        for i in range(len(matrix)):
            counter = i
        new_matrix = copy.deepcopy(matrix)
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                matrix[row][column] = new_matrix[counter - column][row]
        return matrix

sol = Solution()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result = sol.rotate(matrix)
print(result)
