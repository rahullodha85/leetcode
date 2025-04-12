from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target in nums:
            return nums.index(target)

        # binary search
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,6]
    target = 5
    print(s.searchInsert(nums, target)) # Output: 2
    target = 2
    print(s.searchInsert(nums, target)) # Output: 1
    target = 7
    print(s.searchInsert(nums, target)) # Output: 4
    target = 0
    print(s.searchInsert(nums, target)) # Output: 0