# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/

'''
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.
'''

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:

        rows = len(grid)
        cols = len(grid[0])

        zero_arr = [[0] * (cols + 1) for row in range(rows + 1)]
        count = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                zero_arr[row][col] = zero_arr[row][col - 1] + zero_arr[row - 1][col] - zero_arr[row - 1][col - 1] + grid[row - 1][col - 1]
                if zero_arr[row][col] <= k:
                    count += 1 

        return count
