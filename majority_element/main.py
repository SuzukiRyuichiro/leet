from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 0, 0
        for num in nums:
            if count == 0:
                result = num
            count += (1 if result == num else -1)

        return result
            
