class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output, accu = [], 1
        for i in range(0, len(nums)):
        	output.append(accu)
        	accu *= nums[i]

        accu = 1
        for i in range(len(nums) - 1, -1, -1):
        	output[i] *= accu
        	accu *= nums[i]
        return output

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))


# 思路：
# 第一次遍历数组，记录第i个元素前面元素的乘积，
# 第二次逆向遍历，记录第i个元素后面的乘积

# 注意：
# 1. 如何更优雅的解决边界条件（第一个元素和最后一个元素）？
#   初始化累积变量accu为1(乘积为1，求和为0)，先使用，然后再更新。 
#   如果先更新accu的话，会出现accu*=nums[i-1]这种情况，这时需要额外对i-1进行合法性验证，破坏代码的优雅性，同时也会扰乱思路。
