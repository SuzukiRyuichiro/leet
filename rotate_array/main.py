from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = k % len(nums)
        self.rotate_on_spot(nums, 0, len(nums) - 1)
        self.rotate_on_spot(nums, 0, l - 1)
        self.rotate_on_spot(nums, l, len(nums) - 1)
        print(nums)

    def rotate_on_spot(self, arr: List[int], begin: int, end: int):
        while begin < end:
            arr[begin], arr[end] = arr[end], arr[begin]
            begin += 1
            end -= 1


sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 3)

