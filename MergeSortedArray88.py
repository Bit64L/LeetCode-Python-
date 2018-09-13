class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0, n):
        	j = m - 1 
        	while j >= 0 and nums1[j] > nums2[i]:
        		nums1[j+1] = nums1[j]
        		j -= 1
        	nums1[j + 1] = nums2[i]
       		m += 1


