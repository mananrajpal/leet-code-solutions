from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data= {}
        # Iterate over each number in the nums list
        for index, num in enumerate(nums):
            # Calculate how what num is required to be added to current
            # number to reach target
            second_number_required = target - num
            if second_number_required in data:
                return [data[second_number_required], index]
            data[num] = index

sol = Solution()
print(sol.twoSum([3, 2, 3], 6))