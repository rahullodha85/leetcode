from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for num in digits:
            number = number * 10 + num

        number += 1
        digits = []

        index = len(digits) - 1
        while number > 0:
            rem = number % 10
            digits.insert(0, rem)

            number = number // 10
            index -= 1

        return digits

if __name__ == "__main__":
    s = Solution()
    digits = [1, 2, 3]
    print(s.plusOne(digits))  # Output: [1, 2, 4]
    digits = [4, 3, 2, 1]
    print(s.plusOne(digits))  # Output: [4, 3, 2, 2]
    digits = [0]
    print(s.plusOne(digits))  # Output: [1]
    digits = [9]
    print(s.plusOne(digits))  # Output: [1, 0]
