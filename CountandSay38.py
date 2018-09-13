class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(1, n):
            s = self.convert(s)
        return s

    def convert(self, s):
        new_s = ""
        i, num, count = 0, s[0], 1
        while i < len(s):
            if i + 1 < len(s):
                if s[i + 1] != s[i]:
                    new_s += str(count) + num
                    num, count = s[i + 1], 1
                else:
                    count += 1
            i += 1
        new_s += str(count) + num

        return new_s


solution = Solution()
print(solution.countAndSay(5))
