class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      start = 0
      end = len(numbers) - 1
      while start < end:  
        numsum = numbers[end] + numbers[start]
        if numsum == target: 
            return [start+1, end+1]
        if numsum > target:
            end -= 1
        else:
            start += 1
        