class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
       	digits.reverse()
       	accu = 0
       	digits[0] += 1
       	for i in range(0, len(digits)):
       		digit = (digits[i] + accu) % 10
       		accu = int((digits[i] + accu) / 10)
       		digits[i] = digit
       	if accu != 0:
       		digits.append(accu)
       	digits.reverse()
        return digits



solution = Solution()
print(solution.plusOne([9,9,9,9]))