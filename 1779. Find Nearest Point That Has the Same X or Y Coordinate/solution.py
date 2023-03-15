# You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def is_valid(x1,y1,point):
            return x1==point[0] or y1==point[1]
        def manhattan(x1,y1,point):
            return abs(x1-point[0])+abs(y1-point[1])
        
        min_idx = -1
        min_dst = 100000
        for idx,point in enumerate(points):
            if is_valid(x,y,point):
                dst = manhattan(x,y,point)
                if dst<min_dst:
                    min_dst = dst
                    min_idx = idx
        return min_idx
