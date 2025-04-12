from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Check if nums1 is empty
        if len(nums1) == 0:
            nums1.extend(nums2)
            return
        elif len(nums2) == 0:
            return
        index_nums1 = 0
        index_nums2 = 0
        while index_nums1 < len(nums1) and index_nums2 < len(nums2):
            if nums1[index_nums1] <= nums2[index_nums2]:
                index_nums1 += 1
            # else:
            #     temp = nums1[index_nums1]
            #     nums1[index_nums1] = nums2[index_nums2]
            #     if index_nums1 + 1 == len(nums1):
            #         nums1.append(temp)
            #     else:
            #         nums1[index_nums1 + 1] = temp
            #     index_nums1 += 1
            #     index_nums2 += 1

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]