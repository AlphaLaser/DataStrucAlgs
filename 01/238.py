# https://leetcode.com/problems/product-of-array-except-self/description/

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = []
        product = 1

        for i in nums:
            product *= i
            pre.append(product)

        post = []
        product = 1

        for i in nums[::-1]:
            product *= i
            post.append(product)

        post = post[::-1]
        final = []

        final.append(post[1])
        for i in range(1, len(nums) - 1):
            final.append(pre[i - 1] * post[i + 1])
        final.append(pre[len(nums) - 2])

        return final
