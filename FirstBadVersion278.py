# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         if n == 1:
#             return 1
#         if n == 2:
#             return 2 if not isBadVersion(1) else 1

#         lo = 1
#         high = n
#         while lo <= high:
#             mid = int((lo + high) / 2)
#             if mid > 1:
#                 if isBadVersion(mid) and not isBadVersion(mid - 1):
#                     return mid
#                 elif isBadVersion(mid) and isBadVersion(mid - 1):
#                     high = mid - 1
#                 elif not isBadVersion(mid) and not isBadVersion(mid - 1):
#                     lo = mid + 1
#             else:
#                 return 2 if not isBadVersion(mid) else 1
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        high = n
        while lo <= high:
            mid = int((lo + high) / 2)
            if isBadVersion(mid):
                high = mid - 1
            else:
                lo = mid + 1
            if isBadVersion(lo) == isBadVersion(high):
                if isBadVersion(lo):
                    return lo
                else:
                    return high + 1
        return lo 

def isBadVersion(n):
    return True if n >= 4 else False


solution = Solution()
print(solution.firstBadVersion(5))
