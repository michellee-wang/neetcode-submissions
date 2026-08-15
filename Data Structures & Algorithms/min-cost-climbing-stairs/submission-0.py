class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # create DP array of minimum cost of reaching each floor
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            # fill the DP array with minimum cost
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]        