# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        if not sl or not sl:
            return []
        
        fp = sp = 0
        res = []
        while fp<len(fl) and sp<len(sl):
            if fl[fp][0] > sl[sp][1]:
                sp+=1
            elif fl[fp][1]<sl[sp][0]:
                fp+=1
            else:
                res.append([max(fl[fp][0],sl[sp][0]),min(fl[fp][1],sl[sp][1])])

                if fl[fp][1]>sl[sp][1]:
                    sp+=1
                else:
                    fp+=1

        return res