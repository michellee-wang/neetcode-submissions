class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            r = len(nums) - 1
            l = i + 1

            # 2 pointer logic
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: 
                    l += 1
                elif s > 0: 
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
        return [list(t) for t in res]