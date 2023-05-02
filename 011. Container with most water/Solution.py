# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getArea(x, y):
            return abs(x[1] - x[0]) * min(y[0], y[1])

        lp, rp = 0, len(height) - 1
        maximumArea = getArea((rp, lp), (height[lp], height[rp]))
        while rp > lp:
            if height[lp] < height[rp]:
                lp += 1
            elif height[lp] > height[rp]:
                rp -= 1
            elif getArea((rp, lp + 1), (height[lp + 1], height[rp])) > getArea(
                (rp - 1, lp), (height[lp], height[rp - 1])
            ):
                lp += 1
            else:
                rp -= 1
            proposed = getArea((rp, lp), (height[lp], height[rp]))
            maximumArea = proposed if proposed > maximumArea else maximumArea

        return maximumArea
