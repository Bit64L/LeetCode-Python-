class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        T = numRows - 1
        n = len(s)
        col = numRows - 1
        row = -1
        count = 0
        arr = []
        while count < n:
            row += 1
            arr.append([0] * (col + 1))
            for j in range(col + 1):
                if row % T == 0:
                    arr[row][j] = s[count]
                    count += 1
                elif col - j == row % T:
                    arr[row][j] = s[count]
                    count += 1
                if count >= n:
                    break
        ans = ""
        for j in range(col + 1):
            for i in range(row + 1):
                if arr[i][j] != 0:
                    ans += arr[i][j]
        return ans


solution = Solution()
print(solution.convert("A", 1))
