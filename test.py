# Definition for an interval.
import json


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
        intervals.sort()
        ans = [intervals.pop(0)]
        for interval in intervals:
            if interval.start <= ans[-1].end:
                if interval.end > ans[-1].start:
                    ans[-1].end = interval.end
            else:
                ans.append(interval)
        return ans


def stringToInterval(input):
    tokens = json.loads(input)
    return Interval(tokens[0], tokens[1])


def stringToIntervalArray(input):
    intervalArrays = json.loads(input)
    nodes = []
    for intervalArray in intervalArrays:
        nodes.append(stringToInterval(json.dumps(intervalArray)))
    return nodes


def intervalToString(interval):
    return "[{}, {}]".format(interval.start, interval.end)


def intervalArrayToString(intervalArray):
    serializedIntervals = []
    for interval in intervalArray:
        serializedInterval = intervalToString(interval)
        serializedIntervals.append(serializedInterval)
    return "[{}]".format(', '.join(serializedIntervals))


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            intervals = stringToIntervalArray(line)

            ret = Solution().merge(intervals)

            out = intervalArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
