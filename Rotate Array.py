class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # handle k > n

        # helper to reverse part of the array
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # 1) reverse whole array
        reverse(0, n - 1)
        # 2) reverse first k elements
        reverse(0, k - 1)
        # 3) reverse remaining elements
        reverse(k, n - 1)
