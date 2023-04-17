# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(x1,x2):
            return float('inf') if x2[0]-x1[0] == 0 else (x2[1]-x1[1])/(x2[0]-x1[0])
        if len(points)==1:
            return 1
        slopes = {}
        ends = {}
        
        left = 1

        while left<len(points):
            for idx in range(left):
                s = slope(points[left],points[idx])
                check = slopes.get(s)
                if not check:
                    slopes[s] = [[idx,left]]
                    ends[s] = 2
                elif check:
                    exists = False
                    for sec_idx,i in enumerate(check):
                        if idx in i and left not in i:
                            slopes[s][sec_idx].append(left)
                            exists = True
                            continue
                        elif idx in i and left in i:
                            exists = True
                            continue
                    if not exists:
                        slopes[s].append([idx,left])
                        
                        
            left+=1
        return max({i:max([len(j) for j in slopes[i]]) for i in slopes.keys()}.values())               
