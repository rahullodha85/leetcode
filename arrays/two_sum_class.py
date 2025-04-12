class TwoSum:

    def __init__(self):
        self.numbers = []

    def add(self, number: int) -> None:
        self.numbers.append(number)

    def find(self, value: int) -> bool:
        print(self.numbers)
        if len(self.numbers) < 2:
            return False
        for number in self.numbers:
            if (value - number) in self.numbers:
                if (value - number) != number or self.numbers.count(number) > 1:
                    return True

        return False

if __name__ == "__main__":
    two_sum = TwoSum()
    two_sum.add(3)
    two_sum.add(2)
    two_sum.add(1)
    print(two_sum.find(2))  # Output: False
    print(two_sum.find(3))  # Output: True
    print(two_sum.find(4))  # Output: True
    print(two_sum.find(5))  # Output: True
    print(two_sum.find(6))  # Output: False