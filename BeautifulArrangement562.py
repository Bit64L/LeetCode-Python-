class Solution:

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        mark = [0] * (N + 1)
        self.ans = 0

        def helper(work, mark, N, mapping):
            if work > N:
                return 1
            cache_count = mapping.get(str(mark) + '-' + str(work), None)
            if cache_count is not None:
                return cache_count
            count = 0
            for i in range(1, N + 1):
                if mark[i] == 0 and (i % work == 0 or work % i == 0):
                    mark[i] = 1
                    count += helper(work + 1, mark, N, mapping)
                    mark[i] = 0
            mapping[str(mark) + '-' + str(work)] = count
        helper(1, mark, N, {})
        return self.ans

solution = Solution()
print(solution.countArrangement(15))
