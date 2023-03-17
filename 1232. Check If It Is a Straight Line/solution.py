# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1,p2):
            return p2[1]-p1[1],p2[0]-p1[0]

        if len(coordinates)==2:
            return True
        dy,dx = slope(coordinates[1],coordinates[0])
        for i in range(2,len(coordinates)):
            dy_n,dx_n = slope(coordinates[i],coordinates[i-1])
            if dy_n*dx != dx_n*dy:
                return False
        
        return True