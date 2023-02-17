class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = []
        dp.append(nums[0])
        max_value = dp[0]
        for i in range(1, n):
            dp.append(max(nums[i], dp[i - 1] + nums[i]))
            max_value = max(dp[i], max_value)
        return max_value