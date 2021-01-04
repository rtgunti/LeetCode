class Solution:
    def isValid(self, s: str) -> bool:
        l = ['(', '{', '[']
        r = [')', '}', ']']
        q = list()
        for b in s:
            if b in l:
                q.append(b)
            else:
                if len(q):
                    try:
                        ch = l[r.index(b)]
                    except ValueError as ve:
                        return False
                    if q.pop() != ch:
                        return False
                else:
                    return False
        return False if len(q) else True


if __name__ == '__main__':

    s = "()[]{}"
    s = "([)]"
    s = "))(("
    sol = Solution()
    print(sol.isValid(s))
