# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its 
upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by 
its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])

        zero_arr = [[0] * (columns + 1) for i in range(rows + 1)] 

        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                zero_arr[row][column] = zero_arr[row - 1][column] + zero_arr[row][column - 1] - zero_arr[row - 1][column - 1] + matrix[row - 1][column - 1]

        self.prefix_sum_matrix = zero_arr
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum_matrix[row2 + 1][col2 + 1] - self.prefix_sum_matrix[row1][col2 + 1] - self.prefix_sum_matrix[row2 + 1][col1] + self.prefix_sum_matrix[row1][col1]
  

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
