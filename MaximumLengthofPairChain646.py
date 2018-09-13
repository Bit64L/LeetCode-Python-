class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if pairs is None or len(pairs) == 0:
            return 0
        pairs.sort(key=lambda x: x[1])
        ans = 1
        for i in range(len(pairs)):
            last = pairs[i]
            temp_ans = 1
            for j in range(i + 1, len(pairs)):
                if last[1] < pairs[j][0]:
                    last = pairs[j]
                    temp_ans += 1
            ans = max(ans, temp_ans)
        return ans


solution = Solution()
print(solution.findLongestChain([[1, 2], [3, 4], [5, 6]]))
