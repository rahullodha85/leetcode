class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_arr = list(s)
        while start < end:
            if s_arr[start] in vowels:
                if s_arr[end] in vowels:
                    temp = s_arr[start]
                    s_arr[start] = s_arr[end]
                    s_arr[end] = temp
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1

        return ''.join(s_arr)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels("leetcode"))
    print(s.reverseVowels("aA"))
