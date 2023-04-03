# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idxs = []
        if len(intervals)==0:
            return [newInterval]
        for idx,interval in enumerate(intervals):
            if interval[0]>newInterval[1]:
                break
            if (newInterval[0]>=interval[0] and newInterval[1]>=interval[1] and newInterval[0]<=interval[1]) or (newInterval[0]<=interval[0] and newInterval[1]>=interval[1]) or (newInterval[0]<=interval[0] and newInterval[1]<=interval[1]) or (newInterval[0]>=interval[0] and newInterval[1]<=interval[1]):
                idxs.append(idx)
        
        if idxs:
            intervals = intervals[:idxs[0]]+[[min(intervals[idxs[0]][0],newInterval[0]),max(intervals[idxs[-1]][1],newInterval[1])]]+intervals[idxs[-1]+1:]
        else:
            intervals+=[newInterval]
            intervals.sort()

        return intervals          