class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len1:
            nums += nums1[i:]
        else:
            nums += nums2[j:]

        nums_len = len1 + len2
        if (nums_len - 1) % 2 == 0:
            ans = nums[int((nums_len - 1) / 2)]
        else:
            a = nums[int((nums_len - 1) / 2)]
            b = nums[int((nums_len - 1) / 2) + 1]
            ans = (a + b) / 2
        return ans


solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
