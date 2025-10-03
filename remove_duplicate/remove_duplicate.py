from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i, j = 0, 0
    while j < len(nums):
      if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]

      j += 1

    return len(nums)



sol = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
sol.removeDuplicates(nums)

