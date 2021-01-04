
from typing import List


class Solution:
    def getcstr(self, w1, w2):
        cstr = ''
        for (x, y) in zip(w1, w2):
            print(x, y)
            if x == y:
                cstr += x
            else:
                break
        print("cstr", cstr)
        return cstr

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        cstr = strs[0]
        for ind in range(len(strs)):
            cstr = self.getcstr(cstr, strs[ind])
        return cstr


if __name__ == '__main__':
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "dogo", "dogi"]
    cstr = sol.longestCommonPrefix(strs)
    print(cstr)
