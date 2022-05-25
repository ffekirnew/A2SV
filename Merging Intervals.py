class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = 1
        number_of_intervals = len(intervals) - 1
        while i <= number_of_intervals:
            if intervals[i-1][1] >= intervals[i][1]:
                intervals.pop(i)
                number_of_intervals -= 1
            else:
                if intervals[i-1][0] >= intervals[i][0]:
                    intervals.pop(i-1)
                    number_of_intervals -= 1
                else:
                    if intervals[i][0] in range(intervals[i-1][0], intervals[i-1][1]+1):
                        intervals[i][0] = intervals[i-1][0]
                        intervals.pop(i-1)
                        number_of_intervals -= 1
                    else:
                        i += 1

        return intervals