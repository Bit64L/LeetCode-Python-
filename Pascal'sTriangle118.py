# class Solution:
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         if numRows < 1:
#         	return []
#         ans = [[1]]
#         for i in range(1, numRows):
#         	row_ans = []
#         	for j in range(0, i + 1):
#         		if j == 0 or j == i:
#         			row_ans.append(1)
#         		else:
#         			row_ans.append(ans[i-1][j] + ans[i-1][j-1])
#         	ans.append(row_ans)
#         return ans

class Solution:
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows + 1
        ans = [0] * n
        for i in range(0, n):
            for j in range(i, -1, -1):
                if j == 0 or j == i:
                    ans[j] = 1
                else:
                    ans[j] += ans[j - 1]
            tmp = ans
        return ans


solution = Solution()
print(solution.generate(5))
