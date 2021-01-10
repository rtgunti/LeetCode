class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(int(a, 2), int(b, 2))
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    sol = Solution()
    a = str('100')
    b = str('100')
    print(sol.addBinary(a, b))
