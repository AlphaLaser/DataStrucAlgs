# https://leetcode.com/problems/find-pivot-index/description/

'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum_array = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            prefix_sum_array.append(sum)

        postfix_sum_array = []
        sum = 0
        for i in range(len(nums) - 1, -1, -1):
            sum += nums[i]
            postfix_sum_array.append(sum)
        
        postfix_sum_array = postfix_sum_array[::-1] 

        for i in range(len(nums)):
            if prefix_sum_array[i] == postfix_sum_array[i]:
                return i
        
        return -1
