class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        try:
            haystack.index(needle)
        except ValueError as ve:
            return -1


if __name__ == '__main__':
    sol = Solution()
    haystack = 'aaaaa'
    needle = 'bba'
    print(sol.strStr(haystack, needle))
