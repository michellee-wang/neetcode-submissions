class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def c(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(c(i+1), c(i+2))
            return cache[i]
        return min(c(0), c(1))