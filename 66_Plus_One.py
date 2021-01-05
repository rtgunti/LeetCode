from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for ind in range(len(digits)-1, -1, -1):
            if digits[ind] + carry > 9:
                digits[ind] = (digits[ind] + carry) % 10
                carry = 1
            else:
                digits[ind] += carry
                carry = 0
        if carry:
            digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    sol = Solution()
    digits = [0]
    print(digits)
    res = sol.plusOne(digits)
    print(res)
