# encoding:utf8
class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mapping = {}
        for i in nums:
            mapping[i] = mapping[i] + 1 if i in mapping.keys() else 1
        list_ = []
        import heapq
        for key, val in mapping.items():
            heapq.heappush(list_, (-val, key))
        print(list_)
        return [heapq.heappop(list_)[1] for i in range(k)]

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mapping = {}
        for i in nums:
            if i in mapping.keys():
                mapping[i] = mapping[i] + 1
            else:
                mapping[i] = 1
        list_ = []
        for key, val in mapping.items():
            list_.append([key, val])
        list_.sort(key=lambda x: x[1], reverse=True)
        return [list_[i][0] for i in range(k)]


solution = Solution()
print(solution.topKFrequent([2, 3, 4, 1, 4, 0, 4, -1, -2, -1], 2))

# 思路：统计后排序
# 注意：
# 1. sorted函数给dict排序的用法如下：
#   sort_ = sorted(mapping.items(), key=lambda x: x[1])
# 2. 第一次接触对排序
