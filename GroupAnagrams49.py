class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        for str_ in strs:
            arr = list(str_)
            arr.sort()
            curr = mapping.get(str(arr), [])
            curr.append(str_)
            mapping[str(arr)] = curr
        return mapping.values()


solution = Solution()
print(solution.groupAnagrams(["",""]))
