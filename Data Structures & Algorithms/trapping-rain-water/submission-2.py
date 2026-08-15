class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1 
        rMax = height[r]
        lMax = height[l]
        total = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                lMax = max(lMax, height[l])
                # left max height minus current
                total += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                # for each the max height - current height 
                total += rMax - height[r]
        return total
                