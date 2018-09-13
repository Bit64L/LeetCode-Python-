class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) == 0:
        	return []
        i, j = 0, len(numbers) - 1
        while i < j:
        	if numbers[i] + numbers[j] == target:
        		return [i+1, j+1]
        	elif numbers[i] + numbers[j] > target:
        		j -= 1
        	else:
        		i += 1
        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))