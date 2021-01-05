class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if (s == "" or s == " "):
            return 0
        while s[-1] == " ":
            if (s == "" or s == " "):
                return 0
            else:
                s = s[:-1]

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return len(s) - (i + 1)
        return len(s)


if __name__ == "__main__":
    sol = Solution()
    s = "a    ab   "
    print(sol.lengthOfLastWord(s))
