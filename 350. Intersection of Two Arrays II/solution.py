# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = list(set(nums1).intersection(nums2))
        for i in intersection:
            x = nums1.count(i)
            y = nums2.count(i)
            t = intersection.count(i)
            if x>=y:
                intersection+=[i]*(y-t)
            elif y>x:
                intersection+=[i]*(x-t)
        return intersection