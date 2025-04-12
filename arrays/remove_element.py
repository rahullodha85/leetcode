from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            if i < len(nums) and nums[i] != val:
                nums[count] = nums[i]
                count += 1

        print(nums)

        return count

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    for i in range(0, s.removeElement(nums, val)):
        print(nums[i])