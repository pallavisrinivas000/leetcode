from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 !=0:
            return False
        target = total // 2
        
        dp = [False] * (target +1)
        dp[0] = True

        for num in nums:
            for t in range(target, num-1, -1):
                if dp[t-num]:
                    dp[t] = True
        
        return dp[target]