from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_dict = {}

        if len(nums) < 2:
            return False

        for index in range(len(nums)):
            if nums[index] in index_dict.keys():
                index_dict[nums[index]] = {'index': index, 'index_diff': index - index_dict[nums[index]]['index'], 'count': index_dict[nums[index]]['count'] + 1}
            else:
                index_dict[nums[index]] = {'index': index, 'index_diff': 0, 'count': 1}

        for key in index_dict.keys():
            if index_dict[key]['index_diff'] <= k and index_dict[key]['count'] > 1:
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    # nums = [1,2,3,1]
    # k = 3
    # print(s.containsNearbyDuplicate(nums, k)) # Output: True
    # nums = [1,0,1,1]
    # k = 1
    # print(s.containsNearbyDuplicate(nums, k)) # Output: True
    # nums = [1,2,3,1,2,3]
    # k = 2
    # print(s.containsNearbyDuplicate(nums, k)) # Output: False
    # nums = [1,2]
    # k = 2
    # print(s.containsNearbyDuplicate(nums, k)) # Output: False
    nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
    k = 1
    print(s.containsNearbyDuplicate(nums, k)) # Output: True