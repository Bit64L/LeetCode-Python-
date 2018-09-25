class Solution:

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        accus = [0, 32, -32]

        def helper(work, S, ans, path):
            if work == len(S):
                ans.append(path)
                return
            for accu in accus:
                if ord(S[work]) >= 48 and ord(S[work]) <= 57:
                    value = ord(S[work])
                else:
                    value = ord(S[work]) + accu
                    if not ((value >= 97 and value <= 122) or (value >= 64 and value <= 90)):
                        continue
                path += chr(value)
                helper(work + 1, S, ans, path)
                path = path[0:len(path) - 1]
                if ord(S[work]) >= 48 and ord(S[work]) <= 57:
                    break

        helper(0, S, ans, '')
        return ans


solution = Solution()
print(solution.letterCasePermutation('12345'))

# 递归回溯基本结构不变，根据题目做适当变形即可
