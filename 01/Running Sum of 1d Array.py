# https://leetcode.com/problems/running-sum-of-1d-array/submissions/1338500907/

'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            final.append(sum)
        return(final)
