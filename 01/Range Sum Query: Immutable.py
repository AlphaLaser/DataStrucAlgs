# https://leetcode.com/problems/range-sum-query-immutable/solutions/5525857/303-range-sum-query-immutable-python-3-solution-please-upvote/

'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_array = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.prefix_sum_array.append(sum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefix_sum_array[right] - self.prefix_sum_array[left - 1]
        else:
            return self.prefix_sum_array[right]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
