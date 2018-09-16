# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x.start)
        ans = [intervals.pop(0)]
        last = ans[0]
        for interval in intervals:
            if interval.start <= last.end:
                if interval.end > last.end:
                    last.end = interval.end
            else:
                ans.append(interval)
                last = interval
        return ans


solution = Solution()
ans = solution.merge([Interval(1, 4), Interval(2, 3)])
for i in ans:
    print(i.start, i.end)
